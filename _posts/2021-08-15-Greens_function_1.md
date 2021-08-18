---
layout: post
title: Green's function (part I)
date: 2021-08-15
categories: DFT
description: Classical green's function, revisited.
---

Green's function method is a way to decompose a complex inhomogenous source using Dirac delta functions and then combine individually solutions to obtain the true answer.

## Preconditions

Green's function is a solution to a <span class="yellow">linear</span> differential equation with a <span class="yellow">Dirac delta function as the inhomogeneous source</span> and the additional requirement of the <span class="yellow">boundary condition being homogenous</span>.

To clarify, by <span class="yellow">homogenous/inhomogeneous</span>, we mean $\textit{something}=0$ . For example, a differential equation is said to be inhomogeneous if $g(x)$ in the following equation does not equals to $0$, homogeneous otherwise:

$$
\hat{D} f(x) = g(x)
$$

Similarly, the boundary condition is said to be homogeneous only if it specify the value (or the value of the derivative) of the function on the boundary to be $0$. i.e.

$$
f(x=L) = 0 \text{ or } f'(x=L) = 0
$$

On the other hand, by <span class="yellow">linear</span>, we mean no coupling between operators with different derivative order. i.e. no product of function and its derivatives, such as $f(x) \cdot f'(x)$.

Overall, the differential equation should look like:

$$
a_1(x)f(x) + a_2(x)f'(x) + \cdots + a_n(x)f^{n}(x) = g(x) = \delta (x-x'),
\tag{1}
$$

or, we can put all operation into an operator and write Eq. 1 as:

$$
\hat{D} f(x) = g(x) = \delta(x-x')
\tag{2}
$$

where $\hat{D} = a_1(x)+a_2(x)\frac{d}{dx} + \cdots + a_n(x)(\frac{d}{dx})^n$. Since there are no coupling between different order of differentiation, we call this operator a __linear operator__. The linearity is essential to the superposition theory that we are so used to in quantum mechanics that we've just taken it for granted.

## Deriving of Green's function method

Now, how do we apply this particular solution of a particular differential equation to solve all those general questions?
More importantly, what kinds of <span class="yellow">general</span> differential equations can be solved using this method?
Like I said in the beginning, the essence of this method is that it breaks down the complex inhomogeneous source using Dirac delta functions.
This means that we can have any continuous complex inhomogeneous source in our <span class="yellow">general</span> differential equations, but we still need the operator to be linear.
i.e.:

$$
\hat{D} f(x) = g(x)
\tag{3}
$$

where, $g(x)$ is a general continuous function.

$g(x)$ can be expressed (decomposed) using a infinite set of Dirac delta functions with weights as:

$$
g(x) = \int_{-\infty}^{\infty} \delta (x'-x) g(x') dx'
\tag{4},
$$

where, each Dirac delta function (more appropriately, unit pulse) takes one value from $g(x')$. Or this can be interpreted as each unit pulse (located at $x$) has a weight of $g(x)$.

By plugging Eq. 4 into Eq. 3, we get:

$$
\hat{D} f(x) = g(x) = \int_{-\infty}^{\infty} \delta (x'-x) g(x') dx'.
\tag{5}
$$

Note that Green's function is the solution to the equation:

$$
\begin{aligned}
\hat{D} G(x) &= \delta (x-x') \tag{6}\\
\end{aligned}.
$$

<!-- Here we rewrite $f(x)$ as $G(x)$ to differentiate Green's function to the final solution of our general differential equations. -->
Plug Eq. 6 to Eq. 5 (note that we've swapped $x$ and $x'$), we get:

$$
\hat{D} f(x) = \int_{-\infty}^{\infty} \hat{D} G(x')  g(x') dx',
\tag{7}
$$

and since $\hat{D}$ is a linear operator, the final solution to Eq. 3 is:

$$
f(x) = \int_{-\infty}^{\infty}G(x') g(x') dx'.
\tag{8}
$$

Note that to get the particular solution, we also need to add the general solution of homogeneous equation:

$$
\hat{D} f(x) = 0
$$

to the solution in Eq. 8.

Now, things are much clearer: The green's function is to be viewed as the building block of the particular solution since it decomposes the inhomogeneous source using Dirac functions.

## Practical example

To get a taste of how the whole process works, let's consider solving the Poisson equation with Green's function method!
The Poisson equation relates the electrical potential to the charge density through:

$$
\nabla^2 \psi(\vec r) = - \frac{\rho(\vec r)}{\epsilon_0}
\tag{9}
$$

in a non-periodic system, we have the boundary condition:

$$
\psi(\vec r \rightarrow \infty) = 0
$$

substituting $g(x)$ in Eq. 8 with $-\frac{\rho(\vec r)}{\epsilon_0}$, we get:

$$
\psi(\vec r) = \int G(\vec r, \vec r') \rho(\vec r) d \vec r',
\tag{10}
$$

where $G(\vec r, \vec r')$ satisfies:

$$
\nabla^2 G(\vec r, \vec r') = - \frac{1}{\epsilon_0} \delta (\vec r - \vec r')
\tag{11}
$$

To solve this equation and get the Greens function needed to solve Eq. 9, first, we set $\vec r' = 0$ since the delta function only cares about the difference between $\vec r$ and $\vec r'$. This yields $G(\vec r)$ and $\delta(\vec r)$
Then we Fourier transform the Green's function and the delta function:

- Green's function:

    $$
    \begin{aligned}
    G(\vec k) = \mathcal{F}[G(\vec r)](\vec k) &= \frac{1}{(2\pi)^{3/2}} \int G(\vec r) e^{-i\vec k \vec r} d\vec r\\
    G(\vec r) = \mathcal{F}^{-1}[G(\vec k)](\vec r) &= \frac{1}{(2\pi)^{3/2}} \int G(\vec k) e^{i\vec k \vec r} d\vec k
    \end{aligned}
    $$

- delta function:

    $$
    \begin{aligned}
    \delta(\vec k) = \mathcal{F}[\delta(\vec r)](\vec k) &= \frac{1}{(2\pi)^{3/2}} \int \delta(\vec r) e^{-i\vec k \vec r} d\vec r\\
    \delta(\vec r) = \mathcal{F}^{-1}[\delta(\vec k)](\vec r) &= \frac{1}{(2\pi)^{3/2}} \int \delta(\vec k) e^{i\vec k \vec r} d\vec k
    \end{aligned}
    $$

Now, Fourier transforming both sides of Eq. 10 gives:

$$
\begin{aligned}
\nabla^2 G(\vec r, \vec r') &= - \frac{1}{\epsilon_0} \delta (\vec r - \vec r')\\
\nabla^2 \frac{1}{(2\pi)^{3/2}} \int G(\vec k) e^{i\vec k \vec r} d\vec k &= - \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{3/2}} \int \delta(\vec k) e^{i\vec k \vec r} d\vec k\\
\frac{1}{(2\pi)^{3/2}}  \int -k^2 G(\vec k) e^{i\vec k \vec r} d\vec k &= \frac{1}{(2\pi)^{3/2}} \int - \frac{1}{\epsilon_0}  \delta(\vec k) e^{i\vec k \vec r} d\vec k\\
\end{aligned},
\tag{12}
$$

and we can observe that:

$$
\begin{aligned}
k^2 G(\vec k) &= - \frac{\delta(\vec k)}{\epsilon_0}  \\
G(\vec k) &=  - \frac{1}{k^2} \frac{\delta(\vec k)}{\epsilon_0}
\tag{13}
\end{aligned}
$$

To get back to the real-space, inverse FT $G(\vec k)$ and use the inverse FT of $\delta(\vec k)$:

$$
\begin{aligned}
G(\vec r) &= \frac{1}{(2\pi)^{3/2}} \int G(\vec k) e^{i\vec k \vec r} d\vec k\\
&= \frac{1}{(2\pi)^{3/2}} \int - \frac{1}{k^2} \frac{\delta(\vec k)}{\epsilon_0} e^{i\vec k \vec r} d\vec k\\
&= \frac{1}{(2\pi)^{3/2}} \int - \frac{1}{k^2} \frac{1}{\epsilon_0} \left ( \frac{1}{(2\pi)^{3/2}} \int \delta(\vec r') e^{-i\vec k \vec r'} d\vec r' \right ) e^{i\vec k \vec r} d\vec k\\
&= \frac{1}{(2\pi)^{3}} \int \frac{e^{i\vec k (\vec r - \vec r')}}{k^2} d\vec k \int \frac{\delta(\vec r')}{\epsilon_0} d \vec r'\\
&= \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{3}} \int \frac{e^{i\vec k (\vec r)}}{k^2} d\vec k
\end{aligned},
$$

assuming spherical symmetry:;

$$
\begin{aligned}
G(\vec r) &= \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{3}} \int \frac{e^{i\vec k (\vec r)}}{k^2} d\vec k \\
&= \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{3}} \int_0^{2\pi} \int_{0}^{\pi} \int_{0}^{\infty} k^2 \sin(\theta) \frac{e^{i k \cos(\theta) |\vec r|}}{k^2} d\phi d\theta dk  \\
&= \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{2}} \int_{0}^{\pi} \int_{0}^{\infty} k^2 \sin(\theta) \frac{e^{i k \cos(\theta) |\vec r|}}{k^2} d\theta dk
\end{aligned},
$$

substituting $\cos(\theta)$ with $u$ and change the limits of the angular integral:

$$
\begin{aligned}
G(\vec r) &= \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{2}} \int_{0}^{\pi} \int_{0}^{\infty} k^2 \sin(\theta) \frac{e^{i k \cos(\theta) |\vec r|}}{k^2} d\theta dk  \\
&= \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{2}} \int_{-1}^{1} \int_{0}^{\infty} e^{i k u |\vec r|} du dk  \\
&= \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{2}} \int_{0}^{\infty} \frac{1}{ik |\vec r|} \left( e^{i k |\vec r|} - e^{ -i k |\vec r|} \right) dk
\end{aligned}.
$$

We know that:

$$
\sin(a) = \frac{e^{ia} - e^{-ia}}{2i}
$$

so that:

$$
\begin{aligned}
G(\vec r) &= \frac{1}{\epsilon_0} \frac{1}{(2\pi)^{2}} \int_{0}^{\infty} \frac{1}{ik |\vec r|} \left( e^{i k |\vec r|} - e^{ -i k |\vec r|} \right) dk \\
&= \frac{1}{\epsilon_0} \frac{1}{2\pi^{2}} \int_{0}^{\infty} \frac{1}{k |\vec r|} \sin (k |\vec r|) dk
\end{aligned}
$$

substituting $v$ with $(k \mid \vec r \mid)$:

$$
\begin{aligned}
G(\vec r) &= \frac{1}{\epsilon_0} \frac{1}{2\pi^{2}} \int_{0}^{\infty} \frac{1}{k |\vec r|} \sin (k |\vec r|) dk\\
&= \frac{1}{\epsilon_0} \frac{1}{2\pi^{2}} \frac{1}{|\vec r|} \int_{0}^{\infty} \frac{\sin(v)}{v} dv \\
&= \frac{1}{4 \pi \epsilon_0 |\vec r|}
\end{aligned}
\tag{13}
$$

which, is exactly the potential generated by a single point charge located at the origin point.

If we don't specify $\vec r' = 0$, then:

$$
\begin{aligned}
G(\vec r, \vec r') &= \frac{1}{4 \pi \epsilon_0 |\vec r - \vec r'|}
\end{aligned}
\tag{14}
$$

Finally, substituting Eq. 14 to Eq. 10, we get:

$$
\psi(\vec r) = \frac{1}{4 \pi \epsilon_0} \frac{\rho(\vec r')}{|\vec r - \vec r'|} d \vec r'
\tag{15}
$$

Which, is exactly the solution to our Possion equation.

For more information:

- This article if based on [🔗this paper](https://www.scielo.br/j/rbef/a/yvDhk5GVrC5fTtmT9JQMFWb/?lang=en)

- Watch [🔗this video](https://www.youtube.com/watch?v=Ld1u7bew6wc) from Andrew Dotson for a more "matrix" like explanation 😉.


Next up, [🔗the quantum version](../16/Greens_function_2).
