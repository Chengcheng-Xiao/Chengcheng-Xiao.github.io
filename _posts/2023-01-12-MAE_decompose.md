---
layout: post
title: Orbital decomposition of magnetic anisotropy energy using VASP
date: 2023-01-12
categories: Post
description: The magnetic anisotropy energy can be decomposed into orbtial pair contributions using second order perturbation analysis. This is a short tutorial on how to do this.
tags: DFT
---

The spin-orbital coupling term can be simply added to the hamiltonian so that the full Hamiltonian is:

$$
H = H_0 + H_\mathrm{SO} = H_0 + \lambda(r) \hat \sigma \cdot \hat L
$$

where the SOC strength is:

$$
\lambda(r) = \frac{1}{4c^2r} \frac{\partial V}{\partial r}
$$

For 3d states, the integrated value of $\lambda(r)$ is about 30meV, comparing to the usual hoppin parameter, this energy is negliable and the SOC term could be treated as perturbation to $H_0$.

Using perturbation theory, the first order energy correction is:

$$
E^{(1)}_\mathrm{SO} = \sum_n \braket{n|H_\mathrm{SO}|n}
$$

where $\ket{n}$ are the wavefunctions (eigenvectors) to the original Hamiltonian $H_0$. Due to time reversal symmetry, this term is evaluated to zero.

The second order energy correction is:

$$
E_\mathrm{SO}^{(2)} = \sum_{oj} \frac{\braket{o|H_\mathrm{SO}|j}^2}{\epsilon_o-\epsilon_j}
$$

where $o$ denotes the occupied states and $j$ sums over all states. However, when $j$ is also an occupied state, the two terms arising from the exchange of $o$ and $j$:

$$
 \frac{\braket{o|H_\mathrm{SO}|j}^2}{\epsilon_o-\epsilon_j} = - \frac{\braket{j|H_\mathrm{SO}|o}^2}{\epsilon_j-\epsilon_o}
$$

cancels eache other.

So the interaction can only happen between occupied ($o$) and empty states ($u$):

$$
\begin{aligned}
E_\mathrm{SO} &= \sum_{o,u} \frac{\braket{o|H_\mathrm{SO}|u}^2}{\epsilon_o-\epsilon_u} \\
&= \lambda^2 \sum_{o,u} \frac{\braket{o|\hat \sigma \cdot \hat L|u}^2}{\epsilon_o-\epsilon_u} 
\end{aligned}
$$

---

<!-- In a strong exchange splitting limit where spin up states are all occupied and spin down states are partially occupied, we have two couplings: -->

If we also include spin degrees of freedom, we could have two types of coupling:

- The coupling between occupied down/up and unoccupied down/up states.
- The coupling between occupied up and unoccupied down states.

The total SOC energy is approximately (ignoring third order an up terms) equal to the sum of these two contributions:

$$
E_\mathrm{SO} = E_{--} + E_{++} + E_{-+} + E_{+-}
$$

where:

$$
\begin{aligned}
E_{--} = - \lambda^2 \sum_{o^-,u^-} \frac{\braket{o^-|\hat \sigma \cdot \hat L|u^-}}{\epsilon_{u^-}-\epsilon_{o^-}}\\
E_{++} = - \lambda^2 \sum_{o^+,u^+} \frac{\braket{o^+|\hat \sigma \cdot \hat L|u^+}}{\epsilon_{u^+}-\epsilon_{o^+}}\\
E_{+-} = - \lambda^2 \sum_{o^+,u^-} \frac{\braket{o^+|\hat \sigma \cdot \hat L|u^-}}{\epsilon_{u^-}-\epsilon_{o^+}}\\
E_{-+} = - \lambda^2 \sum_{o^-,u^+} \frac{\braket{o^-|\hat \sigma \cdot \hat L|u^+}}{\epsilon_{u^+}-\epsilon_{o^-}}\\
\end{aligned}
$$

Depending on the magnetization axis, assuming that there are no mixing in the orbital part, we can write the spin part of the spinor wavefunction as:

- magnetization along x axis: $(1, -1)$
- magnetization along z axis: $(0, 1)$

For example, inserting these into $\braket{o^-\vert\hat{\sigma}\hat{L}\vert u^-}$, we have:

$$
\begin{aligned}
|\braket{o^-|\hat \sigma \hat L|u^-}_x|^2 &= |\braket{o^-|L_x|u^-}|^2 \\
|\braket{o^-|\hat \sigma \hat L|u^-}_z|^2 &= |\braket{o^-|L_z|u^-}|^2
\end{aligned}
$$

The energy difference bewteen these two terms is:

$$
\mathrm{MAE}_{--} = E_{--}^x - E_{--}^z = \lambda^2 \sum_{o^-,u^-} \frac{|\braket{o^-|L_z|u^-}|^2-|\braket{o^-|L_x|u^-}|^2}{\epsilon_{u^-}-\epsilon_{o^-}}
$$

Similarly, we can calculate the up-down component as,

$$
\mathrm{MAE}_{+-} = E_{+-}^x - E_{+-}^z = - \lambda^2 \sum_{o^+,u^-} \frac{|\braket{o^+|L_z|u^-}|^2-|\braket{o^+|L_x|u^-}|^2}{\epsilon_{u^-}-\epsilon_{o^+}}
$$

Combining up-up, up-down, down-down and down-up temrs together, we get the total MAE as:

$$
\mathrm{MAE} = \lambda^2 (2\delta_{\alpha,\beta}-1) \sum_{o^{\alpha},u^{\beta}} \frac{|\braket{o^{\alpha}|L_z|u^{\beta}}|^2-|\braket{o^{\alpha}|L_x|u^{\beta}}|^2}{\epsilon_{u^{\beta}}-\epsilon_{o^{\alpha}}}
$$

Note that, up to now, we are trating $\lambda$ as a parameter. However, in reaility, it needs to be calculated as $\braket{\phi\vert\lambda(r)\vert\phi}$ where $\phi$ is the radial part of the atomic wavefunctions, which is different for different $l$ quantum numbers. In VASP, this is calculated within the PAW sphere using the all-electron partial waves in `relativistic.F`. If we really want to be percise, we can extract the exact values from VASP.

---

Using [:link: wanSOC](https://github.com/Chengcheng-Xiao/wanSOC) package, I've re-produced Fig. 2(b) of [10.1038/s42005-018-0078-4](https://www.nature.com/articles/s42005-018-0078-4.pdf).

![]({{site.baseurl}}/assets/img/post_img/2023-01-12-img1.png){:height="100%" width="100%" .center}

Subtle differences are caused by VASP's periodic conditions that breaks the rotational invariancce of the $d_{xy}$/$d_{x^2-y^2}$ orbitals.

The code that I wrote to do this can be downloaded from [:file_folder: 2023-01-12-MAE_decomposition.tar.gz]({{site.baseurl}}/assets/other/2023-01-12-MAE_decomposition.tar.gz). 











