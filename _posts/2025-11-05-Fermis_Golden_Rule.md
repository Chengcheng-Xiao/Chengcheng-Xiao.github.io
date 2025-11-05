---
layout: post
title: Fermi's Golden Rule
date: 2025-11-04
categories: Post
description: A simple derivation of Fermi's Golden Rule.
tags: DFT, Math
---

{% include admonition.html type="quote" title="References" body="
Ref: http://staff.ustc.edu.cn/~yuanzs/teaching/Fermi-Golden-Rule-No-II.pdf
" %}

Previosly, we have looked at the quantum TD-LRT, now let us put that into action by consider an perturbation that has a harmonic time-dependence (typical of interaction with radiation):

$$
V(t) = V e^{-i\omega t} + V^\dagger e^{i\omega t} 
$$

Then the relevant transition matrix element is:

$$
V_{fi}(t) = \braket{f|V(t)|i}e^{-i\omega t} + \braket{f|V^\dagger(t)|i} e^{i\omega t} 
$$

Eq. 5 in [:link:quantum TD-LRT](./TD_LRT.html) becomes

$$
\begin{aligned}
{c}_f(t) = {c}_f(t)^{(1)} &=  \frac{V_{fi}}{i\hbar}  \int_{t_0}^t \delta t' e^{i(\omega_{fi}-\omega)t'} +   \int_{t_0}^t\delta t' e^{i(\omega_{fi}+\omega)t'} \\
&=\frac{V_{fi}}{i\hbar} \frac{e^{i(\omega_{fi}-\omega)t}-1}{i(\omega_{fi}-\omega)} + \frac{V_{fi}}{i\hbar} \frac{e^{i(\omega_{fi}+\omega)t}-1}{i(\omega_{fi}+\omega)} 
\end{aligned}
$$

Here, let's make an assumption that $\omega$ is close to $\omega_fi$ (which is called the Bohr angular frequency of $\psi_f$ and $\psi_i$). In this case, the first term dominates and we can safely ignore the second term.

<!-- Let's focus on the first term first (it represent the absorption process, and this derivation only works when $\omega_{fi}$ is much smaller than $t$, i.e., the excitation is in a steady state),  -->

$$
\begin{aligned}
{c}_f(t) = {c}_f(t)^{(1)}&= \frac{V_{fi}}{i\hbar} \frac{e^{i(\omega_{fi}-\omega)t}-1}{i(\omega_{fi}-\omega)} \\
&= \frac{V_{fi}}{i\hbar} \frac{e^{i(\omega_{fi}-\omega)t/2}(e^{i(\omega_{fi}-\omega)t/2}-e^{-i(\omega_{fi}-\omega)t/2})}{i(\omega_{fi}-\omega)}\\
&= \frac{V_{fi}}{i\hbar} \frac{e^{i(\omega_{fi}-\omega)t/2}(2i\sin(\frac{\omega_{fi}-\omega t}{2}))}{i(\omega_{fi}-\omega)}\\
&= \frac{V_{fi}}{i\hbar} \frac{e^{i(\omega_{fi}-\omega)t/2}\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\\
\end{aligned}
$$

The corresponding transition probability is

$$
P_{i\to f}(t) = |{c}_f(t)^{(1)}|^2 = \frac{|V_{fi}|^2}{\hbar^2} \left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2
$$

!!! note Nascent Dirac delta function

The equation 

$$
F(\omega_{fi}-\omega,t)=\left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2
$$

behaves peaks at $\omega_{fi}$ with a width of $\Delta \omega$:
![]({{site.baseurl}}/assets/img/post_img/2025-11-05-img1.png){:height="50%" width="50%" .center}
where $\Delta \omega \approx \frac{4pi}{t}$. We see that as $t \to \infty$, this becomes a delta function.

However, this function has a different normalization comparing to a delta function: 

$$
\int \left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2 \hbar d \omega = \hbar (\frac{2}{t}) t^2 \int \frac{\sin^2(x)}{x^2} d x =2 \pi \hbar t
$$

!!!

Converting using Nascent Dirac delta function, we get

$$
P_{i\to f}(t) = |{c}_f(t)^{(1)}|^2 = \frac{|V_{fi}|^2}{\hbar^2} 2 \pi \hbar t \delta(\omega_{fi}-\omega) = \frac{2 \pi}{\hbar} |V_{fi}|^2 t \delta(\omega_{fi}-\omega)
$$

And the transition rate is

$$
W_{i\to f} = P_{i\to f}(t)/t= |{c}_f(t)^{(1)}|^2 = \frac{2 \pi}{\hbar} |V_{fi}|^2 \delta(\omega_{f} - \omega_i-\omega)
$$

Which is the Fermi's Golden Rule


## Continuum 
Assuming that the final state lives in a continuum of states, we need to account for all  states the system can jump to using

$$
\begin{aligned}
P_{i}(t)  &=  \int P_{i\to f}(t) \rho(E) dE\\
&= \int  \frac{|V_{fi}|^2}{\hbar^2} \left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2 \rho_f(E) dE\\
\end{aligned}
$$

since $F(\omega_{fi}-\omega,t)$ acts as a delta function, we can extract $\rho(E)$ as $\rho(E_{fi})$

$$
\begin{aligned}
P_{i}(t)  &= \int  \frac{|V_{fi}|^2}{\hbar^2} \left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2 \rho_f(E) dE\\
&= \frac{2\pi}{\hbar}|V_{fi}|^2 \rho_f(E_{fi}) t
\end{aligned}
$$

And the transition rate is:

$$
W = P_{i}(t) /t = \frac{2\pi}{\hbar}|V_{fi}|^2 \rho_f(E_{fi})
$$

Which is the Fermi's Golden Rule in continuum.

