---
layout: post
title: Polarizability from quantum TD-LRT
date: 2025-11-04
categories: Post
description: Calculate Polarizability form time-dependent linear response theory.
tags: DFT, Math
---

Previously we have shown how [:link:quantum TD-LRT](./TD_LRT.html) works, now let's put that into work by calculating the polarizability of a quantum system. 
Here we start by considering the dipole-electric field interaction energy

$$
\hat{V}(t) = -\mathbf{\hat d} \cdot \mathbf{E}(t) = e\mathbf{\hat r} \cdot \mathbf{E}(t) \tag{1}
$$

where the external electric field is still

$$
\mathbf{E}(t) = \mathbf{E}_0 e^{-i\omega t} + \mathbf{E}_0^* e^{+i\omega t}.
$$

Substituting Eq. 1 into Eq. 3 of [:link:quantum TD-LRT](./TD_LRT.html), we get:

$$
\dot{c}_n(t) =  \frac{-1}{i\hbar}\sum_m  c_m(t) e^{i\omega_{nm}t}  \lambda \braket{n|\mathbf{\hat d}|m} \cdot \mathbf{E}(t)
$$

Again, if we initialize system to $\ket{0}$ at $t_0=-\infty$ (see Eq. 6 in [:link:quantum TD-LRT](./TD_LRT.html) ). From now assuming $n\neq 0$, to first order, we have

$$
\dot{c}_n(t) =  \frac{-1}{i\hbar} e^{i\omega_{n0}t} \braket{n|\mathbf{\hat d}|0} \cdot \mathbf{E}(t)
$$

Explicitly

$$
\begin{aligned}
\dot{c}_n(t) &= \frac{-1}{i\hbar} e^{i\omega_{n0}t}  \braket{n|\mathbf{\hat d}|0} \cdot \mathbf{E}(t)\\
&=\frac{-1}{i\hbar} e^{i\omega_{n0}t} \braket{n|\mathbf{\hat d}|0} \cdot 
\left( \mathbf{E}_0e^{-i\omega t} + \mathbf{E}_0^*e^{+i\omega t}\right)\\
&=\frac{i}{\hbar} e^{i\omega_{n0}t} \braket{n|\mathbf{\hat d}|0} \cdot \mathbf{E}_0e^{-i\omega t} + 
\frac{i}{\hbar} e^{i\omega_{n0}t} \braket{n|\mathbf{\hat d}|0} \cdot \mathbf{E}_0^*e^{+i\omega t}\\
&=F_{-}(t) + F_{+}(t) \tag{2}
\end{aligned}
$$

{% include admonition.html type="info" title="Note: Time ordering" body="
$e^{\mu t'}$ is a damping factor added to the E-field so that we have perturbation adiabatically turned on in the remote past, and the integration converges as $t_0 \to -\infty$. For more, see [this post](https://chengcheng-xiao.github.io/post/2021/08/16/Greens_function_2.html).
" %}

Now we want to get $c_n(t)$, for that we need to integrate $$\dot{c}_n(t)$$. 
Here we assume the field was adiabatically turned on in the remote past $t_0=-\infty$ by multiplying the E-field by $e^{\mu t'}$ with $\mu \to 0^+$(or equivalently by adding a small positive imaginary part to the frequency). Then integrate from $t'=-\infty$ to $t'=t$, for $F_{-}(t)$ (similar to Eq. 6 in [:link:quantum TD-LRT](./TD_LRT.html)) we get

$$
\begin{aligned}
\int_{-\infty}^t F_{-}(t') dt' &= \frac{i}{\hbar}  \braket{n|\mathbf{\hat d}|0} \cdot \mathbf{E}_0 \int_{-\infty}^t e^{[i(\omega_{n0}-\omega)+\mu] t'} dt'\\
&=\frac{i}{\hbar}  \braket{n|\mathbf{\hat d}|0} \cdot \mathbf{E}_0 \frac{e^{i[(\omega_{n0}-\omega)+\mu] t}}{i(\omega_{n0}-\omega)+\mu}
\end{aligned}
$$

Similarily, for $F_+(t)$

$$
\begin{aligned}
\int_{-\infty}^t F_{+}(t') dt' = \frac{i}{\hbar}  \braket{n|\mathbf{\hat d}|0} \cdot \mathbf{E}^*_0 \frac{e^{[i(\omega_{n0}-\omega)+\mu] t}}{i(\omega_{n0}+\omega)+\mu}
\end{aligned}
$$

Combining

$$
\begin{aligned}
{c}_n(t) &= \frac{i}{\hbar}  \braket{n|\mathbf{\hat d}|0} 
\left( 
\mathbf{E}_0 \frac{e^{[i(\omega_{n0}-\omega)+\mu] t}}{i(\omega_{n0}-\omega)+\mu}+
\mathbf{E}^*_0 \frac{e^{[i(\omega_{n0}+\omega)+\mu]  t}}{i(\omega_{n0}+\omega)+\mu}
\right)\\
&=\frac{i}{\hbar} \braket{n|\mathbf{\hat d}|0} 
\left( 
\mathbf{E}_0 \frac{e^{i(\omega_{n0}-\omega) t}}{i(\omega_{n0}-\omega)+0^+}+
\mathbf{E}^*_0 \frac{e^{i(\omega_{n0}+\omega) t}}{i(\omega_{n0}+\omega)+0^+}
\right)\\
\end{aligned} \tag{3}
$$

where we have gotten rid of $e^{it0^+}=0$. Eq. 3 shows how the wavefunction evolves (to the first order) under a small perturbation of an external E-field - dipole interaction.

We can now calculate the expectation of the dipole operator. First remember that we have the system prepared in $\ket{0}$ ($c_0(t) \approx 1$) so that

$$
\begin{aligned}
\ket{\psi(t)} &= c_0(t) e^{-i\omega_0t} \ket{0} + \sum_{m\neq 0} c_m(t) e^{-i\omega_mt} \ket{m} \\
&\approx e^{-i\omega_0t} \ket{0} + \sum_{m\neq 0} c_m(t) e^{-i\omega_mt} \ket{m}
\end{aligned}
$$

The expectation of the dipole operator becomes 
<!-- (we can also do this with $\lambda$ but I'll not do that here as the results is the same) -->

$$
\begin{aligned}
\braket{\mathbf{\hat d}}(t) &= \braket{\psi|\mathbf{\hat d}|\Psi}\\
&=\sum_{m,m'} c^*_m(t) c_{m'}(t) e^{i(\omega_m-\omega_{m'})t} \braket{m|\mathbf{\hat d}|m' }\\
&= c^*_0(t) c_{0}(t)  \braket{0|\mathbf{\hat d}|0 }\\
&+ \sum_{m\neq0} \left( 
c^*_m(t) c_0(t) e^{i(\omega_m-\omega_{0})t} \braket{m|\mathbf{\hat d}|0}+
c^*_0(t) c_m(t) e^{i(\omega_0-\omega_{m})t} \braket{0|\mathbf{\hat d}|m}
\right)\\
&+ \sum_{m\neq0,m'\neq0} c^*_m(t) c_{m'}(t) e^{i(\omega_m-\omega_{m'})t} \braket{m|\mathbf{\hat d}|m' }\\
&\approx  \braket{0|\mathbf{\hat d}|0 }\\
&+ \sum_{m\neq0} \left( 
c^*_m(t) e^{i(\omega_m-\omega_{0})t} \braket{m|\mathbf{\hat d}|0}+
c_m(t) e^{i(\omega_0-\omega_{m})t} \braket{0|\mathbf{\hat d}|m}
\right)\\
&+ \sum_{m\neq0,m'\neq0} c^*_m(t) c_{m'}(t) e^{i(\omega_m-\omega_{m'})t} \braket{m|\mathbf{\hat d}|m' }\\
\end{aligned}
$$

We see there are zero-th, first, and second order terms involving $c$ coeffs. 
The zero-th order term - $$c^*_0(t) c_{0}(t)  \braket{0|\mathbf{\hat d}|0 }$$ is a constant and does not affect the polarizability so we can safely ignore it, and if we ignore the second order term (because it is small), only focusing on the first order term, the dipole expectation value becomes

$$
\begin{aligned}
\braket{\mathbf{\hat d}}(t) &\approx \sum_{m\neq0} \left( 
c^*_m(t) e^{i(\omega_m-\omega_{0})t} \braket{m|\mathbf{\hat d}|0}+
c_m(t) e^{i(\omega_0-\omega_{m})t} \braket{0|\mathbf{\hat d}|m}
\right) \\
&= \sum_{m\neq0} \left( 
c^*_m(t) e^{i\omega_{m0}t} \braket{m|\mathbf{\hat d}|0}+
c_m(t) e^{i\omega_{0m}t} \braket{0|\mathbf{\hat d}|m}
\right) 
\end{aligned}\tag{4}
$$

substituting Eq. 3 into Eq. 4, we get

$$
\begin{aligned}
\braket{\mathbf{\hat d}}(t) &\approx \sum_{m\neq0} \left[ 
\frac{-i}{\hbar}  \braket{0|\mathbf{\hat d}|m} 
\left( 
\mathbf{E}^*_0 \frac{e^{-i(\omega_{n0}-\omega) t}}{-i(\omega_{m0}-\omega)+0^+}+
\mathbf{E}_0 \frac{e^{-i(\omega_{m0}+\omega) t}}{-i(\omega_{m0}+\omega)+0^+}
\right)
e^{i\omega_{m0}t} \braket{m|\mathbf{\hat d}|0}\right]\\

&+\sum_{m\neq0} \left[  
\frac{i}{\hbar}  \braket{m|\mathbf{\hat d}|0} 
\left( 
\mathbf{E}^*_0 \frac{e^{i(\omega_{m0}-\omega) t}}{i(\omega_{m0}-\omega)+0^+}+
\mathbf{E}_0 \frac{e^{i(\omega_{m0}+\omega) t}}{i(\omega_{m0}+\omega)+0^+}
\right)
e^{i\omega_{0m}t} \braket{0|\mathbf{\hat d}|m}\right]\\

&= \sum_{m\neq0} \left[ 
\frac{1}{\hbar}  \braket{0|\mathbf{\hat d}|m} 
\left( 
\mathbf{E}^*_0 \frac{e^{-i(\omega_{n0}-\omega) t}}{\omega_{m0}-\omega+i0^+}+
\mathbf{E}_0 \frac{e^{-i(\omega_{m0}+\omega) t}}{\omega_{m0}+\omega+i0^+}
\right)
e^{i\omega_{m0}t} \braket{m|\mathbf{\hat d}|0}\right]\\

&+\sum_{m\neq0} \left[  
\frac{1}{\hbar}  \braket{m|\mathbf{\hat d}|0} 
\left( 
\mathbf{E}_0 \frac{e^{i(\omega_{m0}-\omega) t}}{\omega_{m0}-\omega-i0^+}+
\mathbf{E}^*_0 \frac{e^{i(\omega_{m0}+\omega) t}}{\omega_{m0}+\omega-i0^+}
\right)
e^{i\omega_{0m}t} \braket{0|\mathbf{\hat d}|m}\right]

\end{aligned} \tag{5}
$$

{% include admonition.html type="info" title="Note: electric field definition" body="
We use $e^{i\omega t}$ and $e^{-i\omega t}$ to construct $\cos$. So here simply taking terms related to $e^{i\omega t}$ should give us the polarizability.
" %}

Taking only terms that contains $e^{-i\omega t}$ from Eq. 5

$$
\begin{aligned}
\braket{\mathbf{\hat d}}(t)  &\approx 
\frac{1}{\hbar} \sum_{m\neq0} \left[ 
\braket{0|\mathbf{\hat d}|m} 
\left( 
\mathbf{E}_0 \frac{e^{-i(\omega_{m0}+\omega) t}}{\omega_{m0}+\omega+i0^+}
\right)
e^{i\omega_{m0}t} \braket{m|\mathbf{\hat d}|0}\right]\\
&+\frac{1}{\hbar}\sum_{m\neq0} \left[ \braket{m|\mathbf{\hat d}|0} 
\left( 
\mathbf{E}_0 \frac{e^{i(\omega_{m0}-\omega) t}}{\omega_{m0}-\omega-i0^+}+
\right)
e^{i\omega_{0m}t} \braket{0|\mathbf{\hat d}|m}\right]\\
&=\frac{1}{\hbar} \sum_{m\neq0} \left[ 
\braket{0|\mathbf{\hat d}|m} \braket{m|\mathbf{\hat d}|0}
\left( 
\frac{e^{-i\omega_{m0} t}e^{i\omega_{m0}t}}{\omega_{m0}+\omega+i0^+}
\right)
 \right]\mathbf{E}_0e^{-i\omega t} \\
&+\frac{1}{\hbar}\sum_{m\neq0} \left[ 
\braket{m|\mathbf{\hat d}|0} \braket{0|\mathbf{\hat d}|m}
\left( 
 \frac{e^{i\omega_{m0} t}e^{i\omega_{0m}t}}{\omega_{m0}-\omega-i0^+}
\right)
 \right]\mathbf{E}_0e^{-i\omega t}\\
 
 &=\frac{1}{\hbar} \sum_{m\neq0}
\left( 
\frac{\braket{0|\mathbf{\hat d}|m} \braket{m|\mathbf{\hat d}|0}}{\omega_{m0}+\omega+i0^+}
+\frac{\braket{m|\mathbf{\hat d}|0} \braket{0|\mathbf{\hat d}|m}}{\omega_{m0}-\omega-i0^+}
\right)
\mathbf{E}_0e^{-i\omega t} \tag{5.1}

\end{aligned}
$$

According to Maxwell's equations, an external field we have

$$
\mathbf{P} (t) = \frac{\mathbf{d}(t)}{V} = \varepsilon_0 \boldsymbol{\alpha}(\omega) \mathbf{E}(t,\omega)
$$

so

$$
\mathbf{d}(t) = V\varepsilon_0\boldsymbol{\alpha}(\omega)\mathbf{E(t,\omega)} \tag{5.2}
$$

Comparing Eq. 5.1 to Eq. 5.2, we see that

$$
\begin{aligned}
V\varepsilon_0\boldsymbol{\alpha}(\omega) &= \frac{1}{\hbar} \sum_{m\neq0}
\left( 
\frac{\braket{0|\mathbf{\hat d}|m} \braket{m|\mathbf{\hat d}|0}}{\omega_{m0}+\omega+i0^+}
+\frac{\braket{m|\mathbf{\hat d}|0} \braket{0|\mathbf{\hat d}|m}}{\omega_{m0}-\omega-i0^+}
\right)\\
\end{aligned}
$$

Now replacing $i0^+$ with phenomenological damping factor $i\Gamma_m/2$ of mode $m$,

$$
\begin{aligned}
V\varepsilon_0\boldsymbol{\alpha}(\omega) &= \frac{1}{\hbar} \sum_{m\neq0}
\left( 
\frac{\braket{0|\mathbf{\hat d}|m} \braket{m|\mathbf{\hat d}|0}}{\omega_{m0}+\omega+\Gamma_m/2}
+\frac{\braket{m|\mathbf{\hat d}|0} \braket{0|\mathbf{\hat d}|m}}{\omega_{m0}-\omega-i\Gamma_m/2}
\right)\\
&= \frac{1}{\hbar} \sum_{m\neq0}
\left( 
\frac{\braket{0|\mathbf{\hat d}|m} \braket{m|\mathbf{\hat d}|0} (\omega_{m0}-\omega-i\Gamma_m/2)}{(\omega_{m0}+\omega+\Gamma_m/2)(\omega_{m0}-\omega-i\Gamma_m/2)}
+\frac{\braket{m|\mathbf{\hat d}|0} \braket{0|\mathbf{\hat d}|m}(\omega_{m0}+\omega+\Gamma_m/2)}
{(\omega_{m0}+\omega+\Gamma_m/2)(\omega_{m0}-\omega-i\Gamma_m/2)}
\right)\\
&= \frac{1}{\hbar} \sum_{m\neq0}
\left( 
\frac{\braket{0|\mathbf{\hat d}|m} \braket{m|\mathbf{\hat d}|0} \omega_{m0}}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega -  \Gamma_m^2/4} +
\frac{\braket{m|\mathbf{\hat d}|0} \braket{0|\mathbf{\hat d}|m} \omega_{m0}}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega - \Gamma_m^2/4} 
\right)\\
\end{aligned}
$$

and we can now calculate the polarizability tensor $\boldsymbol{\alpha}$ 

$$
\begin{aligned}
\boldsymbol{\alpha}(\omega) &= \frac{1}{V}\frac{1}{\varepsilon_0}\frac{1}{\hbar} \sum_{m\neq0}
\left( 
\frac{\braket{0|\mathbf{\hat d}|m} \braket{m|\mathbf{\hat d}|0} \omega_{m0}}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega -  \Gamma_m^2/4} +
\frac{\braket{m|\mathbf{\hat d}|0} \braket{0|\mathbf{\hat d}|m} \omega_{m0}}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega - \Gamma_m^2/4} 
\right)\\
\end{aligned}
$$

$$\boldsymbol{\alpha}$$ is a 3 by 3 rank-2 tensor, because $$\braket{m\vert \mathbf{\hat{d}}\vert 0}$$ comes from $$\braket{m\vert \mathbf{\hat d}\vert 0}\mathbf{E}_0$$,  $$\braket{0\vert \mathbf{\hat d}\vert m}$$ can lie in a different direction, and the components of $$\boldsymbol{\alpha}$$ become:

$$
\begin{aligned}
{\alpha}_{ij}(\omega) &= \frac{1}{V}\frac{1}{\varepsilon_0}\frac{1}{\hbar} \sum_{m\neq0}
\left( 
\frac{\braket{0|\mathbf{\hat d}_i|m} \braket{m|\mathbf{\hat d}_j|0} \omega_{m0}}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega -  \Gamma_m^2/4} +
\frac{\braket{m|\mathbf{\hat d}_j|0} \braket{0|\mathbf{\hat d}_i|m} \omega_{m0}}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega -  \Gamma_m^2/4} 
\right)\\
\end{aligned}
$$

Using number density $N = 1/V$ which gives the number of this dipole moments in side a unit volume, and ignoring the second order term $- \Gamma_m^2/4$ since dampening is small, we have

$$
\begin{aligned}
{\alpha}_{ij}(\omega) &= \frac{1}{V}\frac{1}{\varepsilon_0}\frac{1}{\hbar} \sum_{m\neq0}
\left( 
\frac{\braket{0|\mathbf{\hat d}_i|m} \braket{m|\mathbf{\hat d}_j|0} \omega_{m0}}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega } +
\frac{\braket{m|\mathbf{\hat d}_j|0} \braket{0|\mathbf{\hat d}_i|m} \omega_{m0}}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega } 
\right)\\
\end{aligned}
$$


For a single state transition from $\ket{0}$ to $\ket{m}$ contribution, we have

$$
{\alpha}_{ij}(\omega) =\frac{N}{\varepsilon_0} \frac{\omega_{m0} }{\hbar} \frac{\braket{0|\mathbf{\hat d}_i|m} \braket{m|\mathbf{\hat d}_j|0} + \braket{0|\mathbf{\hat d}_j|m} \braket{m|\mathbf{\hat d}_i|0} }{\omega_{m0}^2-\omega^2-i\Gamma_m\omega} \tag{6}
$$ 

Averaging over all three directions, we get

$$
\bar{\alpha} (\omega)= \sum_{i=x,y,z}\mathbf{\alpha}_{ii}/3 = \frac{N}{\varepsilon_0} \frac{2\omega_{m0} }{3\hbar} 
\frac{|\braket{0|\mathbf{\hat d}|m}|^2}{\omega_{m0}^2-\omega^2-i\Gamma_m\omega} \tag{7}
$$

## Oscillator strength
Comparing to the result from the Lorentz model

$$
\alpha(\omega) = \frac{Nq^2}{\varepsilon_0 m} \frac{1}{\omega_0^2-\omega^2-i\omega\Gamma}
$$

we see that with quantum version (Eq. 7), we need to have

$$
\frac{2\omega_{m0}|\braket{0|\mathbf{\hat d}|m}|^2}{3\hbar}  \to \frac{q^2}{m}
$$

hence the oscillator strength $S_m$ can be defined as

$$
S_m= \frac{m}{q^2} \frac{2\omega_{m0}|\braket{0|\mathbf{\hat d}|m}|^2}{3\hbar}  
$$

so that 

$$
\frac{q^2}{m} S_m = \frac{2\omega_{m0}|\braket{0|\mathbf{\hat d}|m}|^2}{3\hbar} 
$$

and the corresponding modified Lorentz model is

$$
\alpha_m(\omega) = \frac{Nq^2}{\varepsilon_0 m} \frac{S_m}{\omega_0^2-\omega^2-i\omega\Gamma}
$$

