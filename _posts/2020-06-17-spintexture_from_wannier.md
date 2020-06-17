---
layout: post
title: Calculating spin texture from DFT and Wannier Hamiltonian.
date: 2020-06-17
tags: ["Wannier functions"]
categories: DFT
description: A brief tutorial on calculating (plotting) spin texture from Wannier Hamiltonian
---

## Background

Spin texture describes the pattern which k-dependent spin directions formed in the Brillouin zone.

This peculiar phenomena arises from the coupling between spin and orbital motions of electrons -- spin-orbital coupling (SOC).
Without this coupling, the spin would remain in a "collinear" state and be rotationally invariant.
However, when the SOC is introduced, spin moments are coupled to the anisotropic orbital degrees of freedom which makes them also anisotropic.
This explains the origin of the magnetic anisotropy and the spin texture as well as other exotic phenomenas in condense matter physics.
A rigorous derivation of the SOC Hamiltonian needs relativistic quantum mechanics with many-body interactions.
However, here, I'm presenting a simple "pictorial" description of this phenomena:
The orbital motion of electrons generates a magnetic field, and that magnetic field acts on the spin magnetic moment which makes it precess along that magnetic field direction ("Larmor" precession).
This coupling will generate an energy splitting between different spin directions, hence changing the expectation value of the Pauli matrix.

A simple spin orbital Hamiltonian (can be added to the non-SOC Hamiltonian):

$$\textbf{H}_{soc} = \gamma \sigma \cdot L$$

where $$S$$ and $$L$$ are the spin operator(Pauli matrix) and the angular momentum operator, $$\gamma$$ is the spin-orbital coupling strength constant.

## VASP
### implementation
VASP only consider the SOC effect in "the immediate vicinity of the nuclei" which they uses the PAW spheres as the boundary.
This means they have to use the all-electron partial waves to calculate the spin orbital matrix element and subsequently the total add-on energy.
If you take a close look at the source code, you will find the overlap is calculated by sandwiching the overlap operator

$$\textbf{S} = \textbf{1}+\sum_{ij} Q_{ij} |\beta_{i}><\beta_{j}|$$

### How to?
VASP already provide the projected spin expectation value for each orbital (in x,y,z direction) in `PROCAR` file.

we can use [pyprocar](https://github.com/romerogroup/pyprocar) to plot it.

```
import pyprocar
pyprocar.repair('PROCAR') # usually needed.
pyprocar.fermi2D('PROCAR-repaired', outcar='OUTCAR', st=True, energy=-0.14, noarrow=False, spin=1, code='vasp')
```

__Now, results!__

![]({{site.baseurl}}/assets/img/post_img/2020-06-17-img1.png)
{: .center}

This is a 2D plot of the spin texture. the x and y axis are the rec. space vectors (well, not exactly. Since we have a hex cell, but you konw the gist). The cut energy is set 0.14eV below fermi level, and we have 2 black circle-shape thingy.
They correspond to two different bands, and judging by the arrows (they are the spin expectation vectors in x-y plane), we can safely say they correspond to the opposite spin of a single orbital (in "collinear" sense, up and down).

## Wannier90
### implementation
In the projection routine, VASP project the Bloch function onto a set of pure guiding functions with only one spinor component (this is not necessarily true since I've changed it in my fix, allowing one to specify spin quantisation axis but thats different).
In the mean time, VASP doesn't support writing spin matrix element for each k-point and band (yet, I'll try to implement it [here](https://github.com/Chengcheng-Xiao/VASP2WAN90_v2_fix)).
So if the projection is skewed and we need to mix everything together by doing iterative minimisation (e.g. random projection and a large `num_iter`), then we cannot guarantee the spinor components are well separated and cannot get the right spin-texture.
However, if our initial guess is pretty good (e.g. we can get perfect band interpolation without iterative minimisation), it is usually safe to assume we will get the right spin-texture. On a side note, I found that even with some mixing, if the initial guess is good, we can still get good result.

### How to?
We need:
  - `hr.dat` file
  - `.win` file
  - `\_band*` file

If you dont know how to calculate Wannier functions, go [here](https://github.com/Chengcheng-Xiao/TB_play)!

I've decided to use [pythtb](https://www.physics.rutgers.edu/pythtb/) as my diagonalisation tool (I'm lazy and I use python 2. Yeah, I know what you thinking...)

Since the Hamiltonian and the Pauli matrix commutes. After we obtained the eigenvectors from diagonalising the Hamiltonian, we can apply the coefficients to the Pauli matrix and obtain the expectation value. Since we are in linear territory, we can add the up/down components' coefficients and apply the Pauli matrix or apply Pauli matrix to each set of spinors (for each orbital) and added them up.
Choose you flavour.

It's coding time! (I use [Atom](https://atom.io/) and [hydrogen](https://atom.io/packages/hydrogen) so `#%%` has special meaning, check it out!)
```
#!/usr/bin/env python

from pythtb import * # import TB model class
import matplotlib.pyplot as plt

# read output from Wannier90 that should be in folder named "example_a"
#   see instructions above for how to obtain the example output from
#   Wannier90 for testing purposes
InSe=w90(r"output/wannier90",r"wannier90")

# get tight-binding model without hopping terms above 0.01 eV
my_model=InSe.model()
#%% k_mesh parameters
ksize_x = 21
ksize_y = 21
krange = 1.0
origin = [-krange/2,-krange/2]

#%% set up k grid
k_vec = np.empty([(ksize_x)*(ksize_y),3])
for a in range(ksize_x):
    for b in range(ksize_y):
        k_vec[a*ksize_x+b]=[origin[0]+a*(krange/ksize_x),origin[1]+b*(krange/ksize_y),0.0]

# or use automatic generation (1st BZ, 1st quadrant only)
# k_vec = my_model.k_uniform_mesh([ksize_x,ksize_y,1])
(evals,evacs)=my_model.solve_all(k_vec,eig_vectors=True)

#%% reordering everything
# reorder kpoints
k_vec_new = k_vec.reshape(ksize_x,ksize_y,3)
# reorder evacs, need to swap axis to fortran like...
evacs_new = evacs.reshape(22,ksize_y,ksize_x,22).swapaxes(1,2)
# reorder evals, need to swap axis to fortran like...
evals_new = evals.reshape(22,ksize_x,ksize_y).swapaxes(1,2)

#%% get me spin expectatin value, see pauli matrix... duh.
nband = 16 # check band structure to see which band you want.... duh.
exp = np.empty([ksize_x,ksize_y,3],dtype=np.complex)
for a in range(ksize_x):
    for b in range(ksize_y):
        # for non-sprcified non-collinear spin channels, we use default order (orb1_up, orb1_down, orb2_up, orb2_down..)
        # this default order only works with Wannier90 v2.1.0+
        exp[a,b,0] = np.dot(np.conjugate(evacs_new[nband,a,b,0::2]),complex(+1,0)*evacs_new[nband,a,b,1::2])\
                   + np.dot(np.conjugate(evacs_new[nband,a,b,1::2]),complex(+1,0)*evacs_new[nband,a,b,0::2])
        exp[a,b,1] = np.dot(np.conjugate(evacs_new[nband,a,b,0::2]),complex(0,-1)*evacs_new[nband,a,b,1::2])\
                   + np.dot(np.conjugate(evacs_new[nband,a,b,1::2]),complex(0,+1)*evacs_new[nband,a,b,0::2])
        exp[a,b,2] = np.dot(np.conjugate(evacs_new[nband,a,b,0::2]),complex(+1,0)*evacs_new[nband,a,b,0::2])\
                   + np.dot(np.conjugate(evacs_new[nband,a,b,1::2]),complex(-1,0)*evacs_new[nband,a,b,1::2])

#%% plot spin texture
import matplotlib.transforms as mtransforms

fig, ax = plt.subplots()
# get tran_data function, this will slightly change the direction of the spin vector, but quantitavely its alrigh.
trans_data = mtransforms.Affine2D().skew_deg(-15, -15).rotate_deg(-15) + ax.transData

x = np.arange(origin[0],krange/2.,krange/ksize_x)
y = np.arange(origin[1],krange/2.,krange/ksize_y)

# M = exp[:,:,2].astype('float64') # use sigma_z as color map
M = evals_new[nband,:,:] # use eigenval as color map

im = ax.quiver(x,y,exp[:,:,0],exp[:,:,1],M, scale=13,pivot='mid',transform = trans_data)
# ax.axis([origin[0],krange/2,origin[1],krange/2])
ax.set_aspect('equal')
ax.set_title("band# "+str(nband))
plt.savefig("spintexture_band_"+str(nband)+".png", dpi=300)
# plt.show()

# %% plot fermi surface [or 3D band surface]
import matplotlib.transforms as mtransforms

fig, ax = plt.subplots()
im = ax.imshow(evals_new[17,:,:],
               extent=[origin[0],krange/2,origin[1],krange/2],
               aspect=1,interpolation='lanczos',origin='lower')
# skew and rotate to match k vectors.
trans_data = mtransforms.Affine2D().skew_deg(-15, -15).rotate_deg(-15) + ax.transData
im.set_transform(trans_data)
# reset axes limit
x1, x2, y1, y2 = im.get_extent()
ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], "-",
        transform=trans_data)

ax.set_title("band# "+str(nband))
plt.savefig("fermi_surface_band_"+str(nband)+".png", dpi=300)
```
__And now, some tasters:__

![]({{site.baseurl}}/assets/img/post_img/2020-06-17-img2.png)
{: .center}

![]({{site.baseurl}}/assets/img/post_img/2020-06-17-img3.png)
{: .center}

Here, I'm plotting the spin textrue for two band (No. 17 and No. 18).
I did not use the cut plane method (contrary to the 'direct from DFT' method), instead, I'm showing the eigenvalue of each band with different colour. `Yellow -> higher in energy`, `Black -> lower in energy`.

Well, to me, they look __pretty good__ and __similar to the DFT result__.
## Caveats
for Wanneir90 v2.1.0+, I've changed the spinor order in the VASP2wannier90 interface.
The new spinor orbital order (example):
```
site 1 projection s  (spin_1)
site 1 projection s  (spin_2)
site 1 projection px (spin_1)
site 1 projection px (spin_2)
site 1 projection py (spin_1)
site 1 projection py (spin_2)
```
the old spinor orbital order (example):
```
site 1 projection s  (spin_1)
site 1 projection px (spin_1)
site 1 projection py (spin_1)
...
site 1 projection s  (spin_2)
site 1 projection px (spin_2)
site 1 projection py (spin_2)
```

## Input

I've put all input file in a zip file for download: [VASP]. Have fun computing!

[VASP]:{{site.baseurl}}/assets/other/2020-06-17-W90_spintexture.zip
