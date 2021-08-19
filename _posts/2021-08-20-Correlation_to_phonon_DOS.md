---
layout: post
title: From autocorrelation to phonon DOS
date: 2021-08-19
categories: Post
description: Derivation of how to calculate phonon DOS from autocorrelation functions.
---

The autocorrelation function is a cross-correlation function that tell's the correlation of one signal (function) with a delayed version of it self.

To derive the relation between velocity autocorrelation function and the phonon density of states, let us first start with the Fourier transforming the velocity of an atom $i$, $v_i(t)$.

$$
\mathcal{F}[v_i(t)](\omega) = \int_{\infty}^{\infty}v_i(t)e^{i\omega t} dt
\tag{1}
$$

The power spectrum (which tells us how the energy is distributed over the frequency) of this velocity function is:

$$
\begin{aligned}
|v_i(\omega)|^2 &= v^*_i(\omega) v_i(\omega)
&= \int_{-\infty}^{\infty}  \int_{-\infty}^{\infty} v^*_i(t) v_i(t') e^{i\omega(t-t')} dt dt'.
\end{aligned} \tag{2}
$$

Substitute $t-t'$ with $t''$, the power spectrum can be re-written as:

$$
|v_i(\omega)|^2 = \int_{-\infty}^{\infty}  \int_{-\infty}^{\infty} v^*_i(t''+t') v_i(t') e^{i\omega(t'')} dt'' dt'.
\tag{3}
$$

Before moving on, lets assume that harmonic approximation is valid (so that we have zero-width phonon branches), the atomic displacement with respect to time can be written as:

$$
r_j(t) = \sum_s Q_{s,j} e^{-i\omega_s t},
$$

where $s$ labels the phonon branch and $j$ is a composite index for the vibrations of atom $i$ on three spacial directions. Q is the amplitude of the vibration and $\omega$ is the frequency of the phonon mode.

With the time-dependent displacement derived, the time-dependent velocity can be expressed as:

$$
v_j(t) = \frac{d}{dt} r_j(t) = \sum_s Q_{s,j} (-i\omega_s) e^{-i\omega_s t}.
\tag{4}
$$

Inserting Eq. 4 to Eq.3, and notice we are now using $j$ instead of $i$ to incorporate three spacial dimensions, we get:

$$
\begin{aligned}
|v_j(\omega)|^2 &= \int_{-\infty}^{\infty}  \int_{-\infty}^{\infty} \sum_{s,s'} Q^*_{s,j}(i\omega_s)e^{i\omega_s(t''+t')} Q_{s',j} (-i\omega_s') e^{-i\omega_{s'} t'} e^{i\omega t''} dt'' dt'\\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \sum_{s,s'} Q^*_{s,j}Q_{s',j}(\omega_s \omega_{s'})e^{i(\omega+\omega_s)t''} e^{i(\omega_s - \omega_{s'})t'} dt'' dt'\\
&= \int_{-\infty}^{\infty} \sum_{s,s'} Q^*_{s,j}Q_{s',j}(\omega_s \omega_{s'})e^{i(\omega+\omega_s)t''} \delta(\omega_s - \omega_{s'}) dt''\\
&= \sum_s \int_{-\infty}^{\infty} |Q_{s,j}|^2 \omega_s^2  e^{i(\omega+\omega_s)t''} dt''\\
\end{aligned}
\tag{5}
$$

noting that:
$$\left|Q_{s,j}\right|^2\omega_s^2=k_BT$$
where $k_B$ is the Boltzmann constant and $T$ is temperature, we get:

$$
\begin{aligned}
|v_j(\omega)|^2 &= k_B T \sum_s \int_{-\infty}^{\infty} e^{i(\omega+\omega_s)t''} dt''\\
&= k_B T \sum_s \delta(\omega+\omega_s).
\end{aligned}
$$

If we add contributions from all atoms together:

$$
\sum_j |v_j(\omega)|^2 = 3N k_B T \sum_s \delta(\omega+\omega_s)
$$

remember that the phonon DOS is expressed as
$$\sum_s \delta(\omega_s-\omega)$$, we can write phonon DOS as:

$$
\rho(-\omega) = \sum_s \delta(\omega-\omega_s) = \frac{1}{3Nk_BT} \sum_j |v_j(-\omega)|^2
$$

by the knowledge of Fourier transform of the time-dependent velocity function in Eq. 3, we get:

$$
\rho(-\omega) = \frac{1}{3Nk_BT}\ \sum_j \int_{-\infty}^{\infty}  \int_{-\infty}^{\infty} v^*_j(t''+t') v_j(t') e^{-i\omega(t'')} dt'' dt'
\tag{6}
$$

Finally, the velocity autocorrelation function tells us how the velocity is changing over time and can be written as:

$$
C_{v}(t) = \int_{-\infty}^{\infty} \vec v(t'+t)\cdot \vec v(t')dt'
$$

or, in a more compact way:

$$
C_{v}(t) = \braket{\vec v(t'+t)\cdot \vec v(t')}.
\tag{7}
$$

Inserting Eq. 7 into Eq. 6, we get:

$$
\rho(-\omega) = \frac{1}{3Nk_BT}\ \sum_j \int_{-\infty}^{\infty} \braket{v_j(t''+t')\cdot v_j(t')} e^{-i\omega(t'')} dt''
$$

for convenience, we can set $t'=0$ since the starting time is arbitrary in our MD calculation and we can always set $t'$ as the "median time":

$$
\rho(-\omega) = \frac{1}{3Nk_BT}\ \sum_j \int_{-\infty}^{\infty} \braket{\vec v_j(t'')\cdot \vec v_j(0)} e^{-i\omega(t'')} dt''.
\tag{8}
$$

With Eq. 8, noting the decreasing nature of the velocity autocorrelation function and the fact that the integral always converges, we see that if we have the knowledge of the velocity of each atom across a period of time (since we cannot do infinity, a long period of time will do), we can calculate the phonon density of states.

Code, Coming soon...
