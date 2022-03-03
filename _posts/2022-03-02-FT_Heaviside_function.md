---
layout: post
title: Fourier transform Heaviside step function
date: 2022-03-02
categories: Post
description: Fourier transform Heaviside step function.
tags: Math
---

The definition of Heaviside step function is [:link:](https://mathworld.wolfram.com/HeavisideStepFunction.html):

$$
\theta(x)= \begin{cases}0 & x<0 \\ \frac{1}{2} & x=0 \\ 1 & x>0\end{cases}
$$

It can be written as (If we substitute $x$ with $t-t'$ as we'll be using them in time ordering operator):

$$
\theta\left(t-t^{\prime}\right)=-\frac{1}{2 \pi i} \lim_{\eta \rightarrow 0^+}\int_{-\infty}^{\infty} d \omega \frac{e^{-i \omega (t-t^{\prime})}}{\omega+i \eta} \tag{1}
$$

To show this relation is correct, we need to use the [:link: The Sokhotski-Plemelj formula](../01/Sokhotski_Plemelj_Formula.html):

$$
\lim _{\epsilon \rightarrow 0} \int_{-\infty}^{\infty} \frac{f(x) d x}{x \pm i \epsilon}=\mathcal{P} \int_{-\infty}^{\infty} \frac{f(x) d x}{x} \mp i \pi f(0)
$$

and Eq. 1 turns into:

$$
\begin{aligned}
\theta\left(t-t^{\prime}\right)&=-\frac{1}{2 \pi i} \lim_{\eta \rightarrow 0^+}\int_{-\infty}^{\infty} d x \frac{e^{-i x\left(t-t^{\prime}\right)}}{x+i \eta}\\
&= -\frac{1}{2 \pi i}  \left [ \mathcal{P} \int_{-\infty}^{\infty} \frac{ e^{-i x (t-t^{\prime})} d x}{x}  - i \pi \right]
\end{aligned} \tag{2}
$$

expanding the tems inside the braket:

$$
\begin{aligned}
& \mathcal{P} \int_{-\infty}^{\infty} \frac{ e^{-i x (t-t^{\prime})} d x}{x}  - i \pi \\
=& \lim_{\delta \rightarrow 0} \left \{ \int_{-\infty}^{-\delta} \frac{ e^{-i x (t-t^{\prime})} d x}{x} + \int_{\delta}^{\infty} \frac{ e^{-i x (t-t^{\prime})} d x}{x}\right \}  -i \pi \\
=& \lim_{\delta \rightarrow 0} \left \{ \int_{-\infty}^{-\delta} \frac{ \cos[x (t-t^{\prime})] - i \sin[x (t-t^{\prime})]}{x}dx + \int_{\delta}^{\infty} \frac{ \cos[x (t-t^{\prime})] - i \sin[x (t-t^{\prime})]}{x}dx  \right \} -i\pi\\
\end{aligned}
$$

Becasue $\cos$ is odd, two $\cos$ within the first and second integral vanishes, and in the limit of $\delta \rightarrow 0$ we can combine the $\sin$ terms, giving us:

$$
\begin{aligned}
& \mathcal{P} \int_{-\infty}^{\infty} \frac{ e^{-i x (t-t^{\prime})} d x}{x}  - i \pi \\
=&- i  \int_{-\infty}^{\infty} \frac{  \sin[x (t-t^{\prime})]}{x}dx  -i \pi \\
\end{aligned} \tag{3}
$$

Note that the integral can be re-written as:

$$
\int_{-\infty}^{\infty} \frac{  \sin[x (t-t^{\prime})]}{x}dx = \mathrm{Si} (x[t-t^{\prime})] \big \vert_{x=-\infty}^{x=\infty} = \int_{0}^{x(t-t^{\prime})} \frac{  \sin(\omega)}{\omega} d\omega \big \vert_{x=-\infty}^{x=\infty}
$$

where $\mathrm{Si}$ is the [sine integral](https://mathworld.wolfram.com/SineIntegral.html).

Assuming we have $t-t' > 0$ we have:

$$
\int_{-\infty}^{\infty} \frac{  \sin[x (t-t^{\prime})]}{x}dx =\int_{0}^{x(t-t^{\prime})} \frac{  \sin(\omega)}{\omega} d\omega \big \vert_{x=-\infty}^{x=\infty} = \pi
$$

So that Eq. 3 is:

$$
\mathcal{P} \int_{-\infty}^{\infty} \frac{ e^{-i x (t-t^{\prime})} d x}{x}  - i \pi = 0 \tag{4}
$$

and if $t-t' < 0$ we have:

$$
\int_{-\infty}^{\infty} \frac{  \sin[x (t-t^{\prime})]}{x}dx =\int_{0}^{x(t-t^{\prime})} \frac{  \sin(\omega)}{\omega} d\omega \big \vert_{x=-\infty}^{x=\infty} =- \pi
$$

So that Eq. 3 is:

$$
\mathcal{P} \int_{-\infty}^{\infty} \frac{ e^{-i x (t-t^{\prime})} d x}{x}  - i \pi = -2i\pi \tag{5}
$$

and if $t-t' = 0$ we have:

$$
\int_{-\infty}^{\infty} \frac{  \sin[x (t-t^{\prime})]}{x}dx =\int_{0}^{x(t-t^{\prime})} \frac{  \sin(\omega)}{\omega} d\omega \big \vert_{x=-\infty}^{x=\infty} = 0
$$

So that Eq. 3 is:

$$
\mathcal{P} \int_{-\infty}^{\infty} \frac{ e^{-i x (t-t^{\prime})} d x}{x}  - i \pi = -i\pi \tag{6}
$$

Multiply Eq. 4, 5 and 6 with $\frac{-1}{i 2 \pi}$ gives Eq. 2:

$$
\theta(t-t')= \begin{cases}0 & t-t'<0 \\ \frac{1}{2} & t-t'=0 \\ 1 & t-t'>0\end{cases}
$$
