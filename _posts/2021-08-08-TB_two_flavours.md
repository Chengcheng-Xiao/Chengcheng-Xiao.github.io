---
layout: post
title: Tight-binding, two flavours🍦
date: 2021-08-08
categories: DFT
description: two flavours of calculating tight-binding band structures.
---
Read [🔗this](https://cpb-us-w2.wpmucdn.com/u.osu.edu/dist/3/67057/files/2018/09/tight-binding_model_in_the_second_quantization_formalism-1egl8n3.pdf) for introduction to TB method in a solid state physics perspective.

Read [🔗this](http://www.physics.rutgers.edu/~eandrei/chengdu/reading/tight-binding.pdf) for introduction to TB method in a QFT perspective.

## Flavour 1
In this flavour, we first construct a real-space Hamiltonian and then Fourier transform it to reciprocal space to get the band structrue.

### Steps to solve real-space TB hamiltonian

1. write real-space Hamiltonian.
2. transform the real-space Hamiltonian to reciprocal space.
3. change one of the exponential $e^{ikr}$ to $e^{ik(r-r')} \cdot e^{ikr'}$.
4. use definition of the delta function: $\delta(k,k') = \frac{1}{N} \sum_j e^{i(k-k')r_i}$.
5. Using ladder operator in reciprocal space as basis and write the Hamiltonian in matrix form.


### 1D atomic chain
The real space Hamiltonian (assuming only nearest-neighbor hoppings):

$$
H = -t \sum_i (a_i^\dagger a_{i+1} + a_{i+1}^\dagger a_{i}).
\tag{1}
$$

Remember that:

$$
\begin{aligned}
a_i^\dagger &= \frac{1}{\sqrt{N}} \sum_{k} e^{-ikr_i} a_k^\dagger\\
a_i &= \frac{1}{\sqrt{N}} \sum_{k} e^{ikr_i} a_k,
\end{aligned}
\tag{2}
$$

so that:

$$
\hat H = -\frac{t}{N} \sum_i (\sum_k e^{-ikr_i} a_k^\dagger \sum_k' e^{ik'r_{i+1}}a_k + \sum_k e^{-ikr_{i+1}} a_k^\dagger \sum_k' e^{ik'r_{i}}a_k)
\tag{3}
$$

next, we replace $e^{ik'r_{i+1}}$ ($e^{ik'r_i}$) with $e^{ik'(r_{i+1}-r_i)}\cdot e^{ik'(r_i)}$ ($e^{ik'(r_i-r_{i+1})}\cdot e^{ik'(r_{i+1})}$),

$$
\begin{align*}
\hat{H} &= -\frac{t}{N} \sum_i (\sum_k e^{-ikr_i} a_k^\dagger \sum_{k'} e^{ik'r_{i+1}}a_k + \sum_k e^{-ikr_{i+1}} a_k^\dagger \sum_{k'} e^{ik'r_{i}}a_k) \\
&\begin{aligned}
= -\frac{t}{N} & \sum_i (\sum_k e^{-ikr_i} a_k^\dagger \sum_{k'} e^{ik'(r_{i+1}-r_i)}\cdot e^{ik'(r_i)} a_k \\
&+ \sum_k e^{-ikr_{i+1}} a_k^\dagger \sum_{k'} e^{ik'(r_{i}-r_{i+1})} e^{ik'r_{i+1}} a_k)
\end{aligned}\\
&= -\frac{t}{N} \sum_i (\sum_{kk'} e^{i(k'-k)r_i}  e^{ik'(r_{i+1}-r_i)}  a_k^\dagger a_k + \sum_{kk'} e^{i(k'-k)r_i} e^{ik'(r_{i}-r_{i+1})} a_k^\dagger a_k) \\
&= -\frac{t}{N} (\sum_{kk'} (\sum_i e^{i(k'-k)r_i})  e^{ik'(r_{i+1}-r_i)}  a_k^\dagger a_k + \sum_{kk'} (\sum_i e^{i(k'-k)r_i}) e^{-ik'(r_{i+1}-r_{i})} a_k^\dagger a_k) \\
&= -\frac{t}{N} (\sum_{kk'} N\delta(k,k')  e^{ik'(r_{i+1}-r_i)}  a_k^\dagger a_k + \sum_{kk'} N\delta(k,k') e^{-ik'(r_{i+1}-r_{i})} a_k^\dagger a_k) \\
&= -t (\sum_{k} e^{ik(r_{i+1}-r_i)}  a_k^\dagger a_k + \sum_k e^{-ik(r_{i+1}-r_{i})} a_k^\dagger a_k) \\
&= -t (\sum_{k} e^{ik(r_{i+1}-r_i)} + \sum_k e^{-ik(r_{i+1}-r_{i})}) a_k^\dagger a_k \\
\end{align*}
\tag{4}
$$

For each k point:

$$
\begin{aligned}
\hat{H} &= -t(e^{ik(r_{i+1}-r_i)}+e^{-ik(r_{i+1}-r_{i})})) a_k^\dagger a_k\\
&= -2t\cos(k[r_{i+1}-r_i]) a_k^\dagger a_k
\end{aligned}
\tag{5}
$$

so that the Hamiltonian matrix for 1D atomic chain is a single `1X1` matrix and the dispersion is a simple cos wave:

$$
-2t\cos(k[r_{i+1}-r_i]) = -2t\cos(k\Delta)
\tag{7}
$$

where $\Delta$ is the cell length.

and it looks like:

![test]({{site.baseurl}}/assets/img/post_img/2021-08-08-img1.jpg){:height="320px" width="426px" .center}

Since this is a `1X1` matrix, the basis it self is the eigenvector, we can revert it back to real-space by inverse FT:

$$
a_k(r) = \frac{1}{\sqrt{N}} \sum_j e^{ikr_j} a_j(r)
\tag{8}
$$

### 1D di-atomic chain

The Hamiltionian of this model can be written as:

$$
H = -t \sum_i (a^\dagger_i b_i + b^\dagger_i a_i + b_{i-1}^\dagger a_i + a_i^\dagger b_{i-1})
\tag{9}
$$

__Note__: for di-atomic chain, only 4 hoppings are needed since there are only two bonds inside one unitcell.

Transform this Hamiltonian into reciprocal space:

$$
\begin{aligned}
\hat{H} &= -t \sum_i (a^\dagger_i b_i + b^\dagger_i a_i + b_{i-1}^\dagger a_i + a_i^\dagger b_{i-1})\\
&\begin{aligned}
= -\frac{t}{N} &\sum_i (\sum_k e^{-ikr^a_{i}} a^\dagger_k \sum_{k'} e^{ikr^b_{i}} b_k + \sum_k e^{-ikr^b_{i}} b^\dagger_k \sum_{k'} e^{ikr^a_{i}} a_k \\
&+ \sum_k e^{-ikr^b_{i-1}} b^\dagger_k \sum_{k'} e^{ikr^a_{i}} a_k + \sum_k e^{-ikr^a_{i}} a^\dagger_k \sum_{k'} e^{ikr^b_{i-1}} b_k)
\end{aligned}\\

&\begin{aligned}
= -t (&\sum_k e^{ik(r^b_i - r^a_i)} a^\dagger_k b_k + \sum_k e^{-ik(r^b_i - r^a_i)} b^\dagger_k a_k \\
&+ \sum_k e^{ik(r^a_{i} - r^b_{i-1})} b^\dagger_k a_k + \sum_k e^{-ik(r^a_{i} - r^b_{i-1})} a^\dagger_k b_k)
\end{aligned}\\
&= -t(\sum_k e^{ik(r^a_{i} - r^b_{i-1})}+e^{-ik(r^b_i - r^a_i)})b^\dagger_k a_k -t(\sum_k e^{ik(r^b_i - r^a_i)}+e^{-ik(r^a_{i} - r^b_{i-1})})a^\dagger_k b_k \\
&= \sum_k 2\cos(k\Delta) b^\dagger_k a_k + \sum_k 2\cos(k\Delta) a^\dagger_k b_k
\end{aligned}
\tag{10}
$$

where $\Delta$ is the lattice vector length.
using  $b^\dagger_k a_k$ and  $a^\dagger_k b_k$ as basis, we can write the Hamiltonian in reciprocal space as:

$$
H = \left( \begin{matrix} 0 & -2t\cos(k\Delta) \\ -2t\cos(k\Delta) & 0 \end{matrix} \right)
\tag{11}
$$

Diagonalize this matrix by means like:

$$
|EI - H | = 0
\tag{12}
$$

we get the eigenvalues (aka bands):

$$
\begin{aligned}
E_{1}(k) = + 2t\cos(k\Delta)\\
E_{2}(k) = - 2t\cos(k\Delta)\\
\end{aligned}
\tag{13}
$$

which looks like:

![]({{site.baseurl}}/assets/img/post_img/2021-08-08-img2.jpg){:height="320px" width="426px" .center}

we see that the BZ is now halved, this is actually due to band folding. Still, every bit of information is preserved here, for example, at $\Gamma$ point. the upper band corresponds to the states at the edge of the primitive BZ.

The eigenvectors can be obtained by solving the equations:

$$
(EI-H)A = 0
$$

where $E$ is the dispersion, $I$ is the identity matrix, $A$ is the eigenvectors.

Here the eigenvectors are:

$$
\begin{aligned}
A_1 = \frac{1}{\sqrt{2}}\left( \begin{matrix} 1  \\ 1  \end{matrix} \right)\\
A_2 = \frac{1}{\sqrt{2}}\left( \begin{matrix} 1  \\ -1  \end{matrix} \right) \\
\end{aligned}
\tag{14}
$$

again, we can get the real space representation using inverse FT:

$$
\begin{aligned}
A^1_{k}(r) &= 1 \frac{1}{\sqrt{N}} \sum_j e^{ikr_j} a_j(r) + 1 \frac{1}{\sqrt{N}} \sum_j e^{ikr_j} b_j(r)\\
A^2_{k}(r) &= 1 \frac{1}{\sqrt{N}} \sum_j e^{ikr_j} a_j(r) - 1 \frac{1}{\sqrt{N}} \sum_j e^{ikr_j} b_j(r)
\end{aligned}
\tag{15}
$$

## Flavour 2
In this flavour, we act directly the Bloch wavefunctions on to the Hamiltonian.

### Steps to solve real-space TB hamiltonian

1. write out the expression of the Hamiltonian matrix.
2. change one of the exponential $e^{ikr}$ to $e^{ik(r-r')} \cdot e^{ikr'}$.
3. use the definition of Dirac delta function: $\delta(k,k') = \frac{1}{N} \sum_j e^{i(k-k')r_i}$.
4. do the same thing with all atoms and construct the full Hamiltonian using the elements we got.

For in this method, we don't need a specific real-space Hamiltonian, I'll write it directly:

First, we have the Fourier relation (discrete FT with respect to the lattice, this is basically what anti-Wannierization):

$$
\psi^{\alpha}_{\vec k}(\vec r) = \frac{1}{\sqrt{N}} \sum_{R_{\alpha}} \exp(i \vec k R_{\alpha})\phi^{\alpha}_{R_{\alpha}}(\vec r)
\tag{16}
$$

where $\alpha$ label the orbital inside one unitcell which is labeled by $\vec R_{\alpha}$, assume we have $N$ unitcell to consider (summation goes up to $N$), the $\frac{1}{\sqrt{N}}$ is the normalization factor.

In reverse (we are not going to use this relation in this note but just for the sake of completeness):

$$
\phi^{\alpha}_{R_{\alpha}}(\vec r) = \frac{1}{\sqrt{N}} \sum_{\vec k} \exp(-i \vec k \vec R_{\alpha})\psi^{\alpha}_{\vec k}(\vec r)
\tag{17}
$$

Now, the Hamiltonian elements (in reciprocal space) can be calculated by sandwiching it in between two Bloch functions. i.e.:

$$
H_{\alpha \beta} = \bra{\psi^{\alpha}_{\vec k}(\vec r)} \hat H \ket{\psi^{\beta}_{\vec k}(\vec r)}
\tag{18}
$$

Note that the Hamiltonian ($\hat H$) here is still expressed as:

$$
H = -\frac{1}{2} \nabla^2 + V(r)
\tag{19}
$$

Now, if we plug in Eq. 1 to Eq. 3, we get:

$$
\begin{align}
H_{\alpha,\beta} &= \sum_{\vec k, \vec k'} \bra{\psi^{\alpha}_{\vec k}(\vec r)} \hat H \ket{\psi^{\beta}_{\vec k'}(\vec r)}\\
&=\frac{1}{N}  \sum_{\vec k, \vec k'} \sum_{\vec R_{\alpha}} \exp(-i \vec k \vec R_{\alpha}) \bra{\phi^{\alpha}_{\vec R_{\alpha}}(\vec r)} \hat H \sum_{\vec R_{\beta}} \exp(i \vec k' \vec R_{\beta}) \ket{\phi^{\beta}_{\vec R_{\beta}}(\vec r)} \\
&=\sum_{\vec k, \vec k'}  \sum_{\vec R_{\alpha}} \frac{1}{N}  \exp(i\vec R_{\alpha} (\vec k' - \vec k)) \sum_{\vec R_{\beta}} \exp(i \vec k' (\vec R_{\beta}-\vec R_{\alpha})) \bra{\phi^{\alpha}_{\vec R_{\alpha}}(\vec r)} \hat H \ket{\phi^{\beta}_{\vec R_{\beta}}(\vec r)} \\
&= \sum_{\vec k, \vec k'} \delta(\vec k' - \vec k) \sum_{\vec R_{\beta}} \exp(i \vec k' (\vec R_{\beta}-\vec R_{0})) \bra{\phi^{\alpha}_{\vec R_{0}}(\vec r)} \hat H \ket{\phi^{\beta}_{\vec R_{\beta}}(\vec r)} \\
&=  \sum_{\vec R_{\beta}} \exp(i \vec k (\vec R_{0}- \vec R_{\beta})) \bra{\phi^{\alpha}_{\vec R_{0}}(\vec r)} \hat H \ket{\phi^{\beta}_{\vec R_{\beta}}(\vec r)} \\
&= \sum_{\vec R_{\beta}} \exp(i \vec k (\vec R_{0}- \vec R_{\beta})) \cdot (-t^{\vec R_{0},\vec R_{\beta}}_{\alpha, \beta}) = H_{\alpha, \beta}(\vec k)
\end{align}
\tag{20}
$$

here, we've taken advantage of the fact that we are summing over a huge amount of real-space cells ($\vec R_{\alpha}$ and $\vec R_{\beta}$),

$$
\sum_{\vec R_{\beta}} \exp(i \vec k' (\vec R_{\beta}-\vec R_{\alpha})) \bra{\phi^{\alpha}_{\vec R_{\alpha}}(\vec r)} \hat H \ket{\phi^{\beta}_{\vec R_{\beta}}(\vec r)}
$$

can be replaced with:

$$
\sum_{\vec R_{\beta}} \exp(i \vec k' (\vec R_{\beta}-\vec R_{0})) \bra{\phi^{\alpha}_{\vec R_{0}}(\vec r)} \hat H \bra{\phi^{\beta}_{\vec R_{\beta}}(\vec r)}.
$$

In the last step, since the Hamiltonian is still in real space, we can calculate the integral directly in real space and the resulting energy ($-t^{\vec R_{0},\vec R_{\beta}}_{\alpha, \beta}$) is the so-called hopping energy.

If $\alpha = \beta$ and $\vec R_{0} = \vec R_{\beta}$, then we call this hopping the "On-site" hopping (energy).

Also note that for the "on-site" energy term, since $\alpha = \beta$ and $\vec R_{0} = \vec R_{\beta}$, $H_{\alpha, \beta}$ does not depend on the wave vector $\vec k$.

Now that we have the Hamiltonian elements in reciprocal space, all we need to do to get the band structure is to set a $\vec k$ and diagonalize the Hamiltonian.

## Important take-away
The Hamiltonian in the rec space can be simply constructed using the following relation:

$$
H_{\alpha,\beta} (\vec k) = \sum_{\vec R_{\beta}} \exp(i \vec k (\vec R_{0}- \vec R_{\beta})) \cdot (-t^{\vec R_{0},\vec R_{\beta}}_{\alpha, \beta})
\tag{21}
$$

and all we need is the real-space hopping amplitude which can be easily obtained from `wannier90_hr.dat`.

😉 keep a note of this relation for we'll need it for next post's surface green function calculations!
