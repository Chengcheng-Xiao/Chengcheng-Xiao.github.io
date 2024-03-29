---
layout: post
title: Green's function (part II)
date: 2021-08-16
categories: Post
description: Quantum version of Green's function, explained.
tags: Math DFT
---
Like I have said in [:link: my post](../15/Greens_function_1) about the classical Green's function:

> Green's function method is a way to decompose a complex inhomogenous source using Dirac delta functions and then combine individually solutions to obtain the true answer.

This time, let's take a look of the quantum version in the first quantization formalism.
<!-- Specifically, the version under second qunatization (or, in Fock space). -->

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

Now, this doesn't look like a linear inhomogeneous equation that we're used to in the classical Green's function formulation. However, we can re-write it to the following form:

$$
\begin{aligned}
\left[i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2\right] \Psi (\vec r, t) &= V(\vec r, t) \Psi(\vec r, t)\\
\hat H  \Psi (\vec r, t) &= g(\vec r, t).
\end{aligned}
\tag{3}
$$

<!-- Assuming the potential is time-independent we can move it to the operator on the left hand side:

$$
\frac{\left[i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2\right]}{V(\vec r)} \Psi (\vec r, t) = \Psi(\vec r, t) \tag{3.1}
$$ -->


which looks much like the linear inhomogeneous equation we are after.
With only one exception being that the inhomogeneous source $g(\vec r, t)$ is $\Psi(\vec r, t)$ dependent.
We can solve this, but we need a recursive solution to find $\Psi(\vec r, t)$.

Or, with Greens function, instead, we can solve the following inhomogeneous equations:

$$
\begin{aligned}
\left[i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2\right] G(\vec r, t;\vec r',t') &= \delta(\vec r -\vec r')\delta(t - t').
\end{aligned}
$$

Assuming $V$ is time-independent, we have energy conservation, hence the time-evolution operator $\mathcal{T} e^{-i/\hbar \int_{t'}^{t} \hat H \cdot t dt} = e^{-i/\hbar \hat H (t-t')}$, where $\mathcal{T}$ is the time ordering operator. We can use this time-evolution operator instead of integrate over $\delta (t-t)$ to transform the inhomogenous source $\Psi(\vec r, t)$,

$$
\begin{aligned}
\left[i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2\right] G(\vec r, t;\vec r',t') &= \delta(\vec r -\vec r') e^{-i\frac{\hat H}{\hbar} (t-t')},
\end{aligned}
\tag{4}
$$

if we multiply $\Psi(\vec r', t')$ to both side and integrate over $r'$:

$$
\begin{aligned}
\int \left[i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2\right] G(\vec r, t;\vec r',t') \Psi(\vec r', t') d \vec r' &= \int \delta(\vec r -\vec r') e^{-i\frac{\hat H}{\hbar} (t-t')} \Psi(\vec r', t') d \vec r'\\
&= \Psi(\vec r, t). \tag{4.1}
\end{aligned}
$$

Eq. 4.1 solves the Eq. 3 when $V(\vec r, t) = 1$:

$$
\left[i\hbar \frac{\partial}{\partial t} +\frac{\hbar^2}{2m} \nabla^2\right] \Psi (\vec r, t) =  \Psi(\vec r, t) \tag{4.2}
$$


Comparing Eq. 4.1 to Eq. 4.2, we see that $\Psi(\vec r, t)$ can be found by:

$$
\Psi(\vec r,t) = \int G(\vec r, t;\vec r',t') \Psi(\vec r',t')  d^3 r'.
\tag{5}
$$

Notice that in Eq. 5, the solution is also present in the integral which suggests we still need a recursive or iterative method to obtain the answer, but it should be much simpler than the original problem.


Taking a good look at Eq. 5, we see that $G(\vec r, t;\vec r',t')$ links $\Psi (\vec r', t')$ to $\Psi (\vec r, t)$, effectively, _propagates_ the wavefunction from one state to another.
Note that propagation implies $t > t'$, i.e. $t$ is a time later then $t'$ and it is because of this $\mathcal{T}$ is dropped in Eq. 4.

To further clarify this _propagation_, recall that due to energy conservation, using again the time evolution operator $U(t,t') = e^{-\frac{i}{\hbar}H(t-t')}$.
Expanding the wavefunction in the position representation as: $\Psi(\vec r, t) = \braket{\vec r \vert \Psi(t)}$, we can re-express the wavefunction at position $\vec r$ and time $t$ as:

$$
\Psi(\vec r, t) = \bra{\vec r} e^{-\frac{i}{\hbar}H(t-t')} \Psi(t')
$$

Inserting the closure relation of the position operator $\int \ket{\vec r'}\bra{\vec r'} d^3 r' = \mathcal{1}$:

$$
\Psi(\vec r, t) = \int \bra{\vec r}e^{-\frac{i}{\hbar}H(t-t')}\ket{\vec r'} \bra{\vec r'} \Psi(t') d^3 r'.
\tag{6}
$$

Comparing Eq. 6 to Eq. 5, we see that:

$$
\begin{aligned}
G(\vec r, t;\vec r',t') &= \bra{\vec r}e^{-\frac{i}{\hbar}H(t-t')}\ket{\vec r'}\\
&= \bra{\vec r}e^{-\frac{i}{\hbar}H(t)} \cdot e^{\frac{i}{\hbar}H(t')} \ket{\vec r'}\\
&= \braket{\vec r, t\vert\vec r', t'}.
\end{aligned}
\tag{7}
$$

From Eq. 7, we see that we have associated the Green's function to the probability amplitude of preparing the particle in a state $\ket{\vec r', t'}$ and later find that that particle in state $\bra{\vec r, t}$.

To give these "states" (which are actually operators) meaning, we need to insert another closure relation: $\sum_n \ket{n}\bra{n} = \mathcal{1}$ where $\ket{n}$ and $\bra{n}$ are eigenvectors of the Hamiltonian.
With the closure relation inserted, the Green's function reads:

$$
G(\vec r, t;\vec r',t') = \sum_n \bra{\vec r} e^{-\frac{i}{\hbar}H(t-t')} \ket{n}\braket{n\vert\vec r'}
$$

since the Hamiltonian $\hat H$ acts on the eigenvectors and gives us the eigenvalues $E_n$, also noting that acting the position operator $\bra{r}$ on the eigenvectors $\ket{n}$ gives us the eigenfunctions $\psi_n(r)$, we have:

$$
\begin{aligned}
G(\vec r, t;\vec r',t') &= \sum_n \braket{\vec r \vert n}\braket{n\vert\vec r'} e^{-\frac{i}{\hbar}E_n(t-t')}\\
&= \sum_n \psi_n(\vec r) \psi_n^*(\vec r') e^{-\frac{i}{\hbar}E_n(t-t')}.
\end{aligned}
$$

Remembering that we have implicitly set $t > t'$ for this relation and for this propagator, if $t<t'$ things should equals to $0$. If we don't constrain the time ordering, then we would arrived at [:link: a kernal function for both retarded and advanced Green's function](https://physics.stackexchange.com/questions/494134/single-particle-greens-function). To achieve time ordering, we insert a Heaviside step function $\Theta$ into the expression:

$$
\begin{aligned}
G(\vec r, t;\vec r',t') &= \Theta(t-t') \sum_n \psi_n(\vec r) \psi_n^*(\vec r') e^{-\frac{i}{\hbar}E_n(t-t')}. \tag{8}
\end{aligned}
$$

This is called the retarded Green's function and it satisfies Eq. 4 and can be used to construct our general solution to Eq. 1 (again, assuming $\hat H$ is time-independent since we did so to derive this solution by assuming $V(\vec r, t) = 1$. However, we can generalize it to time-dependent situation by introducing time-dependence by changing the time-evolution operator to $e^{-i/\hbar \int_{t'}^{t} \hat H t dt}$ so that $E_n$ is time-dependence in the end).

Fourier transforming this Green's function from time-domain to frequency domain, we get:

$$
\begin{aligned}
\mathcal{F}[G(\vec r, t;\vec r',t')](\vec r, \vec r', E) &= \int_{-\infty}^{\infty} \Theta(t-t') \sum_n \psi_n(\vec r) \psi_n^*(\vec r') e^{-i\frac{E_n}{\hbar}(t-t')} e^{i \frac{E}{\hbar}}(t-t') d(t-t')\\
&= \int_{0}^{\infty} \sum_n \psi_n(\vec r) \psi_n^*(\vec r') e^{-i E_n\textbf{t}} e^{i E\textbf{t}} d\textbf{t}\\
&= \sum_n \psi_n(\vec r)  \psi_n^*(\vec r') \int_{0}^{\infty} e^{i(E-E_n)\textbf{t}} d\textbf{t} \tag{9}
\end{aligned}
$$

where $\textbf{t} = \frac{t-t'}{\hbar}$.

Now, let's insert $e^{-\eta \textbf{t}}$ in to Eq. 9 where $\eta$ is a positive _infinitesimal_ quantity.
We can do this because the value of $e^{-\eta \textbf{t}}$ goes to $1$ as $\eta \rightarrow 0^+$ (alternatively, check out [:link: this post](../../../2022/03/02/FT_Heaviside_function.html) of how to properly Fourier transform Heaviside step functions). And then Fourier transform Eq. 9:

$$
\begin{aligned}
\mathcal{F}[G(\vec r, t;\vec r',t')](\vec r, \vec r', E) &= \sum_n \psi_n(\vec r)  \psi_n^*(\vec r') \int_{0}^{\infty} e^{i(E-E_n)\textbf{t}} e^{-\eta \textbf{t}} d\textbf{t}\\
=G(\vec r, \vec r', E)&= \sum_n \psi_n(\vec r)  \psi_n^*(\vec r') \int_{0}^{\infty} e^{i(E-E_n+i\eta)\textbf{t}} d\textbf{t}\\
&= \sum_n \psi_n(\vec r)  \psi_n^*(\vec r') \frac{e^{i(E-E_n)\textbf{t}} e^{-\eta \textbf{t}} |_{\textbf{t}=0}^{\textbf{t}=\infty}}{i(E-E_n+i\eta)}\\
&= \sum_n \psi_n(\vec r)  \psi_n^*(\vec r') \frac{-1}{i(E-E_n+i\eta)}\\
&= \sum_n \psi_n(\vec r)  \psi_n^*(\vec r') i\frac{1}{(E-E_n+i\eta)} \tag{10}
\end{aligned}
$$


From Eq. 9, We see that when there are poles (divergences) when the energy matches the eigenvalue $E_n$.

To write the whole thing in Dirac's bra-ket notation and expand this in eigenvector basis

$$
G(E)_{kl}=\braket{k | G(E) | l} = \sum_n i \frac{\braket{k \vert n} \braket{n \vert l}}{E-E_n+i\eta} \tag{11}
$$

---

Second quantization version, coming soon!

Examples, coming soon!
