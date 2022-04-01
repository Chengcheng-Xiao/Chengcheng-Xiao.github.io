---
layout: post
title: From Autocorrelation to Phonon bands
date: 2022-03-31
categories: Post
description: Atomic velocity autocorrelation function (VACF) is like the phonoic version of the electron Green's function. It reflects the degrees of "similarity" of the atomic velocity between different times. If a system can be described using harmonic approximation, then the atomic oscillation will give a perfect VACF, naturally, the line-width of the phonon spectrum will also be vanishing. This post explains the relation between VACF and phonon spectrum and provides a derivation from ACVF to phonon bands (spectrum).
tags: DFT
---


## Definition of a Correlation function
<!-- Ref: https://nanohub.org/resources/7581/download/Martini_L9_DynamicProperties.pdf -->
The correlation between signal A and B:

$$
C(t)=\lim _{\tau \rightarrow \infty} \frac{1}{\tau} \int_{0}^{\tau} A\left(t_{0}\right) B\left(t_{0}+t\right) d t_{0}
$$

or more generally:

$$
C(t)=\lim _{\tau \rightarrow \infty} \frac{\int_{-\tau}^{\tau} A\left(t_{0}\right) B\left(t_{0}+t\right) d t_{0}}{\int_{-\tau}^{\tau} A\left(t_{0}\right) B\left(t_{0}\right) d t_{0}}
$$

## From autocorrelation to phonon DOS
<!-- Ref: https://www.fisica.unam.mx/personales/naumis/index_archivos/Tesis/tesis_Hugo.pdf (password: tesis) -->

The velocity of atom is $i$: $v_i(t)$. Fourier transform this velocity (from time domain to frequency domain), we get:

$$
v_i(\omega) = \int_{-\infty}^{\infty} v_i(t) e^{i\omega t} dt
$$

The so called `power spectrum` is defined as:

$$
\begin{align*}
|v_i(\omega)|^2 &= v^*_i(\omega) v_i(\omega) \\
 &= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} v^*_i(t) v_i(t') e^{i\omega (t-t')} dt dt'
\end{align*}
$$

Substitute $t''=t-t'$, we have:

$$
|v_i(\omega)|^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} v^*_i(t''+t') v_i(t') e^{i\omega (t'')} dt'' dt'
$$

Since the phonon exist in the harmonic limit, we want to express $v_i(t)$ in terms of harmonic displacement $r$ (an plane wave expansion):

$$
r_j(t) = \sum_s Q_{s,j} e^{-i\omega_s t}
$$

where $s$ stands for phonon branch and $j$ is a composit index for the vibriation on three directions on atom $i$, $Q$ is the vibration amplitude (with $\frac{1}{2} m_i$ absorbed).

The velocity can now be expressed as:

$$
\dot{r}_{j}(t)=v_{j}=\sum_{s} Q_{s j}\left(-i \omega_{s}\right) e^{-i \omega_{s} t}
$$

Substitute Eq. (5) to (3), we get:

$$
\begin{array}{c}
\frac{1}{N} \sum_{i=1}^{N}\left|v_{i}(\omega)\right|^{2}=\frac{1}{N} \sum_{s, s^{\prime}} \sum_{j=1}^{3 N} \int_{-\infty}^{\infty} Q_{s j} Q_{s^{\prime} j}^{*}\left(i \omega_{s}\right)\left(i \omega_{s^{\prime}}\right) e^{i\left(\omega+\omega_{s^{\prime}}\right) t^{\prime \prime}} d t^{\prime \prime} \times \int_{-\infty}^{\infty} e^{-i\left(\omega_{s}-\omega_{s^{\prime}}\right) t^{\prime}} d t^{\prime}
\end{array}
$$

Note that
$$
\int_{-\infty}^{\infty} e^{-i\left(\omega_{s}-\omega_{s^{\prime}}\right) t^{\prime}} d t^{\prime} = \delta(\omega_{s}-\omega_{s^{\prime}})
$$
, and that
$$
\left|Q_{s j}\right|^{2} \omega_{s}^{2}=T k_{B}
$$
due to equipartition theorem, Eq. (5) becomes:

$$
\sum_{i=1}^{N}\left|v_{i}(\omega)\right|^{2}=\sum_{s} \int_{-\infty}^{\infty} 3 N k_{B} T e^{i\left(\omega+\omega_{s}\right) t^{\prime \prime}} d t^{\prime \prime}=3 N k_{B} T \sum_{s} \delta\left(\omega+\omega_{s}\right)
$$

Since the phonon DOS is $\sum_{s} \delta\left(\omega+\omega_{s}\right)$, it can be expressed as:

$$
\rho(\omega)=\sum_{s} \delta\left(\omega+\omega_{s}\right)=\frac{1}{3 N T k_{B}} \sum_{i=1}^{N}\left|\mathbf{v}_{i}(\omega)\right|^{2}
$$

Remember we have already derived
$$
\left|\mathbf{v}_{i}(\omega)\right|^{2}
$$
 in Eq. (3):

$$
\rho(\omega)=\frac{1}{3 N T k_{B}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \sum_{i=1}^{N} \mathbf{v}_{i}\left(t^{\prime \prime}+t^{\prime}\right) \cdot \mathbf{v}_{i}\left(t^{\prime}\right) e^{i \omega\left(t^{\prime \prime}\right)} d t^{\prime \prime} d t^{\prime}
$$

The autocorrelation function can be defined (with a normalization factor of $1/C_{xx}(0)$) as:

$$
C_{xx}(t') = \int_{-\infty}^{\infty}\mathbf{v}_{i}\left(t^{\prime \prime}+t^{\prime}\right) \cdot \mathbf{v}_{i}\left(t^{\prime}\right) dt' = \braket{\mathbf{v}_{i}\left(t^{\prime \prime}+t^{\prime}\right) \cdot \mathbf{v}_{i}\left(t^{\prime}\right)}
$$

so that Eq. (8) becomes:

$$
\rho(\omega)=\frac{1}{3 N T k_{B}} \int_{-\infty}^{\infty} \sum_{i=1}^{N}\left\langle\mathbf{v}_{i}(t) \cdot \mathbf{v}_{i}(0)\right\rangle e^{i \omega t} d t
$$

## Power spectrum and FT
### Power spectrum
<!-- Ret: https://www.wikiwand.com/en/Spectral_density#/Power_spectral_density -->

The `energy` of a signal is defined as:

$$
E \triangleq \int_{-\infty}^{\infty}|x(t)|^{2} d t
$$

Using Parseval's theorem, we can write:

$$
\int_{-\infty}^{\infty}|x(t)|^{2} d t=\int_{-\infty}^{\infty}|\hat{x}(f)|^{2} d f,
$$

Where,

$$
\hat{x}(f) \triangleq \int_{-\infty}^{\infty} e^{-i 2 \pi f t} x(t) d t
$$

The integrand  $\left|\hat{x}(f) \right|^{2}$ can be interpreted as a density function describing the energy contained in the signal at the frequency $f$.
Therefore, the energy spectral density of $x(t)$ is defined as:

$$
\bar{S}_{x x}(f) \triangleq|\hat{x}(f)|^{2}
$$

Interestingly, this energy spectral density is actually a dual to the autocorrelation function $S_{xx}(t)$:

$$
\begin{align*}
C_{xx}(\tau) &= \int_{\infty}^{\infty} S_{xx}(f) e^{i2\pi\tau f} df \\
&= \int_{\infty}^{\infty}\int_{\infty}^{\infty}\int_{\infty}^{\infty} x(t)x^*(t') e^{i2\pi f(t'-t)} dt dt' e^{i2\pi f \tau} df \\
&= \int \int x(t)x^*(t') \int_{\infty}^{\infty} e^{i2\pi f(t'-t)} e^{i2\pi f \tau} df dt dt'\\
&= \int \int x(t)x^*(t') \delta(t'-t+\tau) dt dt'\\
&= \int \int x(t)x^*(t') \delta([t'+\tau]-t) dt dt' \\
&= \int \int x(t)x^*(T+\tau) \delta([T]-t) dt d(T+\tau) \\
&= \int \int x(t)x^*(T+\tau) \delta(T-t) dt d(T) \\
&= \int_{\infty}^{\infty} x^*(T+\tau) [\int_{\infty}^{\infty} x(t) \delta(T-t) dt] dT\\
&= \int_{\infty}^{\infty} x^*(T+\tau) x(T) dT
\end{align*}
$$

Note that this autocorrelation function is not normalized, which means it will become zero for a "pulse-like" signal when the integration reaches $\infty$.
To normalize it, simply devided this by $C_{xx}(0)$.

This is the so-called [Wiener–Khinchin theorem](https://www.wikiwand.com/en/Wiener%E2%80%93Khinchin_theorem).

### Derivation of Parseval's (Plancherel's) formula:
This can be easily derived (in general this is actually called Plancherel's formula):

$$
\begin{align*}
\int_{-\infty}^{\infty} f(t) g(t)^{*} d t&=\int_{-\infty}^{\infty}\left(\frac{1}{2 \pi} \int_{-\infty}^{\infty} \bar{f}(\omega) e^{i \omega t} d \omega\right)\left(\frac{1}{2 \pi} \int_{-\infty}^{\infty} \bar{g}\left(\omega^{\prime}\right)^{*} e^{-i \omega^{\prime} t} d \omega^{\prime}\right) d t \\
&=\left(\frac{1}{2 \pi}\right) \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \bar{f}(\omega) \bar{g}\left(\omega^{\prime}\right)^{*}\left[\left(\frac{1}{2 \pi}\right)\int_{-\infty}^{\infty} e^{i\left(\omega-\omega^{\prime}\right) t} d t\right] d \omega^{\prime} d \omega \\

&=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \bar{f}(\omega)\left(\int_{-\infty}^{\infty} \bar{g}\left(\omega^{\prime}\right)^{*} \delta\left(\omega-\omega^{\prime}\right) d \omega^{\prime}\right) d \omega \\
&=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \bar{f}(\omega) \bar{g}(\omega)^{*} d \omega
\end{align*}
$$

and if we substitute $\omega$ with $\omega*2\pi$, we get:

$$
\int_{-\infty}^{\infty} f(t) g(t)^{*} d t = \int_{-\infty}^{\infty} \bar{f}(\omega) \bar{g}(\omega)^{*} d \omega
$$

which is what we want.




---
## Periodic systems


For periodic systems, the phonon bandstructure can also be interpreted as phonon DOS at each $k$ point.
To obtain this "spectrum" function. we need to Fourier transform the velocity function with respect to the unit cell vectors.
For example, lets say we have a $\sqrt[3]{N}\times\sqrt[3]{N}\times\sqrt[3]{N}$ supercell (so that we have a total of N unit cells) and have a MD trajectory file calculated using it (so we have the time-evolution of the velocity of each atom):


![Screenshot 2021-08-20 at 9](_v_images/20210820095646803_318448978.png =478x)

Here, we label the atoms in each cell with $j$ (again a composite label with three direction added) and the unit cell position is expressed as $\vec R$ so that the velocity of atom $j$ at cell $\vec R$ (in three direction) is:

$$
v_{j}(\vec R, t).
\tag{9}
$$

Fourier transform (discrete) Eq. 9 with respect to $\vec R$, we get:

$$
\begin{aligned}
\mathcal{F}[v_{j}(\vec R, t)](\vec k,t) = \frac{1}{\sqrt{N}} \sum_{\vec R} v_j(\vec R,t) e^{i\vec k \vec R} = v_{j}(\vec k, t),
\end{aligned}
\tag{10}
$$

where we have $N$ unit cell in the supercell


Using Eq. 10, we can express the phonon DOS at each $\vec k$ point as:

$$
\rho(\vec k, -\omega) = \frac{1}{3Nk_BT}\ \sum_j \int_{-\infty}^{\infty} \braket{v_{j}(\vec k, t'')\cdot v_{j}(\vec k, 0)} e^{-i\omega(t'')} dt''.
\tag{11}
$$
