---
layout: post
title: Testing Berry phase method in VASP and QE for 2D system
date: 2019-08-10
tags: ["Berryphase"]
categories: DFT
description:
---
The VASP and QE both have berry phase module that calculate the electronic polarization automagically. However, their results always seem to be puzzling, especially for low dimensional systems. To get a clear picture of how to these routine performs in 2D systems, I used monolayer NbN sheet as an example, calculating dipole moment using both charge center method and berryphase one. Also, in order to compare with polarization lies within the periodical directions, an prototypical $$BaTiO_{3}$$ system was tested using the same routine.

Before diving into things, let review some basic concepts that are of paramount importance to later calculations.

## Background

According to the modern theory of polarization, the electrical polarization depends on the difference of dipole moment between centro-symmetric system and non-centro-symmetric stucture. The reason behind is that the polairzation cannot be uniquely determined due to periodical boundary conditions.(That is, translation of unitcell vector can yield unphysical movements in the charge centers.)

Toillustrate this, first, consider a imaginary one dimensional atomic chain that have two differenc atoms: a anion and a cation.

![]({{site.baseurl}}/assets/img/post_img/2019-08-10-img1.png)
{: .center}

We can easily determine the dipole moment pointing from the anion to the cation.

However, the physical world does not work in such simple way. If we take a step deeper, differentiate the electrons and ions, the problem become much harder to solve:

![]({{site.baseurl}}/assets/img/post_img/2019-08-10-img2.png)
{: .center}

Here, the electrons are represented as charge density and are spread out between two ions. To get the charge center for electrons, we have to integrate the charge density in the unitcell:

$$\langle r_{electron} \rangle = \int_{unitcell}dr*\rho(r)$$

And the positive charge center can be found:

$$\langle R_{ion} \rangle = \Sigma_{i=A,B} R*Q_{i} /Q_{total}$$


These expressions seem to be very easy to solve, but it actually depends on the choice of unicell. For example, if we translate the unitcell a litte to the right:

![]({{site.baseurl}}/assets/img/post_img/2019-08-10-img3.png)
{: .center}

Taking a closer look at the picture, some charge "jumped" from the left end to the right end due to periodical conditions. And even though the structrure is unchanged, this translation changes the charge center of electrons while left the ion center unaffected.

To eliminate this ambiguity, Vanderbile and others found out that it is not the dipole moment for non-centrosymmetric phase that matters, the actual polarization depends on the change of polarization from the non-centrosymmetric phase to the centro-symmetric phase.

__Side Note:__  *how to define a centrosymmetric phase?*

__Answer:__ *Calculate optimum transition route and extract the local maxima as centrosymmetric phase.*


## Implementation


## 2D System
2D-NbN, as an out of plane ferroelectric system suggested by Anuja et al, have exotic switchable out-of-plane (OOP) polarization which can happen without switching of ionic positions. I choose this to show how Berry phase method can, sometimes, be cumbersome and have boundaries in certain systems.

![]({{site.baseurl}}/assets/img/post_img/2019-08-10-img4.png)
{: .center}

The system consist of one Nb and one N atom that forms a Boron Nitride like structure. The polarization can be switched by switching the $$\Delta$$ in the z axis:

$$\Delta=Z_{Nb}-Z_{N}$$

Due to the fact that this structure possess OOP polarization in which the periodical conditions are broken, the charge center can be uniquely defined since the charge density reverts to zero at the vacuum region.

The vacuum region is chosen as around 30 so that imaging counterpart does minimum effects on each other.

![]({{site.baseurl}}/assets/img/post_img/2019-08-10-img5.png)
{: .center}

## Charge Center method
The charge center method is performed using this tool ([LINK](https://raw.githubusercontent.com/Chengcheng-Xiao/Tools/master/VASP/chgcent.py)). The final polarization obtained for intrinsic NbN monolayer is:

$$Polarization=3.28 pC/m$$

And the transition curve is obtained almost identical to the published result:

![]({{site.baseurl}}/assets/img/post_img/2019-08-10-img6.png)
{: .center}

## VASP berryphase
To avoid error as mentioned in [LINK](https://www.sciencedirect.com/science/article/pii/S0022459612003234), I performed both automatic and manual berryphase calculation using the tag:
```
LDIPOL = .TRUE.
IDIPOL = 3
DIPOL = 0.5 0.5 0.2681174992499997
LCALCPOL = .T.
```
And
```
LDIPOL = .TRUE.
IDIPOL = 3
DIPOL = 0.5 0.5 0.26378659
LBERRY = .TRUE.
IGPAR  = 3
NPPSTR = 1
```
The final results does not make sense as:
```
Ionic dipole moment: p[ion]=(   -10.24777     5.91655     0.00000 ) electrons Angst

Total electronic dipole moment: p[elc]=(    -3.63403     2.09811    29.94773 ) electrons Angst
```
And
```
e<r>_ev=(     0.00209     0.00028    -0.01672 ) e*Angst
e<r>_bp=(     0.00000     0.00000    29.96212 ) e*Angst

Total electronic dipole moment: p[elc]=(     0.00209     0.00028    29.94540 ) e*Angst

ionic dipole moment: p[ion]=(    -6.30632    12.74335     0.00000 ) e*Angst
```

No matter how I tried: a different K-points, a different DIPOL value ... the `p[elc]` does not change and stays at around 30 e*Angst.
One thing that I notice: changing DIPOL tag greatly affects the convergence (mostly due to add in dipole corrections) and `p[ion]` value. But it does absolutely nothing to `p[elc]` which is puzzling.

Think about it, if we can define the origin of the cell using `DIPOL` and the electronic polarization does not change with this tag, how can we confidently say adding the electronic part to the ionic part is the right way to obtain the total  polarization?

As of now, I don't know how to use VASP's berry phase  routine to calculate electronic polarization on the non-periodical direction (OOP).


----

_**So, what about polarization on the periodical directions?**_

----

## 3D system
Now lets consider a prototypical $$BaTiO_{3}$$ unitcell:


By varying the atomic displacement from the centrosymmetric phase (CENT) to ferroelectric one (FE). VASP produce a series of ionic and electronic contribution to the total dipole moment.

| Image | Ion (elect*A) | Electron (elect*A) |
|-------|---------------|--------------------|
| 0 (CENT)    | 0             | 0                  |
| 1     | -12.01278     | -0.29138           |
| 2     | -11.92507     | -0.58047           |
| 3     | -11.83735     | -0.86532           |
| 4     | -11.74963     | -1.14461           |
| 5     | -11.66192     | -1.41757           |
| 6 (FE) | -11.5742      | -1.68399           |

It is clear that the centrosymmetric one has a wrong ionic contribution to the total polarziation.

At first, I thought this is due to the imposed symmtry constraint. However, after switch off symmetry entirely (ISYM=-1), VASP still produce this abnormal value of 0.0 elect*A for centrosymmetric phase.

After figure out which value is clearly wrong, we can now proceed to calculate total polarization
```
Total ionic contribution = 0.5258 elect*A
Total electronic contribution = -1.68399 elect*A
Total dipole moment = -1.15819
Volume = 64.35864801 A^3

Total polarization = -0.288293871 C/m^2
```

Exactly the same with [LINK](https://docs.quantumwise.com/tutorials/polarization/polarization.html) and [experimental value](https://journals.aps.org/pr/abstract/10.1103/PhysRev.99.1161) of 0.26 C/m^2.

By far, every thing works fine for the periodical system in VASP. The only problem is that the centrosymmetric phase's ionic part cannot be automatically calculated (or the output cannot be trusted).

There are two way of solving this:

  #1.calculate a series of structure points, linear fitting to make sure the "correctness" of the ionic part.

  #2. manually calculate ionic contribution by:

$$\mathbf{Dipole} = - \sum_j Z_j^{ion}\tau_j$$

where $$Z_j^{ion}$$ is the valence electron number of atom j and $$\tau_j$$ is its positions (relative to `DIPOL`). And substract the centrosymmetric one to the ferroelectric one. The minus sign is to count the charge sign of ions and electrons.

_**So far so good.**_ I am now confident that at least, VASP's berryphase routine works correctly on periodical directions.


## QE berryphase

(*to be continued*)
