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

Previosly, we have looked at the quantum TD-LRT, now let us put that into action by consider an perturbation that has a oscillatory time-dependence (typical of interaction with radiation) which can be written in the form of:

$$
V(t) = V e^{-i\omega t} + V^\dagger e^{i\omega t} 
$$

This form explicitly enforces the perturbation to be hermitian.

Then the relevant transition matrix element is:

$$
V_{fi}(t) = \braket{f|V(t)|i}e^{-i\omega t} + \braket{f|V^\dagger(t)|i} e^{i\omega t} 
$$

Eq. 8 in [:link:quantum TD-LRT](./TD_LRT.html) becomes
Eq. 8 in [quantum TD-LRT](:/264f8a38608c4aa2944dc01b376e6a0d) becomes

$$
\begin{aligned}
{c}_f(t) = {c}_f(t)^{(1)} &=  \frac{V_{fi}}{i\hbar}  \left[  \int_{0}^t \delta t' e^{i(\omega_{fi}-\omega)t'} +   \int_{0}^t\delta t' e^{i(\omega_{fi}+\omega)t'} \right ]\\
&=\frac{V_{fi}}{i\hbar} \frac{e^{i(\omega_{fi}-\omega)t}-1}{i(\omega_{fi}-\omega)} + \frac{V_{fi}}{i\hbar} \frac{e^{i(\omega_{fi}+\omega)t}-1}{i(\omega_{fi}+\omega)} 
\end{aligned}
$$

Here, let's make an assumption that the final state lives higher in energy than the initial state (ie.e., $\omega_f > \omega_i$), hence  $\omega$ is close to $\omega_{fi}$ (which is called the Bohr angular frequency of $\ket{f}$ and $\ket{i}$). In this case, we are effectively considering an absorption process where the perturbation energy is being absorbed. Because of this we can safely ignore the second term which only has big contribution when we are studying stimulated emission process (i.e., final state has lower energy than the initial state).

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

{% include admonition.html type="note" title="Nascent Dirac delta function" body="
The equation 

$$
F(\omega_{fi}-\omega,t)=\left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2
$$

peaks at $\omega_{fi}$ with a width of $\Delta \omega$,


where $\Delta \omega \approx \frac{4pi}{t}$. 
We see that as $t \to \infty$, this becomes a delta function.

However, this function has a different normalization comparing to a delta function: 

$$
\int \left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2 \hbar d \omega = \hbar (\frac{2}{t}) t^2 \int \frac{\sin^2(x)}{x^2} d x =2 \pi \hbar t
$$
" %}
<!-- <div> -->
<!--   <img src="../../../assets/img/post_img/2025-11-05-img1.png" alt="image"/> -->
<!-- </div> -->

Converting using Nascent Dirac delta function, we get

$$
P_{i\to f}(t,\omega) = |{c}_f(t)^{(1)}|^2 = \frac{|V_{fi}|^2}{\hbar^2} 2 \pi \hbar t \delta(\omega_{fi}-\omega) = \frac{2 \pi}{\hbar} |V_{fi}|^2 t \delta(\omega_{fi}-\omega)
$$

And the transition rate (probability per unit time) is

$$
W_{i\to f} = \frac{\delta P_{i\to f}(t,\omega)}{\delta t}= \frac{2 \pi}{\hbar} |V_{fi}|^2 \delta(\omega_{f} - \omega_i-\omega)
$$

Which is the Fermi's Golden Rule.

### Phase of the perturbation
Since here we are integrating from $0$ to $t$, we can imagine that if we switch the perturbation from $\cos$ vs $\sin$, we *should* get a different result. Let's now show how this will actually not affect the final conclusion.

Recalling that the resonant contribution to the amplitude ${c}_f(t)$ is:

$$
{c}_f(t) = \int_0^te^{i(\omega_{fi}-\omega) t’} =\frac{e^{i(\omega_{fi}-\omega) t} − 1}{i(\omega_{fi}-\omega)}
$$

The transition probability is:

$$
P_{i\to f}(t) = |{c}_f(t)|^2 \propto \left [\frac{\sin^2((\omega_{fi}-\omega) t/2)}{(\omega_{fi}-\omega)/2}\right]^2.
$$

But what happens if we switch from the cosine perturbation to a sine one? Remembering that:

$$
\begin{aligned}
\sin(\omega t) = \frac{1}{2i}(e^{i\omega t} − e^{-i\omega t})\\
\cos(\omega t) = \frac{1}{2} (e^{i\omega t} + e^{-i\omega t})
\end{aligned}
$$

so the only difference caused by this switching is a $1/i$ factor and a sign switch.

Still only taking the resonance term $e^{-i\omega t}$, the amplitude in the $\sin$ case would be come

$$
{c}_f(t)^{\sin} = i {c}_f(t)^{\cos}  \propto i \int_0^t e^{i(\omega_{fi}-\omega)t'} dt' =  \int_0^t  e^{i(\omega_{fi}-\omega)t'+\pi/2} dt'
$$

{% include admonition.html type="note" title="Note: Identity" body="
$$
i e^{i(\omega_{fi}-\omega)t'} = e^{i\left[ (\omega_{fi}-\omega)t'+\pi/2\right]}
$$
" %}

hence if we switch to from $\cos$ to $\sin$, after taking the mod square of ${c}_f(t)$, we get

$$
P_{\sin}(t) = 4 \sin^2[(\Omega t − \pi)/2]/\Omega^2.
$$

Comparing to 

$$
P_{\cos}(t) = 4 \sin^2((\Omega t)/2)/\Omega^2,
$$

we see that they differ for finite $t$. But in the long‑time rate limit (i.e., $t \to \infty$):

$$
\frac{\delta P_{\sin}(t)}{\delta t} \to 2\pi \delta(\Omega)\\
\frac{\delta P_{\cos}(t)}{\delta t} \to 2\pi \delta(\Omega)
$$

because shifting the phase of $\Omega t$ inside the sine does not change the long‑time $\delta$-function limit.

So although amplitudes differ and finite‑time probabilities differ, the rate is identical.

The phase of the perturbation ($\sin$ vs $\cos$) matters to the amplitude ${c}_f(t)$ because we turn on the perturbation at $t_0=0$ so it is a non-adiabatic perturbation, as we integrate the amplitude when from $0$ to $t$. If the perturbation is turned on adiabatically from the distant past, we integrate form $\infty$ to $t$ and this phase gets canceled directly when we calculate the transition probability (mode square of the $c$ coefficients), even before we push $t$ to $\infty$.

<!-- The result of these two ways matches each other when we set $t \to \infty$ because then they are essentially the same -->

## State decay (phenomenological)
If a state has finite lifetime $\tau$, meaning its survival amplitude decays:

$$
\ket{\psi(t)} = e^{-iEt/\hbar} e^{-\Gamma t/2\hbar} \ket{\phi}, \quad \Gamma=\hbar/\tau
$$

This corresponds to having a complex energy

$$
E \to E-i\frac{\Gamma\hbar}{2}
$$

A state with a complex energy is not a stationary state — therefore it is not an eigenstate of the Hamiltonian, and does not have exact energy.

In standard Fermi’s Golden Rule, 

$$
{c}_f(t) \propto \delta(\omega_f - \omega_i -\omega)
$$

where we have strict energy conservation condition from the delta function.

But with finite lifetimes, $E_i$ is replaced by

$$
E_i - i\Gamma_i\hbar/2.
$$

and the ${c}_f(t)$becomes: 
<!-- delta function becomes a Lorentzian: -->

$$
\begin{aligned}
{c}_f(t) &\propto \int_0^t e^{-i(E_i-i\Gamma_i\hbar/2)/\hbar t'} e^{iE_f/\hbar t'} e^{-i\omega t'}  dt' \\
&= \int_0^te^{i\omega_{fi} t'} e^{-\Gamma_i t'/2} e^{-i\omega t'}  dt'\\
&= \frac{e^{i(\omega_{fi}-\omega)t-\Gamma_i t/2}-1}{i(\omega_{fi}-\omega)-\Gamma_i/2} 
\end{aligned}
$$

Taking $t\to\infty$, $e^{i(\omega_{fi}-\omega)t}e^{-\Gamma_i t/2}$ vanishes as $e^{-\Gamma_i t/2} \to 0$, and we are left with 

$$
\begin{aligned}
{c}_f(\infty) \propto \frac{-1}{i(\omega_{fi}-\omega)-\Gamma_i/2 } 
\end{aligned}
$$

and the  transition probability is proportional to a lorentzian:

$$
P_{i\to f}(t) = |{c}_f(t)|^2 \propto \frac{\Gamma_i/2}{(\omega_{fi}-\omega)^2 + \left( \frac{\Gamma_i}{2}\right)^2 } = L(\omega;\omega_{fi},\Gamma/2)
$$

You can test and see that the Lorentzian becoms a delta function as $\Gamma_i$ goes to zero.

This expresses exactly what happens physically:
- Due to the finite life time of states, transitions don’t require perfect energy match.
- They occur most strongly near resonance, but with a width determined by the sum of lifetimes.



## Continuum 
Assuming that the final state lives in a continuum of states, we need to account for all  states the system can jump into using

$$
\begin{aligned}
P_{i}(t,\omega)  &=  \int P_{i\to f}(t,\omega) \rho_f(E) dE\\
&= \int  \frac{|V_{fi}|^2}{\hbar^2} \left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2 \rho_f(E) dE\\
&= \int  \frac{2\pi}{\hbar^2} |V_{fi}|^2 \delta(\omega_{fi}-\omega) t \rho_f(E) dE\\
&= \int  \frac{2\pi}{\hbar^2} |V_{fi}|^2 \delta(\omega_{fi}-\omega)  \rho_f(\hbar \omega)  t \hbar d\omega\\
&= \frac{2\pi}{\hbar} |V_{fi}|^2 \rho_f(\hbar \omega_{fi}) t
\end{aligned}
$$

<!-- since $F(\omega_{fi}-\omega,t)$ acts as a delta function, we can extract $\rho(E)$ as $\rho(E_{fi})$
$$
\begin{aligned}
P_{i}(t)  &= \int  \frac{|V_{fi}|^2}{\hbar^2} \left[\frac{\sin(\frac{(\omega_{fi}-\omega) t}{2})}{(\omega_{fi}-\omega)/2}\right]^2 \rho_f(E) dE\\
&= \frac{2\pi}{\hbar}|V_{fi}|^2 \rho_f(E_{fi}) t
\end{aligned}
$$ -->

And the transition rate (unit time transition probability) is:

$$
W =\frac{\delta P_{i}(t,\omega)}{\delta t} = \frac{2\pi}{\hbar}|V_{fi}|^2 \rho_f(E_{fi})
$$

Which is the Fermi's Golden Rule in continuum states.


