---
layout: post
title: Multicentered bond order index
date: 2021-09-08
categories: Post
description: Deriving renormalized multicentered bond order index.
tags: Tight-binding
---

In my [:link: previous post]({% post_url 2021-09-07-Density_mat %}), I've demonstrated that the density matrix of a spin-degenerate system (i.e. restricted Hartree-Fock ones) have duodempotency:

$$
\left(\rho ^n\right)_{lm} = 2^{n-1} \rho_{lm}.
$$

Assuming $n=2$, we have:

$$
\left(\rho ^2\right)_{lm} = 2 \cdot \rho_{lm} = \sum_{\sigma} \rho_{l\sigma} \rho_{\sigma m}
\tag{1}
$$

and,

$$
\mathrm{Tr}[\rho^2] = 2 \mathrm{Tr}[\rho] = \sum_{\lambda} \sum_{\sigma} \rho_{\lambda \sigma} \rho_{\sigma \lambda} = 2N
\tag{2}
$$

where $N$ is the number of electron in the system.

We can re-write Eq. 2 by assigning the orbitals to atoms:

$$
\begin{aligned}
2N &= \sum_{\lambda}^\text{all orbitals} \sum_{\sigma}^\text{all orbitals} \rho_{\lambda \sigma} \rho_{\sigma \lambda}\\
&= \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} \left[ \sum_{\lambda \in A} \sum_{\sigma \in B} \rho_{\lambda \sigma} \rho_{\sigma \lambda} \right]\\
&= \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}}  \text{BI}_{AB}.
\end{aligned}
\tag{3}
$$

In Eq. 3, we define the Bonding Index ($\mathrm{BI}$) as:

$$
\text{BI}_{AB} = \sum_{\lambda \in A} \sum_{\sigma \in B} \rho_{\lambda \sigma} \rho_{\sigma \lambda}
\tag{4}
$$

This, is actually the so-called Wiberg bond index when $A\neq B$ (See the original paper [:link: 10.1016/0040-4020(68)88057-3](https://www.sciencedirect.com/science/article/pii/0040402068880573) and [:link: simple explanations](https://mattermodeling.stackexchange.com/a/1469/1804)).

For reasons that will become clear, let's move the prefix $2$ on the left-hand-side of Eq. 3 to the right-hand-side:

$$
N = 2^{-1} \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}}  \text{BI}_{AB} = \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} 2^{-1} \text{BI}_{AB}
\tag{5}
$$

Now, since the BI matrix in this case is a 2D matrix, we can partition it into two categories: the diagonal part and non-diagonal part:

- The diagonal part: One-center contribution (e.g. electrons shared on atom A).

$$
N_{A} = 2^{-1} \mathrm{BI}_{AA}
$$

- The off diagonal part: Two-center contribution (e.g. electrons shared between atom A and B).

$$
N_{AB} = 2^{-1} (\mathrm{BI}_{AB} + \mathrm{BI}_{BA})
$$

---

Remember before we assumed $n=2$ and then arrived at Eq. 1 and E1. 2?
Now, assuming $n=3$, we have:

$$
2^2N = \mathrm{Tr}[\rho^3] = 2^2 \mathrm{Tr}[\rho] = \sum_{\lambda} \sum_{\sigma} \sum_{l} \rho_{\lambda \sigma} \rho_{\sigma l} \rho_{l \lambda}
\tag{6}
$$

and again, we re-write this by assigning orbitals to atoms and move the prefix $2^2$ to the right hand side:

$$
\begin{aligned}
N &= 2^{-2} \sum_{\lambda}^\text{all orbitals} \sum_{\sigma}^\text{all orbitals} \sum_{l}^\text{all orbitals} \rho_{\lambda \sigma} \rho_{\sigma l} \rho_{l \lambda}\\
&= 2^{-2} \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} \sum_C^{\text{all atoms}}  \left[\sum_{\lambda \in A} \sum_{\sigma \in B} \sum_{l \in C} \rho_{\lambda \sigma} \rho_{\sigma l} \rho_{l \lambda}\right]\\
&= 2^{-2} \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} \sum_C^{\text{all atoms}}  \text{BI}_{ABC}\\
&=\sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} \sum_C^{\text{all atoms}}  2^{-2} \text{BI}_{ABC}\\
\end{aligned}
\tag{7}
$$

This time, the BI matrix is three dimensional (we have three indices), which means we have more ways to partition it (hence the number of electrons):

- The diagonal part: one-center contribution (e.g. electons on atom A).

$$
N_{A} = 2^{-2} \mathrm{BI}_{AAA}
$$

- The off-diagonal part 1: two-center contribution (e.g. electons shared between atom A and B).

$$
N_{AB} = 2^{-2} (\mathrm{BI}_{AAB}+\mathrm{BI}_{ABA}+\mathrm{BI}_{BAA})
$$

- The off-diagonal part 2: three-center contribution (e.g. electrons shared between atom A, B and C).

$$
N_{ABC} = 2^{-2} (\mathrm{BI}_{ABC} + \mathrm{BI}_{ACB} + \mathrm{BI}_{CBA} + \mathrm{BI}_{BCA} + \mathrm{BI}_{CAB})
$$

---

Okay, we can now clearly see that, to describe a n-center bonding, we need to dot n times the density matrix with itself.
By doing so Eq. 2 looks like:

$$
\mathrm{Tr}[\rho^n] = 2^{n-1} \mathrm{Tr}[\rho] = \sum_{\lambda\sigma...\gamma}  \rho_{\lambda\sigma} \rho_{\sigma \alpha} ... \rho_{\gamma\lambda} = 2^{n-1}N
\tag{8}
$$

and the resulting BI matrix:

$$
\text{BI}_{ABC...K} = \sum_{\lambda \in A} \sum_{\sigma \in B} ... \sum_{\gamma \in k} \rho_{\lambda\sigma} \rho_{\sigma \alpha} ... \rho_{\gamma\lambda},
\tag{9}
$$

is n-dimensional (there are n indices for $\text{BI}_{ABC...K}$).

Also, due to duodempotency, every time we dot another density matrix, we need another prefactor of $2^{-1}$ to normalize our BI so that it represent the number of electrons in the system that are partitioned to the multicentered bonding state.

Mathematically, we can write our renormalized BI which gives the number of electrons that belongs to k-centered bonding between atom A, B, ... K as:

$$
N_{ABC...K} = A_k^k \cdot 2^{-(k-1)} \mathrm{BI}_{ABC...K}
\tag{10}
$$

Where $A_n^m = \frac{n!}{(n-m)!}$ and $A_k^k = k!$ gives the permuations of our k atoms, we need this prefactor becasue the bond index matrix remains invariant under any permutations (when using orthogonal basis set).
However, under non-orthogonal basis, they only remain invariant under cyclic permutations and we need to some more work.

Now this looks fin and dandy but use be warned: this derivation only works with spin-degenerate cases. i.e. restricted Hartree-Fork generated density matrix. For spin-polarized cases, see [:link: 10.1016/S0166-1280(99)00339-5](https://www.sciencedirect.com/science/article/pii/S0166128099003395?via%3Dihub).
<!-- If we have multiple occurrence of the same atom in the $N_{AAABCD...K}$, we have $A_k^k/how many occurrences$.
For example, $N_{AAABCD} = 6!/3 * BI_{AAABCD}$. -->
