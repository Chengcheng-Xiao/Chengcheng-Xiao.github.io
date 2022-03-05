---
layout: post
title: Green's function to Dyson equation
date: 2022-03-04
categories: Post
description: From Green's function to Dyson equation
tags: Math DFT
---

In its time-dependent form, the Schrodinger's equation reads:

$$
i\hbar \frac{\partial}{\partial t} \Psi (\vec r, t) = \hat H \Psi(\vec r, t)
\tag{1},
$$

where the Hamiltonian operator $\hat H$ is $-\frac{\hbar^2}{2m} \nabla^2 + V(\vec r, t)$.

Write the Schordinger's equation in full:

$$
i\hbar \frac{\partial}{\partial t} \Psi (\vec r, t) = \left[-\frac{\hbar^2}{2m} \nabla^2 + V(\vec r, t)\right] \Psi(\vec r, t)
\tag{2}.
$$

Let's first consider the free particle situation where $V=0$ and we know the total energy in this case is conserved:

$$
i\hbar \frac{\partial}{\partial t} \Psi (\vec r, t) = \left[-\frac{\hbar^2}{2m} \nabla^2 \right] \Psi(\vec r, t) = E \Psi(\vec r, t).
$$

After some rearranging, we get:

$$
\begin{aligned}
\left[ E - i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2\right] \Psi (\vec r, t) &=  0 \\
\left[ E - \hat H_0 (\vec r,t) \right] \Psi (\vec r, t) &=  0
\end{aligned}
$$

and here, the differential equation is homogeneous, but, we can still define the associated Green's function as:

$$
\left[ E - \hat H_0 (\vec r,t) \right] g(\vec r, \vec r'; t, t') =  \delta(r-r') \delta(t-t')
$$

Now, let's add in the potential term (time-independent) as perturbation, we recover the original Schordinger equation:

$$
\begin{aligned}
[\hat H_0+V(\vec r))\Psi(\vec r, t] &= E \Psi(\vec r, t)\\
\left[ i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2 - V(\vec r, t) \right] \Psi (\vec r, t) &= E \Psi(\vec r, t)\\
\left[ E - i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2 \right] \Psi (\vec r, t) &= V(\vec r, t) \Psi(\vec r, t)\\
\left[ E - \hat H_0 (\vec r, t) \right] \Psi (\vec r, t) &= V(\vec r, t) \Psi(\vec r, t)\\
\end{aligned}
$$

Here, we are treating $V(\vec r, t) \Psi(\vec r, t)$ as the source of the "inhomogeneous".
Since we alreay know the Green's function of the unperturbed operator $E - \hat H_0 (\vec r, t)$, we can express the solution to this equation as:

$$
\Psi (\vec r, t) = \Psi_0 (\vec r, t) + \int d \vec r' g(\vec r, \vec r'; t, t') V(\vec r', t') \Psi(\vec r', t'),
$$

where $\Psi_0 (\vec r, t)$ is the solution to the homogeneous equation.

However, it is possible to express $\Psi (\vec r, t)$ more directly from the Green's function of the perturbed system.
To define $G(\vec r, \vec r'; t,t')$:

$$
(E-\hat H) G(\vec r, \vec r'; t, t') = \delta(\vec r - \vec r') \delta(t-t')
$$

with $\hat H = \hat H_0 + V$. Using Eq. XX, we can write Eq. XX as:

$$
\begin{aligned}
G\left(\vec r, \vec r^{\prime}; t, t'\right) &=[E-\hat H]^{-1} \delta\left(\vec r-\vec r^{\prime}\right) \delta (t-t') \\
&=[E-\hat H]^{-1}\left[ E-\hat H_{0}(\vec r) \right] g\left(\vec r, \vec r^{\prime}; t, t'\right) \\
&=[E-\hat H]^{-1} [E-\hat H+V(\vec r)] g\left(\vec r, \vec r^{\prime}; t, t'\right) \\
&=g\left(\vec r, \vec r^{\prime}; t, t'\right)+ [ E-\hat H ]^{-1} V(\vec r) g\left(\vec r, \vec r^{\prime}; t, t'\right)
\end{aligned}
$$

and according to the inverse operator notation:

$$
\ldots(\lambda-\hat{L})^{-1}=\int \ldots G\left(x, x^{\prime}\right) d x^{\prime}
$$

we can express Eq. XX as:

$$
G\left(\vec r, \vec r^{\prime}; t, t'\right)=g\left(\vec r, \vec r^{\prime}; t, t'\right)+\int \int  G\left(\vec r, \vec r_{1}; t, t_1\right) V\left(\vec r_{1}; t_1\right) g\left(\vec r_{1}, \vec r^{\prime}; t_1, t'\right) d \vec r_{1} dt_1
$$

This result is called the Dyson equation, and it allows us to express the Green's function of the perturbed system in term of the unperturbed one.

## inverse operator notation

Because:

$$
\begin{aligned}
(\lambda - \hat L) G(x,x') &= \delta (x,x')\\
\int (\lambda - \hat L) G(x,x') f(x') dx' &= \int \delta (x,x') f(x') dx'\\
(\lambda - \hat L) \int  G(x,x') f(x') dx' &= f(x)\\
\int  G(x,x') f(x') dx' &= (\lambda - \hat L)^{-1} f(x)\\
\end{aligned}
$$

we can infer:

$$
\ldots(\lambda-\hat{L})^{-1}=\int \ldots G\left(x, x^{\prime}\right) d x^{\prime}
$$

Where $\ldots$ can be any operator or functions.

---
Reference: [Green's functions in quantum mechanics courses](https://arxiv.org/abs/2107.14104)
