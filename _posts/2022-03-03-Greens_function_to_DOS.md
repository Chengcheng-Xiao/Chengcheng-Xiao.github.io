---
layout: post
title: From Greens function to DOS
date: 2022-03-03
categories: Post
description: Using Greens function to express DOS
tags: Math DFT
---

Remembering that in [:link: this post](../../../2021/08/16/Greens_function_2.html) we have derived that the greens function for non-interacting time-independent is (expressed in eigenvalue basis):


$$
G(E) = i \sum_n \frac{\ket{n} \bra{n}}{(E-E_n+i\eta)}
$$

For historical reason (I'm not actually sure why but that's what everytext book says...), we ditch the imaginary sign:

$$
G(E) = \sum_n \frac{\ket{n} \bra{n}}{(E-E_n+i\eta)}.
$$

Now, if we sandwich it in between two eigenvectors (of the Hamiltonian) and take the sum over these eigenvectors, we get:

$$
\begin{aligned}
\sum_j<j|G(E)|j> &= \sum_j \sum_n \frac{\braket{j \vert n} \braket{n \vert j}}{(E-E_n+i\eta)}\\
&=\sum_j \frac{1}{(E-E_j+i\eta)}
\end{aligned}
$$

This can also be written as the trace of the matrix representation of $G$:

$$
\mathrm{Tr}[G( E)_{kl}] = \sum_j \frac{1}{(E-E_j+i\eta)} \tag{1}
$$

<!-- Replacing $E-E_j$ with $\omega_j$, we get:

$$
\mathrm{Tr}[G(E)_{kl}] = \sum_j \frac{1}{(\omega_j+i\eta)} \tag{2}
$$ -->

According to [:link: the Sokhotski-Plemelj formula](../01/Sokhotski_Plemelj_Formula.html):

$$
\mathrm{Tr}[G( E)_{kl}] = \sum_j \frac{1}{(E-E_j+i\eta)} = \sum_j \left [ \mathcal{P} \frac{1}{E-E_j} - i \pi \delta(E-E_j) \right ] \tag{3}
$$


Remembering that the definition of the density of state (DOS) is :

$$
\rho(E) = \sum_j \delta(E-E_j) \tag{4}
$$

and since we have $\delta(E-E_j)$ as the imaginary part of the Eq. 3, we can express it as:

$$
\mathrm{Im} \mathrm{Tr}[G(E)_{kl}] = -\pi \sum_j \delta(E-E_j) = - \pi \rho(E) \tag{5}
$$

$\eta$ acts as an smearing factor (because it is a manually added finite life time to the time evolution propagator of states. See Eq. 10 in [:link: this post](../../../2021/08/16/Greens_function_2.html)) of the DOS since Eq. 3 only works when $\eta \rightarrow 0^+$.
