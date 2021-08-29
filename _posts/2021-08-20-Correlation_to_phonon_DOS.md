---
layout: post
title: From velocity autocorrelation function to phonon DOS
date: 2021-08-20
categories: Post
description: Derivation of how to calculate phonon DOS from autocorrelation functions.
tags: MD Phonon
---

The autocorrelation function is a cross-correlation function that shows the correlation of one signal (function) with a delayed version of it self.

To derive the relation between velocity autocorrelation function and the phonon density of states, let us first start with the Fourier transforming the velocity of an atom $i$, $v_i(t)$.

$$
\mathcal{F}[v_i(t)](\omega) = \int_{-\infty}^{\infty}v_i(t)e^{i\omega t} dt,
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

Note that the exponential $e^{i\omega t}$ in Eq. 1 doesn't contain a minus sign.
This is just a difference in convention, if we put in the minus sign, then
$$v^*_i(t''+t')$$
in Eq. 3 would become
$$v^*_i(-t''+t')$$.
However, this does not affect any of the following analysis.

Before moving on, let's assume that harmonic approximation is valid (which, in theory, we should have zero-width phonon branches), the atomic displacement with respect to time can be written as:

$$
r_j(t) = \sum_s Q_{s,j} e^{-i\omega_s t},
$$

where $s$ labels the phonon branch and $j$ is a composite index for the vibrations of atom $i$ on three spacial directions.
Q is the amplitude of the vibration (with $\sqrt{\frac{1}{2} m_j}$ absorbed in) and $\omega$ is the frequency of the phonon mode.

With the time-dependent displacement derived, the time-dependent velocity can be expressed as:

$$
v_j(t) = \frac{d}{dt} r_j(t) = \sum_s Q_{s,j} (-i\omega_s) e^{-i\omega_s t}.
\tag{4}
$$

Inserting Eq. 4 to Eq. 3, and notice we are now using $j$ instead of $i$ to incorporate three spacial dimensions, we get:

$$
\begin{aligned}
|v_j(\omega)|^2 &= \int_{-\infty}^{\infty}  \int_{-\infty}^{\infty} \sum_{s,s'} Q^*_{s,j}(i\omega_s)e^{i\omega_s(t''+t')} Q_{s',j} (-i\omega_s') e^{-i\omega_{s'} t'} e^{i\omega t''} dt'' dt'\\
&= \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} \sum_{s,s'} Q^*_{s,j}Q_{s',j}(\omega_s \omega_{s'})e^{i(\omega+\omega_s)t''} e^{i(\omega_s - \omega_{s'})t'} dt'' dt'\\
&= \int_{-\infty}^{\infty} \sum_{s,s'} Q^*_{s,j}Q_{s',j}(\omega_s \omega_{s'})e^{i(\omega+\omega_s)t''} \delta(\omega_s - \omega_{s'}) dt''\\
&= \sum_s \int_{-\infty}^{\infty} |Q_{s,j}|^2 \omega_s^2  e^{i(\omega+\omega_s)t''} dt''\\
\end{aligned}
\tag{5}
$$

noting that, due to [:link: equipartition theorem](https://en.wikipedia.org/wiki/Equipartition_theorem), the total energy of an oscillator is $k_BT$ where $k_B$ is the Boltzmann constant and $T$ is temperature.
Since we can express the total energy as pure kinetic energy at the equilibrium position, we get:

$$
E_{\text{tot}} = E_{\text{kin}} = \frac{1}{2} m v^2 = Q^2 \omega^2  = k_BT.
$$

Substituting
$$|Q_{s,j}|^2 \omega_s^2$$
with $k_BT$, Eq. 5 becomes:

$$
\begin{aligned}
|v_j(\omega)|^2 &= k_B T \sum_s \int_{-\infty}^{\infty} e^{i(\omega+\omega_s)t''} dt''\\
&= k_B T \sum_s \delta(\omega+\omega_s).
\end{aligned}
$$

If we add contributions from all atoms (assuming there are $N$ atoms) in all three directions:

$$
\sum_j |v_j(\omega)|^2 = 3N k_B T \sum_s \delta(\omega+\omega_s)
$$

remember that the phonon DOS is expressed as
$$\sum_s \delta(\omega_s-\omega)$$, we can write phonon DOS as:

$$
\rho(-\omega) = \sum_s \delta(\omega_s-\omega) = \frac{1}{3Nk_BT} \sum_j |v_j(-\omega)|^2
$$

by the knowledge of Fourier transform of the time-dependent velocity function in Eq. 3, we get:

$$
\rho(-\omega) = \frac{1}{3Nk_BT}\ \sum_j \int_{-\infty}^{\infty}  \int_{-\infty}^{\infty} v^*_j(t''+t') v_j(t') e^{-i\omega(t'')} dt'' dt'.
\tag{6}
$$

Remembering that the system is at its equilibrium state and the velocity signal is more or less periodic.
For this reason, the following integral diverges:
<!-- Finally, the velocity autocorrelation function, which tells us how the velocity is changing over time, can be written as: -->

$$
\int_{-\infty}^{\infty} \vec v(t+t')\cdot \vec v(t')dt'
$$

Noting that the DOS function is a Dirac delta function, at $\omega = \omega_s$, the the DOS should indeed diverge.
However, since we only care about the difference of the $\rho$ with different $\omega$s in our final plots, instead of using the Fourier transform, we can re-write the integral as:

<!-- we have to use the discrete Fourier transform in Eq. 1.
Assuming we have N time points, we can write: -->

$$
\frac{1}{N_{t'}} \sum_{t'=0}^{N_{t'}} \vec v(t+t')\cdot \vec v(t'),
$$

where, $N_{t^{\prime}}$ is the number of time points we have.
This expression can also be seen as an averaged velocity autocorrelation function:

$$
\begin{aligned}
C_{v}(t) &= \frac{1}{N} \sum_{t'=0}^N \vec v(t+t')\cdot \vec v(t')\\
&= \braket{\vec v(t)\cdot \vec v(0)}
\end{aligned}
\tag{7}
$$

Alternatively, we can re-normalize this autocorrelation function by doing something like:

$$
C_{v}(t) = \frac{\braket{\vec v(t)\cdot \vec v(0)}}{\braket{\vec v(0)\cdot \vec v(0)}},
$$

Which, normalizes the maximum correlation to $1$.
This is what you see in, e.g. [:link: 10.1016/j.cpc.2011.04.019](https://www.sciencedirect.com/science/article/pii/S0010465511001500) or, [:link: 10.1039/c8nr07373b](https://pubs.rsc.org/en/content/articlelanding/2018/nr/c8nr07373b).

Inserting Eq. 7 into Eq. 6, we get:

<!-- $$
\rho(-\omega) = \frac{1}{3Nk_BT}\ \sum_j \int_{-\infty}^{\infty} \braket{v_j(t''+t')\cdot v_j(t')} e^{-i\omega(t'')} dt''.
$$

For convenience, we can set $t'=0$ since the starting time of a MD calculation is arbitrary and we can always set $t'$ as the "median" of the time period that we run: -->

$$
\rho(\omega) = \frac{1}{3Nk_BT}\ \sum_j \int_{-\infty}^{\infty} \braket{v_j(t'')\cdot v_j(0)} e^{i\omega(t'')} dt''.
\tag{8}
$$

With Eq. 8, noting the decreasing nature of the velocity autocorrelation function so that the integral always converges, we see that if we have the knowledge of the velocity of each atom across a period of time (since we cannot do infinity, a we need to have a cut-off time for the integral), we can calculate the phonon density of states.

In practice, Eq. 8 should be rewrite in a discrete form as:

$$
\rho(\omega) = \frac{1}{3Nk_BT}\ \sum_j \frac{1}{N_{t''}} \sum_{t''=0}^{N_{t''}} \braket{v_j(t'')\cdot v_j(0)} e^{i\omega(t'')}.
\tag{9}
$$

<!-- and $\omega$ can only be integer times of $\frac{2\pi}{N_{t^{\prime \prime}}}$. -->


---

For periodic systems, the phonon bandstructure can also be interpreted as phonon DOS at each $k$ point.
To obtain this "spectrum" function. we need to Fourier transform the velocity function with respect to the unit cell vectors.
For example, lets say we have calculated a $\sqrt[3]{N}\times\sqrt[3]{N}\times\sqrt[3]{N}$ supercell (so that we have a total of $N$ unit cells):

![]({{site.baseurl}}/assets/img/post_img/2021-08-20-img1.png){:height="70%" width="70%" .center}

Here, we label the atoms in each cell with $j$ (again a composite label with three direction added) and the unit cell position is expressed as $\vec R$ so that the velocity of atom $j$ at cell $\vec R$ (in three direction) is:

$$
v_{j}(\vec R, t).
\tag{10}
$$

Fourier (discrete) transform Eq. 9 with respect to $\vec R$, we get:

$$
\begin{aligned}
\mathcal{F}[v_{j}(\vec R, t)](\vec k,t) = \frac{1}{\sqrt{N}} \sum_{\vec R} v_j(\vec R,t) e^{i\vec k \vec R} = v_{j}(\vec k, t),
\end{aligned}
\tag{11}
$$

where we have $N$ unit cell in the supercell.


Using Eq. 10, we can express the phonon DOS at each $\vec k$ point as:

$$
\rho(\vec k, -\omega) = \frac{1}{3Nk_BT}\ \sum_j \int_{-\infty}^{\infty} \braket{v_{j}(\vec k, t'')\cdot v_{j}(\vec k, 0)} e^{-i\omega(t'')} dt''.
\tag{12}
$$

---

## Physical explanation

Okay, the derivation is nice and easy, but what's the physics behind?

Let's consider a single atom that's vibrating at its equilibrium position.
Its velocity vs time can be plotted as:

![]({{site.baseurl}}/assets/img/post_img/2021-08-20-img2.svg){:height="70%" width="70%" .center}

The autocorrelation function $v(t+t^{\prime})v(t^{\prime})$ of this velocity signal at different $t$ is (different colors indicate different $t$s):

![]({{site.baseurl}}/assets/img/post_img/2021-08-20-img3.svg){:height="70%" width="70%" .center}

If we do an average of the autocorrelation by integrating from $0$ to $2\pi$ in time, likewhat we did in Eq. 7, we get:

![]({{site.baseurl}}/assets/img/post_img/2021-08-20-img4.svg){:height="70%" width="70%" .center}

It can be clearly seen that after exactly one period, the correlation is back at it's maximum.
Fourier transforming this averaged velocity autocorrelation function gives exactly the intrinsic vibrating frequency of this vibration mode.

---
I have wrote a piece of [:link: code]({{site.baseurl}}/assets/other/2021-08-20-MD_phonon.tar.gz) trying to implement this with velocity files produced by lammps,
but I have ran out of vacation time and the code is not working...
hopefully I'll get time to finish in the future.
