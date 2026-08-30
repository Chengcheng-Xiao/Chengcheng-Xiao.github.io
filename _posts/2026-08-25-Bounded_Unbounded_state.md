---
layout: post
title: "\"Unbounded States\" in Electrides are Multicentred Bonds"
date: 2026-08-25
categories: Post
description: "A recent paper argues that unbounded states are the true origin of
the interstitial electrons in electrides, in this blog post I show that it is
simply an extension of multicentred bonding."

tags: Comments

---

An interesting paper recently poped on arXiv titled ["Potential-Barrier Affinity
Effect in Solid Systems"](https://arxiv.org/abs/2511.11160) by Qiang Xu, Zhao
Liu and Yanming Ma, in which the authors relay three interesting points:

1. They pointed out that the interstitial electronic states in electrides does
   not sit (or peaked) in a Kohn-Sham potential well, instead, they are usually
   found to be near a potential maximum.

2. At the same time, the interstitial states have their Kohn-Sham eigen-energies
   higher than the potential maximum, which leads to the so-called "unbounded"
   nature of these states. And they further used words such as "near-free
   electron state" in relation to there "unbounded" states.

3. Using a simple 1D Kornig-Penny model, they discoverted that the interstitial
   peak of the wave function is rooted in the continuous nature of the wave
   function that was forced between the interstitial region and the atomic
   region. Or as they put it, the "Potential-Barrier Affinity".

I find the paper to be well written and interesting, as it gives novel huristics
to the origin of interstitial localised electrons in electrides.

In this post, I want to provide an alternative explanation of the origin of this
"unbounded" phenomena of the interstitial states that is equally valid and
chemically intuitive, and try to convince you that this phenomena is simply just
an extension of the multicentred bonding theory.

## Alternative explanation of the "unbounded" states

Perhaps to no one's suprise, Ma et al are not the first people to make the
observations that the interstitial states are usually found near a potential
maximum instead of a minimum -- back in 1993, [Singh et
al.](https://doi.org/10.1038/365039a0) conducted DFT calculations on
Cs+(15C5)2e− and found that the chemical potential of the void region was higher
than that of the surrounding crystal, and localisation of the electron in this
region was justified by a need to lower its kinetic energy. 

However, Ma et al did bring up an interesting finding that the interstitial
states found in electrides have their eigen-energies higher than the potential
maximum, which seemingly breaks the classical understanding of the potential
well and the bound states. To rationalise this, the authors made a connection
between certain eigen-states of a 1D Kornig-Penny model to the unbounded states
of an isolated finite potential well, and argued that the "interstitial
localisation" of electrons in electrides is caused by similar "unbounded" states
that have eigen-energy higher than the global effective Kohn-Sham potential
maximum.

<!-- However, I want to point out that the use of the words such as "unbounded" and -->
<!-- "nearly-free electron" in this context is not strictly correct, and might be -->
<!-- misleading and requires more careful consideration. -->

<!-- The authors claim that interstitial localisation effect is caused by "unbounded" -->
<!-- states that has eigen-energies higher than the global potential maximum.  -->

This behaviour can, alternatively, be easily understood using a simple energy
component analysis of the Kohn-Sham eigen-energy using atomic basis (i.e., of
linear combination of atomic orbitals method).

Let us start by considering a di-atomic system where each atom has a s-orbital
and the bonding state is formed by the in-phase combination of these s-orbitals.
Naturally, if the bonding orbital have a strong peak at the bond centre, we can
assume a Wannier like bonding orbital at the bond centre $\psi_\mathrm{W}$ and
the potential energy $V$ of this state is approximated by

$$ 
% V = \int_\mathrm{near\ bond\ centre} \psi^*_\mathrm{W}(x) V_M
%\psi_\mathrm{W}(x) dx = V_M 

V \approx \int \psi^*_\mathrm{W}(x) V_M
\psi_\mathrm{W}(x) dx = V_M, 
$$

and the kinetic energy $T$ is bigger than zero because this is a bonding orbital

$$
% T = \int_\mathrm{near\ bond\ centre} \psi^*_\mathrm{W}(x) (-\frac{1}{2} \nabla^2) \psi_\mathrm{W}(x) dx > 0
T = \int \psi^*_\mathrm{W}(x) \left[ -\frac{1}{2} \nabla^2 \right] \psi_\mathrm{W}(x) dx > 0.
$$

Hence the total eigen-energy will be larger than the KS potential near the bond
centre:

$$
E = T + V > V_M.
$$

In other words, **a bonding state with significant portion of its wave function
peaked at the bond centre will have higher eigen-energy than the potential at
the bond centre.** 

We can generalise this to more realistic periodic systems. We now switch to a 1D
model system of Be chain and study its electronic properties using DFT. In this
system, the bond distance between adjacent Be atoms is $2$ Å and a vacuum of
$10$ Å is employed along the other two directions. The electronic structure is
approximated at the PBE level with a plane-wave cutoff of 500 eV and 20x1x1
k-point sampling.

The result show that there are two occupied bands (both near-free electron like)
formed by linear combination of 1s and 2s+(2p) orbitals. The band structure is
as follows

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img1.png){:height="50%" width="50%" .center}

where the 1s bonding state ($\psi_\mathrm{1s}$) has an energy of $\sim -50$ eV,
and is localised on atomic sites.

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img2.png){:height="50%" width="50%" .center}

On the other hand, the 2s (zone centre) + 2p (zone boundary) bonding state ($\psi_\mathrm{2s}$) has an energy of
$\sim -3.5$ eV and is localised on the bond centre

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img3.png){:height="50%" width="50%" .center}

The full Kohn-Sham potential profile along the atomic chain is:

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img4.png){:height="70%" width="70%" .center}

Note that here the atoms sit at $0$ Å and $2$ Å positions. Clearly, we see that
the same behaviour as described in the paper is found even for this simple
system: the $V_M$ is $\sim20$ eV which is much lower than the energy of the 2s
bonding state $\psi_\mathrm{2s}$ of $\sim -3.5$ eV. 

This matches the expectation from our previous analytical result -- the bonding
orbital that has significant amplitude near the bond centre ($\psi_\mathrm{2s}$)
should have higher energy than the Kohn-Sham effective potential at the bond
centre ($V_M$), due to its excessive kinetic energy. 

It is interesting to note that in this simple 1D system, $V_M$ is also the
(global) maxima along the periodic 1D direction. However, one would not
categorise this system as an electride, similar to what the authors discussed in
the manuscript of Al.

### Link to the Multicentred Bonding Theory

We can generalise this finding to all other types of **bonding orbitals**
including multicentred bonding orbitals which we believe is the underlying
mechanism of the existence of interstitial states: An in-phase combination of
atomic orbitals form a bonding orbital that peaks at the interstitial region,
leading to an eigen-energy higher than the potential at the bond centre
(interstitial centre). A definition originated from this theory leads to a much
more general and applicable criteria for identifying electrides: **If a system
has a multicentred bonding orbital that strongly peaks at the interstitial
region, it is an electride.**

<!-- There are several consequences of using this definition: -->
<!--  -->
<!-- Now, under the linear combination of atomic orbital (LCAO) framework, the need -->
<!-- for a bonding orbital to have significant peak at the bond centre depends on two -->
<!--     criteria:  -->
<!-- 1. The shape of the orbitals. Ie, how diffusive the orbitals are. -->
<!-- 2. The distance between these orbitals. -->
<!--  -->
<!-- One can come up with an analytical geometric criteria for certain types of -->
<!-- orbitals so that the LCAO bonding state will have significant portion of its -->
<!-- wave function near the bond centre. We anticipate this will be prominent for -->
<!-- cages formed by atoms with frontier s-orbitals and in systems where pressure is -->
<!-- applied (i.e., smaller cages). -->

<!-- ### Alternative explanation of the "origin' of interstitial state -->

From a linear combination of atomic orbtials (LCAO) perspective, the existance
of interstitial states is a direct consequence of the orthogonality of the
atomic basis -- low-lying states are localised on the atoms so that higher
energy states needs to be orthogonal to them. At certain geometry, the bonding
orbitals formed by the in-phase combination of atomic orbitals will have their
peaks at the interstitial region, causing its eigen-energy to be higher than the
potential barrier.

Our alternative explanation also explains why almost all electride consists of
cages that are made with group-I and II species, they possess highly dispersive
s-orbitals that can form these interstitial states more easily, especially under
pressure (high-pressure electride?). 

It is also worth noting that the this origin is a direct reflection of the
Fermionic nature of electrons and is consistent with previous argument that the
Pauli exclusion "forces" electrons to be localised in the interstitial region.

People have found that ELF is a good quantitiy to test if a system is an
electride or not. This also fits perfectly to the multicentre bonding theoyr,
ELF probes the Fermi-hole of the system and are widely used to identify covalent
bonds, which in this case is well suited for finding electride-like states, as a
complimentary to the charge density maxima in the interstitial regions.

### Unbounded states in solid state systems - delocalised or localised? 

The word "unbounded" was generally used in the context of isolated systems. As
an idealised example, if we consider a 1D finite potential well where the
potential is zero at infinity and $-V$ inside the well, the eigen-energies of
bound states are quantised and lower than zero (i.e., lower than potential at
infinity), and the eigen-energies of unbounded states are higher than the
potential at infinity (zero) and are continous (i.e., not quantised). In this
case, the definition of an unbounded state is clear: **they are states that have
eigen-energy higher than the potential at infinity, and their wave functions are
not localised, but oscillate across the entire space.**

Furthermore, for isolated systems, the unbounded states are extended to
infinity, and the bound states can only appear near the potential well. This
offers a clear distinction between a localised state and a delocalised state:
**bounded states are localised and have lower energy than the potential well
maxium and unbounded states are delocalised nd have higher energy than the
potential well maximum.**

However, in solid state systems, according to Bloch's theorem, the electronic
wave functions are completely extended along all directions, regardless of their
eigen-energies. Hence, we no longer have a clear distinction between a localised
state and a delocalised state. 


In solid state systems, "localisation" is usually interpreted by two
diffinitions: (1) The wavefunctions are peaked at a specific locations, and (2)
The dispersion of the band is small, which means that the kinetic energy of the
state is relatively small. 


It is worth noting that these two definitions do not contradict each other and
if they are both satisfied, we have a strict definition of a localised state.
    For example, semi-core states are strongly peaked on the atomic sites and
    have very small dispersion. From a tight-binding perspective, these states
    are strongly localised because the atomic orbitals have very small
    interaction with each other and are peaked on the atoms. If we take a look
    at the eigen-energy of these states, we will find that they are more or less
    the same as the single atom energy level of the corresponding atomic orbital
    which also verifies that these states are made of atomic orbitals that
    possess little interaction(hybridisation) with each other.


From a more pratical (and perhaps more chemical) perspective, having peaks at a
specific locations is a more relaxed definition of localisation that is
connected to the physical observable of the system -- charge density. If the
wave function is normalisable and strongly peaked at specific locations, the
charge density will also be strongly peaked at those locations. I believe this
is the definition that should be used for the electride community.

### Unbounded states in solid state systems - Near-free electron like?

Ma et al used word such as "near-free electron state" in relation to the
interstitial states, based on their observation that interstitial states have
eigen-energies higher than the potential maximum and have parabolic dispersion.
However, I find this description misleading:

First of all, the Kronig-Penny model does not have strict unbounded states that
give a pure continouse energy spectrum, and all states from the Kronig-Penny
model are normalisable hence are not scattering states -- In reality, all
electronic states are contrained by the vacuum level as the system cannot be
truly periodic infinitely. 

I find it interesting that the vacuum level in solid state systems is defined as
the potential in the vacuum region far away from the atoms, but exactly how far
away is really "far away" is arbitary. As an analogy, consider breaking a bond
by increasing the distence between two atoms, the potential in the middle of the
bond will eventually converge to the vacuum level, but at exactly what distance
is this bond considered broken is not well defined.

In their paper, Ma et al presented a brand new set of criteria to identify
electride systems: (i) the Fermi level lies above the maximum of the effective
potential barrier; (ii) the barrier maximum is located in a spatially open
region far from nuclei; and (iii) an appreciable density of occupied states
exists between the Fermi level and the barrier maximum. 

Following my vacuum level argument, I find that their central criteria (i), is
not valid to identify electrides as one can easily construct a system that does
NOT satisfies these criteria but should be considered an electride. For example,
if we have a block of prototypical electride material, we can always carve out a
    small portion of the system and replace it with vacuum. The resulting system
    will have a potential maximum at the vacuum level, which is higher than the
    Fermi level of the electride, and hence does not satisfy the criteria (i).


Secondly, not all prototypical electrides have parabolic dispersion! YCl system
(see [ref](https://www.nature.com/articles/s41467-026-69049-0)), for example,
shows a flat band at the Fermi level, which is a signature of strong correlation
and is not a near-free electron state. As a matter of fact, the correlation
interaction is an interesting topic in electrides and is actively being explored
(see [ref2](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.110.024413)
and
[ref3](https://pubs.acs.org/jpclcd/article/12/50/12020/581019/Electronic-Correlation-Strength-of-Inorganic)).


