---
layout: post
title: From Green's function to Dyson equation
date: 2022-03-04
categories: Post
description: From Green's function to Dyson equation
tags: Math DFT
---

In its time-dependent form, the Schrodinger's equation reads:

$$
\hat H \Psi(\vec r) = E \Psi(\vec r)
\tag{1},
$$

where the Hamiltonian operator $\hat H$ is $-\frac{\hbar^2}{2m} \nabla^2 + V(\vec r)$.

Let's first consider the free particle situation where $V=0$, we write the solution as $\Psi_0(\vec r)$:

$$
\left[-\frac{\hbar^2}{2m} \nabla^2 \right] \Psi_0(\vec r) = E \Psi_0(\vec r). \tag{3}
$$

After some rearranging, we get:

$$
\begin{aligned}
\left[ E + \frac{\hbar^2}{2m} \nabla^2\right] \Psi_0 (\vec r) =\left[ E - \hat H_0 (\vec r) \right] \Psi_0 (\vec r) =  0 \tag{4}
\end{aligned}
$$

and here, the differential equation is homogeneous. The Green's function for the operator $\left[ E - \hat H_0 (\vec r) \right]$ can be written as:

$$
\left[ E - \hat H_0 (\vec r) \right] g(\vec r, \vec r' ) =  \delta(r-r') \tag{5}
$$

Now, let's add back the potential term (time-independent) as perturbation, we write the solution to this Schrodinger equation as $\Psi(\vec r)$:

$$
\begin{aligned}
[\hat H_0+V(\vec r)]\Psi(\vec r) &= E \Psi(\vec r)\\
\left[ E - \hat H_0 (\vec r) \right] \Psi (\vec r) &= V(\vec r) \Psi(\vec r).
\end{aligned} \tag{6}
$$

Here, we are treating $V(\vec r) \Psi(\vec r)$ as the source of the "inhomogeneous" and because $V$ is treated as perturbation, we have kept the energy constant as $E$.
Since we alreay know the Green's function of the unperturbed operator $E - \hat H_0 (\vec r)$, we can express the solution to this equation as:

$$
\Psi (\vec r) = \Psi_0 (\vec r) + \int d \vec r' g(\vec r, \vec r' ) V(\vec r') \Psi(\vec r'). \tag{7}
$$

At this point, we have two ways to get the Dyson equation.

---

### Using operator

Alternatively, we can still express $\Psi (\vec r, t)$ more directly from the Green's function of the perturbed system with $G(\vec r, \vec r')$:

$$
(E-\hat H) G(\vec r, \vec r' ) = \delta(\vec r - \vec r')  \tag{8}
$$

with $\hat H = \hat H_0 + V$.

Using Eq. 5, we can write Eq. 8 as:

$$
\begin{aligned}
G\left(\vec r, \vec r^{\prime}\right) &=[E-\hat H]^{-1} \delta\left(\vec r-\vec r^{\prime}\right) \\
&=[E-\hat H]^{-1}\left[ E-\hat H_{0}(\vec r) \right] g\left(\vec r, \vec r^{\prime} \right) \\
&=[E-\hat H]^{-1} [E-\hat H+V(\vec r)] g\left(\vec r, \vec r^{\prime} \right) \\
&=g\left(\vec r, \vec r^{\prime} \right)+ [ E-\hat H ]^{-1} V(\vec r) g\left(\vec r, \vec r^{\prime} \right) \tag{9}
\end{aligned}
$$

and according to the [inverse operator notation](#inverse-operator-notation):

$$
\ldots(\lambda-\hat{L})^{-1}=\int \ldots G\left(x, x^{\prime}\right) d x^{\prime} \tag{10}
$$

we can express Eq. 9 as:

$$
G\left(\vec r, \vec r^{\prime} \right)=g\left(\vec r, \vec r^{\prime} \right)+\int  G\left(\vec r, \vec r_{1}\right) V\left(\vec r_{1}\right) g\left(\vec r_{1}, \vec r^{\prime}\right) d \vec r_{1}.  \tag{11}
$$

If we drop the integration symbols:

$$
G = g + gVG
$$

This result is called the Dyson equation, and it allows us to express the Green's function of the perturbed system in term of the unperturbed one.

### Using wavefunctions

Similarly, we can find $\Psi(\vec r)$ from $G\left(\vec r, \vec r^{\prime} \right)$, to do this, we re-express the un-perturbed equation as:

$$
\begin{aligned}
E\Psi_0(\vec r) - \hat H_0 \Psi_0(\vec r) &= 0\\
E\Psi_0(\vec r) - (\hat H_0 + V) \Psi_0(\vec r) &= -V \Psi_0(\vec r)\\
(E - \hat H )\Psi_0(\vec r) &= -V \Psi_0(\vec r)\\ \tag{12}
\end{aligned}
$$

Using Eq. 8 and noting that V is treated as perturbation so that we can keep $E$, we get:

$$
\Psi_0(\vec r) =\Psi(\vec r) - \int G(\vec r, \vec r') V(\vec r') \Psi_0(\vec r') d \vec r' \tag{13}
$$

Note that the homogeneous solution to operator $(E - \hat H )$ in Eq. 12 is just $\Psi(\vec r)$.
Rearranging Eq. 13, we get:

$$
\Psi(\vec r) =\Psi_0(\vec r) + \int G(\vec r, \vec r') V(\vec r') \Psi_0(\vec r') d \vec r' \tag{13}
$$


Remembering Eq. 7, dropping the integration, with Eq. 13, we can re-write it as:

$$
\begin{aligned}
\Psi &= \Psi_0 + gV\Psi\\
&= \Psi_0 + gV (\Psi_0 + gV \Psi)\\
&= \Psi_0 + gV\Psi_0 + gVgV(\Psi_0 + gV \Psi)\\
&= \Psi_0 + (g + gVg + gVgVg+ \cdots)V\Psi_0\\
\end{aligned} \tag{14}
$$

Comparing Eq. 13 with Eq. 13, we see that:

$$
G = g + gVG
$$

or symbolically:

$$
G^{-1} = g^{-1} -V.
$$

Which, again, gives us the so-called Dyson equation.

---


## Inverse operator notation

Because:

$$
\begin{aligned}
(\lambda - \hat L) G(x,x') &= \delta (x,x')\\
\int (\lambda - \hat L) G(x,x') f(x') dx' &= \int \delta (x,x') f(x') dx'\\
(\lambda - \hat L) \int  G(x,x') f(x') dx' &= f(x)\\
\int  G(x,x') f(x') dx' &= (\lambda - \hat L)^{-1} f(x)\\
\end{aligned} \tag{A.1}
$$

we can infer:

$$
\ldots(\lambda-\hat{L})^{-1}=\int \ldots G\left(x, x^{\prime}\right) d x^{\prime} \tag{A.2}
$$

Where $\ldots$ can be any operator or functions.

---
Reference: [Green's functions in quantum mechanics courses](https://arxiv.org/abs/2107.14104)

Reference: [An introduction to Green’s function in many-body condensed-matter quantum systems](https://neel.cnrs.fr/wp-content/uploads/2020/12/GF1_Blase_Aussois.pdf)
