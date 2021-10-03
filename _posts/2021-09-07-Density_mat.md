---
layout: post
title: Duodempotency of density matrix
date: 2021-09-07
categories: Post
description: Deriving duodempotency of spin-degenerate density matrices
tags: Tight-binding
---

Density matrix, or density operator, is a very useful tool in quantum mechanics as it incorporates all the essential information of a set of wavefunctions.
In spin-degenerate case, the density matrix has duodempotency which means the $n^{th}$ power of it is equal to multiplying a prefactor of $2^{n-1}$ to it.

Let's first derive the density matrix.

Assuming we have a set of orthonormal eigenstates $\ket{\psi_i}$ of a molecular system.
The probabilities of an electron is in one of these state is $\omega_i$ (usually is in between 0 and 1, but for spin degenerate system, it should be between 0 and 2) so that the expectation value of an operator $\hat{O}$ is:

$$
\braket{\hat{O}} = \sum_i \braket{\psi_i \vert \hat{O} \vert \psi_i}
\tag{1}
$$

note that this is a quantum _and_ statistical average ($\omega$ can be fractional).

If states are singly(in spin-degenerate case, doubly) occupied (i.e. if $\omega_i0$ are integers of $1(2)$ or $0$), we say the system is in a collection of "pure" states and the statistical average disappears.
<!-- In our case, for a system with multiple electrons, ignoring thermal excitations, we have a set of occupied states. -->

The density operator is defined as:

$$
\hat{p} = \sum_i \omega_i \ket{\psi_i} \bra{\psi_i}
\tag{2}
$$

and we expand our eigenstates set $\ket{\psi_i}$ with a set of basis states $\ket{\phi_i}$:

$$
\ket{\psi_i} = \sum_j c_j^{(i)} \ket{\phi_j}.
\tag{3}
$$

Using Eq. 3 and Eq. 2, we can write Eq. 1 as:

$$
\begin{aligned}
\braket{O}&=\sum_{i} w_{i} \sum_{j} c_{j}^{(i)*}\braket{\phi_{j}\vert\hat{O} \sum_{k} c_{k}^{(i)} \vert \phi_{k}} \\
&=\sum_{j} \sum_{k}\left[\sum_{i} c_{j}^{(i)*} w_{i} c_{k}^{(i)}\right]\braket{\phi_{j}\vert\hat{O} \vert \phi_{k}} \\
&=\sum_{j} \sum_{k} \rho_{k j} O_{j k}=\operatorname{Tr}(\rho O)
\end{aligned}.
\tag{4}
$$

In Eq. 4, we can easily use the density matrix to obtain the expectation value of an operator.
Also, when the operator we are calculating is the identity matrix (operator), we get the total number of electrons $N$ in the system.
i.e. $\mathrm{Tr}[\rho]=N$.

The matrix element of the density matrix $\rho$ can be expressed as:

$$
\rho_{k j}=\sum_{i}  w_{i} c_{k}^{(i)}c_{j}^{(i)*}=\braket{\phi_{k}\vert\hat{\rho}\vert \phi_{j}}
\tag{5}
$$

---

To show the duodempotency property, we need to calculate the square of the density matrix:

$$
\left(\rho ^2\right)_{lm} = \sum_k \rho_{lk} \rho_{km}.
\tag{6}
$$

Substituting Eq. 5 to Eq. 6:

$$
\begin{aligned}
\left(\rho ^2\right)_{lm} &= \sum_k \rho_{lk} \rho_{km}\\
&= \sum_k \sum_i c_l^{(i)} \omega_i c_k^{(i)*} \sum_j c_k^{(j)} \omega_j c_m^{(j)*}.
\end{aligned}
$$

Since we only have occupied and unoccupied molecular (eigen) states $\ket{\psi_i}$, we can restrict the summation of $i$ and $j$ to those occupied space. Note that in our case, the occupied states are doubly occupied, i.e. $\omega = 2$:

$$
\begin{aligned}
\left(\rho ^2\right)_{lm} &=  \sum_k \sum_i c_l^{(i)} \omega_i c_k^{(i)*} \sum_j c_k^{(j)} \omega_j c_m^{(j)*}\\
&= 2 \sum_i^{occ} 2 \sum_j^{occ}   c_l^{(i)} c_m^{(j)*} \sum_k \left[ c_k^{(i)} c_k^{(j)*} \right].
\end{aligned}
$$

Remember that the molecular states are orthonormal, they have the following relation:

$$
\sum_k \left[ c_k^{(i)} c_k^{(j)*} \right] =
\begin{cases}
    1,& \text{if } i=j\\
    0,& \text{if } i\neq j
\end{cases}
\tag{7}
$$

with relation, the square of the density matrix reads:

$$
\begin{aligned}
\left(\rho ^2\right)_{lm} &= 2 \sum_i^{occ} 2 \sum_j^{occ}   c_l^{(i)} c_m^{(j)*} \sum_k \left[ c_k^{(i)} c_k^{(j)*} \right] \\
&= 2 \sum_i^{occ} 2 c_l^{(i)} c_m^{(i)*} \\
&= 2 \sum_i \omega_i c_l^{(i)} c_m^{(i)*} = 2 \rho_{lm}
\end{aligned}
\tag{8}
$$

Naturally, for the $n^{th}$ power, we have:

$$
\left(\rho ^n\right)_{lm} = 2^{n-1} \rho_{lm}
\tag{9}
$$

and:

$$

\mathrm{Tr}[\left(\rho ^n\right)_{lm}] = 2^{n-1} \mathrm{Tr}[\rho_{lm}] = 2^{n-1} N
$$

Where $N$ is the number of electrons in the system.

Eq. 9 demonstrated that for spin-degenerated systems, the density matrix has _duodempotency_, and this property is directly related to the fact that for a Fermion system, we have two electrons occupying one state (like those from restricted Hartree-Fock calculations).
If we can only have one electron occupying one state, then we would have _idempotency_ like we learned in our undergraduate quantum mechanics class and if we can have $x$ electrons occupying one states we would have:

$$
\left(\rho ^n\right)_{lm} = x^{n-1} \rho_{lm}
$$

Note that if we need to consider spin, things will look kind of different.
