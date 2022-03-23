---
layout: post
title: The evolution of bond index
date: 2022-03-20
categories: Post
description: Bond index(BI) is a measurement of the "average number of electron pairs shared between atoms". It provides an intuitive description of the covalency between atoms. This post provides a birds-eye-view of the development of the bond index formalism.
tags: DFT
---
## Review: Density matrix
Before we get into things, we (at least I) needs to review the mathematical formulation of the Density matrix object. The generic matrix elements of the density matrix can be expressed as:

$$
\rho_{kl} = \sum_i^\text{occupied} n_i c_k^{(i)} c_l^{(i)*} \tag{1}
$$

where $n_i$ is the occupation number of that molecular orbital. $c_k^i$ and $c_l^i$ are the coefficient of the atomic orbitals $\phi_k$ and $\phi_l$ that made up the molecular orbital $i$. i.e.

$$
\psi_i = \sum_j c_j^i \phi_j \tag{2}
$$


The charge density can be expressed by the density matrix $\hat \rho$ as:

$$
\rho(\vec r) = \sum_k \sum_l \rho_{kl} \phi^*_k(\vec r) \phi_l(\vec r) \tag{3}
$$

Assuming the basis set to be orthogonal (again, like in Hückle theory), the charge number can be expressed as:

$$
\begin{aligned}
N &= \sum_k \sum_l \rho_{kl} \braket{\phi_l \vert \phi_k}\\
&= \sum_k \sum_l \rho_{kl} \int \phi_k^*(\vec r) \phi_l(\vec r) d\vec r\\
&=\text{Tr}(\hat \rho) \tag{4}
\end{aligned}
$$

Or in more general situation, we can use the overlap matrix $\hat S$:

$$
\begin{aligned}
N &= \sum_k \sum_l \rho_{kl} \braket{\phi_k \vert \phi_l}\\
&= \sum_k \sum_l \rho_{kl} S_{kl}\\
&=\text{Tr}(\hat \rho \hat S) \tag{5}
\end{aligned}
$$

## Bond index

Bond index(BI) is a measurement of the "__average number of electron pairs shared between atoms__". For example, if the index of two atoms is $1$ then there is one pair of electrons shared between these two atoms, hence, one bond.

### Coulson bond index

The simplest version to calculate the BI is probably the one proposed by Coulson for $\pi$-orbitals at the Hückle level. By definition, the bond index between atoms $A$ and $B$ is given by:

$$
\text{BI}_{AB}^\text{Coulson} = \sum_{k\in A} \sum_{l\in B} \sum_i^\text{occupied} n_i c_k^{(i)} c_l^{(i)*} \tag{6}
$$

The definition in Eq. 6 is actually a selection of off-diagonal elements of the density matrix $\hat \rho$ (see Eq. 1) where the index of $k$ and $l$ is constrained to the orbitals that belong to atom $A$ and $B$ respectively:

$$
\text{BI}_{AB}^\text{Coulson} = \sum_{k\in A} \sum_{l\in B} \rho_{kl} \tag{7}
$$

The draw back of this bond index is that it can only be used to measure the bond index of $\pi$ bonds. To illustrate this, we consider the following two atoms situation where on each atoms there are only one $p_x$ orbitals with $x$ axis being the bond direction (hence only $\sigma$ bonds can form):

![]()

This simple system has two molecular orbital, one bonding and one anti-bonding:

$$
\begin{aligned}
\psi_\text{bonding} &= \frac{1}{\sqrt{2}} (\phi_1 - \phi_2)\\
\psi_\text{anti-bonding} &= \frac{1}{\sqrt{2}} (\phi_1 + \phi_2)\\
\end{aligned}
$$

and if only the bonding orbital $\psi_\text{bonding}$ is occupied, then, the Coulson's bond index would be:

$$
\begin{aligned}
\text{BI}_{AB}^\text{Coulson} &= \sum_i^\text{occupied} n_i c_1^{(i)} c_2^{(i)*} \\
&= 2 \cdot \frac{1}{\sqrt{2}} \cdot \left( - \frac{1}{\sqrt{2}} \right)\\
&= -1 \tag{8}
\end{aligned}
$$

Which, sadly, gives a negative number... To rectify this, we immediately think of squaring this number. The first person to think of doing it is K.B. Wiberg.

### Wiberg bond index
The Wiberg bond index as defined in [:link: the original paper](https://doi.org/10.1016/0040-4020(68)88057-3) uses the _square_ of the selected off-diagonal elements of the density matrix:

$$
\begin{aligned}
\text{BI}_{AB}^\text{Wiberg} &= \sum_{k\in A} \sum_{l\in B} |\rho_{kl}|^2 \\
&= \sum_{k\in A} \sum_{l\in B} \left ( \sum_i^\text{occupied} n_i c_k^{(i)} c_l^{(i)*} \right ) \cdot \left ( \sum_j^\text{occupied} n_j c_k^{(j)} c_l^{(j)*} \right ) \\
\end{aligned} \tag{9}
$$

Which, is intrinsically positively defined for all types of bonds between atoms in a molecule. Wiberg bond index has a value close to our chemical intuition. E.g. for an Ethyne molecule (C2H2), we would expect to get a number close to $3$ for the two carbon atoms.

Now, this definition is good for all close-shell (all molecular orbitals are doubly occupied) molecules and the basis set is orthonormal.But that isn't always the case, as a matter of fact, most ab-initio programs use non-orthogonal basis set and can calculate spin polarized systems. To solve this, in 1983 I. Mayer proposed an alternative formulation of the Wiberg's bond index that utilizes the overlap matrix between basis orbitals.

### Mayer bond index

The Mayer bond index, as defined in the [:link: original paper](https://doi.org/10.1016/0009-2614(83)80005-0), is:

$$
\text{BI}_{AB}^\text{Mayer} = \sum_{k\in A} \sum_{l\in B} |\rho_{kl} S_{kl}|^2
$$

and for the open-shell molecules, according to the [:link: original paper](https://doi.org/10.1002/qua.560260111) the matrix elements $\rho_{kl}$ is given as the sum:

$$
\sum_i n_i c_k^{(i,\alpha)}c_k^{(i,\alpha)*}+\sum_i n_i c_k^{(i,\beta)}c_k^{(i,\beta)*}
$$

where $\alpha$ and $\beta$ stands for different spin channel.

### Multicentered bond index

The multicentered bond index is a generalization of the Mayer (or Wiberg's) bond index. For details, check out [:link: this post](../../../2021/09/08/Bond_order.html)
