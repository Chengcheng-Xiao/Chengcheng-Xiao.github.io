---
layout: post
title: Multicentered bond order index
date: 2021-09-08
categories: Post
description: Deriving renormalized multicentered bond order index.
tags: Tight-binding
---

From my [previous post]({% post_url 2021-09-07-Density_mat %}), I've demonstrated that the density matrix of a spin-degenerate system (i.e. restricted Hartree-Fock ones), we have duodempotency:

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
\mathrm{Tr}[P^2] = 2 \mathrm{Tr}[P] = \sum_{\lambda} \sum_{\sigma} P_{\lambda \sigma} P_{\sigma \lambda} = 2N
\tag{2}
$$

where $N$ is the number of electron in the system.

We can re-write Eq. 2 by assigning the orbitals to atoms:

$$
\begin{aligned}
2N &= \sum_{\lambda \in A}^\text{all orbitals} \sum_{\sigma \in B}^\text{all orbitals} P_{\lambda \sigma} P_{\sigma \lambda}\\
&= \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} \left[ \sum_{\lambda \in A} \sum_{\sigma \in B} P_{\lambda \sigma} P_{\sigma \lambda} \right]\\
&= \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}}  \text{BI}_{AB}.
\end{aligned}
\tag{3}
$$

In Eq. 3, we have defined the Bonding Index ($\mathrm{BI}$) as:

$$
\text{BI}_{AB} = \sum_{\lambda \in A} \sum_{\sigma \in B} P_{\lambda \sigma} P_{\sigma \lambda}
\tag{4}
$$

This definition is actually the so-called Wiberg bond index when $A\neq B$ (See the original paper [:link: 10.1016/0040-4020(68)88057-3](https://www.sciencedirect.com/science/article/pii/0040402068880573) and [:link: simple explanations](https://mattermodeling.stackexchange.com/a/1469/1804)).

For reasons that will become clear, let's move the prefix $2$ on the left-hand-side of Eq. 3 to the right-hand-side:

$$
N = 2^{-1} \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}}  \text{BI}_{AB} = \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} 2^{-1} \text{BI}_{AB}
\tag{5}
$$

Now, since the BI matrix in this case is a 2D matrix, we can partition it into two categories: the diagonal part and non-diagonal part:

- The diagonal part: One-center contribution (e.g. on atom A).

$$
2^{-1} \mathrm{BI}_{AA}
$$

- The off diagonal part: Two-center contribution (e.g. between atom A and B).

$$
2^{-1} (\mathrm{BI}_{AB} + \mathrm{BI}_{BA})
$$

---

Remember before we assumed $n=2$ and then arrived at Eq. 1 and 2?
Now, let's assume $n=3$, we have:

$$
\mathrm{Tr}[P^3] = 2^2 \mathrm{Tr}[P] = \sum_{\lambda} \sum_{\sigma} \sum_{l} P_{\lambda \sigma} P_{\sigma l} P_{l \lambda} = 2^2N
\tag{6}
$$

and again, we re-write this by assigning orbital to atoms and move the prefix $2^2$ around:

$$
\begin{aligned}
N &= 2^{-2} \sum_{\lambda}^\text{all orbitals} \sum_{\sigma}^\text{all orbitals} \sum_{l}^\text{all orbitals} P_{\lambda \sigma} P_{\sigma l} P_{l \lambda}\\
&= 2^{-2} \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} \sum_C^{\text{all atoms}}  \left[\sum_{\lambda \in A} \sum_{\sigma \in B} \sum_{l \in C} P_{\lambda \sigma} P_{\sigma l} P_{l \lambda}\right]\\
&= 2^{-2} \sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} \sum_C^{\text{all atoms}}  \text{BI}_{ABC}\\
&=\sum_A^{\text{all atoms}} \sum_B^{\text{all atoms}} \sum_C^{\text{all atoms}}  2^{-2} \text{BI}_{ABC}\\
\end{aligned}
$$

This time, the BI is three dimensional, which means we have more ways to partition it (hence the number of electrons):

- The diagonal part: one-center contribution (e.g. on atom A).

$$
2^{-2} \mathrm{BI}_{AAA}
$$

- The off-diagonal part 1: two-center contribution (e.g. between atom A and B).

$$
2^{-2} (\mathrm{BI}_{AAB}+\mathrm{BI}_{ABA}+\mathrm{BI}_{BAA})
$$

- The off-diagonal part 2: three-center contribution (e.g. between atom A, B and C).

$$
2^{-2} (\mathrm{BI}_{ABC} + \mathrm{BI}_{ACB} + \mathrm{BI}_{CBA} + \mathrm{BI}_{BCA} + \mathrm{BI}_{CAB})
$$

---

Okay, we can now clearly see that, to describe a n-center bonding, we need to dot n times the density matrix with itself so that Eq. 2 looks like:

$$
\mathrm{Tr}[P^n] = 2^{n-1} \mathrm{Tr}[P] = \sum_{\lambda\sigma...\gamma}  P_{\lambda\sigma} P_{\sigma \alpha} ... P_{\gamma\lambda} = 2^{n-1}N
$$

and the resulting BI matrix:

$$
\text{BI}_{ABC...K} = \sum_{\lambda \in A} \sum_{\sigma \in B} ... \sum_{\gamma \in k} P_{\lambda\sigma} P_{\sigma \alpha} ... P_{\gamma\lambda},
$$

is n-dimensional (there are n indexes for $\text{BI}_{ABC...K}$).

Also, due to duodempotency, everytime we dot another density matrix, we need another prefactor of $2^{-1}$ to normalize our BI so that it represent the number of electrons in the multicentered bonding state.

Mathematically, we can write the number of electrons that belongs to k-centered bonding between atom A, B, ... K as:

$$
N_{ABC...K} = A_k^k \cdot 2^{-(k-1)} \mathrm{BI}_{ABC...K}
$$

Where $A_n^m = \frac{n!}{(n-m)!}$ and $A_k^k = k!$ gives the permuations of our k atoms.
Note that when using orthogonal basis set, the bond index matrix remain invariant under any permutations.
However, under non-orthogonal basis, they only remain invariant under cyclic permutations.

<!-- If we have multiple occurrence of the same atom in the $N_{AAABCD...K}$, we have $A_k^k/how many occurrences$.
For example, $N_{AAABCD} = 6!/3 * BI_{AAABCD}$. -->
