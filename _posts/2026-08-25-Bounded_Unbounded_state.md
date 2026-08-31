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
Liu and Yanming Ma, in which the authors bring up three interesting points:

1. They pointed out that the interstitial electronic states in electrides does
   not sit (or peaked) in a Kohn-Sham potential well, instead, they are usually
   found to be near a potential maximum.

2. At the same time, the interstitial states have their Kohn-Sham eigen-energies
   higher than the potential maximum, which leads to the so-called "unbounded"
   nature of these states. And they further used words such as "near-free
   electron state" in relation to there "unbounded" states.

3. Using a simple 1D Kornig-Penny model, they discovered that the interstitial
   peak of the wave function is rooted in the continuous nature of the wave
   function that was forced between the interstitial region and the atomic
   region. Or as they put it, the "Potential-Barrier Affinity".

I find the paper an interesting read as it gives novel huristics
to the origin of interstitial localised electrons in electrides.

In this post, I want to provide an alternative explanation of the origin of this
"unbounded" phenomena of the interstitial states that is equally valid and
chemically intuitive, and try to convince you that this phenomena is simply just
an extension of the multicentred bonding theory.

## Alternative explanation of the "unbounded" states

Perhaps to no one's suprise, Ma et al are not the first people to make the
observations that the interstitial states are usually found near a potential
maximum instead of a minimum -- back in 1993, [Singh et
al](https://doi.org/10.1038/365039a0) conducted DFT calculations on
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

However, I found this behaviour is actually a manifestation of the multicentred
bonding theory where the interstitial orbitals are considered bonding orbitals
formed by surrounding atoms' atomic orbtials. Hence can be easily understood via
energy component analysis of the Kohn-Sham eigen-energy using atomic basis
(i.e., of linear combination of atomic orbitals method).

Let us start by considering a di-atomic system where each atom has a s-orbital
and the bonding state is formed by the in-phase combination of these s-orbitals.
Naturally, if the bonding orbital have a strong peak at the bond centre, we can
assume a Wannier like bonding orbital at the bond centre $\psi_\mathrm{W}$ and
the potential energy $V$ of this state can be approximated by

$$ 
V \approx \int \psi^*_\mathrm{W}(x) V_M
\psi_\mathrm{W}(x) dx = V_M, 
$$

and because this is a bonding orbital, the kinetic energy $T$ is bigger than
zero 

$$
T = \int \psi^*_\mathrm{W}(x) \left[ -\frac{1}{2} \nabla^2 \right] \psi_\mathrm{W}(x) dx > 0.
$$

Hence the total eigen-energy will be larger than the KS potential near the bond
centre:

$$
E = T + V > V_M.
$$

In other words, this finding tells us that **a bonding state with significant
portion of its wave function peaked at the bond centre will have higher
eigen-energy than the potential at the bond centre,** due to its excessive
kinetic energy.

This simple analysis leads to two important conclusions:

1. The phenomena where the Kohn-Sham eigen-energy of the bonding orbital is
   higher than the potential at the bond centre is **not a special case, but
   rather a general phenomena that can be expected in any bonding orbital that
   has significant amplitude at the bond centre.**

2. This phenomena depends on the orbital types -- From a linear combination of
   atomic orbtials (LCAO) perspective, **it depends on the distance between the
   atomic orbtials and the shape of the atomic orbitals.**

Next, I'll try to generalise this to more realistic periodic systems and show
that this behaviour can indeed be controlled by manipulating with the bond
distance.

### Generalisation to 1D periodic system

To convince ourselves that this phenomena exist not just in our simple di-atomic
model but to more realistic systems, we now proceed to perform simple DFT
calculations on a 1D Li chain. In this system, the bond distance between
adjacent Li atoms is 2 Å (along the x-direction) and a vacuum of 10 Å is
employed along the other two directions. The electronic structure is
approximated at the PBE level with a plane-wave cutoff of 500 eV and 20x1x1
k-point sampling.

As shown below, the band structure suggests that there are two bands that are of
interest here (both have parabolic-shape dispersion). One fully occupied at ~-50
eV which is composed of mostly Li's 1s orbitals, and the other half-occupied at
~-3.5 eV which is composed of mostly Li's 2s and 2p<sub>x</sub> orbitals

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img1.png){:height="50%" width="50%" .center}

Interestingly, the probability density of the 1s bonding state
($\psi_\mathrm{1s}$) is localised (peaked) on atomic sites.

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img2.png){:height="40%" width="40%" .center}

On the other hand, the 2s (zone centre) + 2p (zone boundary) bonding state
($\psi_\mathrm{2s}$) is localised (peaked) on the bond centre.

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img3.png){:height="40%" width="40%" .center}

Now, if we looke at the full Kohn-Sham potential profile along the atomic chain
(Note that here the atoms sit at 0 Å and 2 Å positions),

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img4.png){:height="70%" width="70%" .center}

we see that it has a maximum $V_M$ of ~20 eV at the bond centre, which is much
lower than the eigen-energy of the second bonding state $\psi_\mathrm{2s}$ of
~-3.5 eV. Combining with the fact that $\psi_\mathrm{2s}$ is also strongly
peaked at the bond centre, we see that the conclusions of our previous analysis
hold true in this much more realistic setting as well.


<!-- It is interesting to note that in this simple 1D system, $V_M$ is also the -->
<!-- (global) maxima along the periodic 1D direction. However, one would not -->
<!-- categorise this system as an electride, similar to what the authors discussed in -->
<!-- the manuscript of Al. -->


### Tunning it!

Accoding to our previous analysis, the phenomena of having a bonding state with
eigen-energy higher than the potential at the bond centre can only happen if the
bonding state has significant amplitude at the bond centre. Hence, if we can
change the bond distance between the atoms, within the LCAO approximation, we
can tune the amplitude of the bonding state at the bond centre and hence tune
the eigen-energy of the bonding state relative to the potential at the bond
centre.

Again, we will use the same 1D Li chain model, but this time we will change the
bond distance between adjacent Li atoms from 3 Å to 8 Å, and see how the
eigen-energy of the bonding state $\psi_\mathrm{2s}$ changes relative to the
potential at the bond centre.

Noticing that we the band structrue of $\psi_\mathrm{2s}$ state always has a
minimum at the zone centre (Γ point), we can track the eigen-energies of
occupied states by simply tracking the two ends: eigen-energy of the bonding
state at the Γ point and the Fermi energy, and compare them with the potential
max at the bond centre.

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img5.png){:height="70%"
width="70%" .center}

Focusing on the two limits: At a bond distance of 3 Å, both the eigen-energy at
Γ point and the Fermi energy of the bonding state $\psi_\mathrm{2s}$ are higher
than the potential at the bond centre, meaning all states occupied are
"unbounded" states. However, at a bond distance of 8 Å, both the eigen-energy at
Γ point and the Fermi energy of the bonding state $\psi_\mathrm{2s}$ are lower
than the potential at the bond centre, meaning all occupied states have been
turned into "bounded" states. 

Now, if we plot the charge density coming from $\psi_\mathrm{2s}$ at these two
bond distances,

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img6.png){:height="70%"
width="70%" .center}

we see that at 3 Å, the charge density is strongly peaked at the bond centre,
while at 8 Å, the charge density is strongly peaked on the atomic sites. This
    means that by simply changing the bond distance, we can easily tune the
    eigen-energy of the bonding state relative to the potential at the bond
    centre.

You might be wondering: **Are these two states fundamentally different?** I
believe the answer is no -- They both represent the same bonding state! As we
all know, if we stretch a bond from its equilibrium distance to inifity, the
"bond breaking" point cannot be strictly defined as their transition is
continuous and smooth. Here, we see that the same smooth transition between
"bounded" and "unbounded" states because they are a consequence of the same
"bond breaking" process.


Here, I would also like to point out that even though the eigen-energy of the
bonding state $\psi_\mathrm{2s}$ is still higher than the potential at the bond
centre at a bond distance of 5 Å, it **has already lost its peak at the bond
centre** (see below), meaning that one cannot use the charge density peak to
deteremine if a state is "bounded" or "unbounded".

![]({{site.baseurl}}/assets/img/post_img/2026-08-25-img7.png){:height="70%"
width="70%" .center}


### Link to the Multicentred Bonding Theory

{% capture body_content %} 

We have recently release a paper on the multicentred bonding theory of
electrides, in which we proposed that the interstitial states in electrides are
simply multicentred bonding orbitals formed by the in-phase combination of
atomic orbitals. Give it a read at
[https://arxiv.org/abs/2605.11724](https://arxiv.org/abs/2605.11724)!

{% endcapture %}

{% include admonition.html type="tip" title="Paper" body=body_content %}

Now that I have demonstrated that the same behaivour can be easily understood
using the LCAO argument, I would like to note that this analysis can also be
easily generalised to all other types of bonding orbitals including multicentred
bonding orbitals, which we believe should be the (chemical) origin of the of
interstitial states: **An in-phase combination of atomic orbitals form a bonding
orbital that has a significant amplitude at the interstitial region**. Similarly
to our 1D model, this would naturally leads to an eigen-energy higher than the
potential at the bond centre (interstitial centre). 

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

This also provides an alternative explanation of the origin of interstitial
states in electrides. From a LCAO perspective, the existance of interstitial
states is a direct consequence of the orthogonality of the atomic basis --
low-lying states are localised on the atoms and high energy states needs to be
orthogonal to them, hence are "pushed" out of the atomic region. At certain
geometry, the bonding orbitals formed by the in-phase combination of atomic
orbitals will have their peaks at the interstitial region, causing its
eigen-energy to be higher than the potential barrier. 

It is worth noting that this origin is a direct reflection of the Fermionic
nature of electrons and is consistent with previous argument that the Pauli
exclusion "forces" electrons to be localised in the interstitial region.

It is also worth noting that people have found electron localisation function
(ELF) to be a useful tool to identify electrides. ELF fits perfectly to the
multicentre bonding theory because it probes the Fermi-hole of the system, i.e.,
tries to find an orbital that occupies a certain region of space that is not
simultaniously occupied by other orbtials (for more details, see [this
post](../../../2022/01/17/ELF.html)). ELF is widely used to identify covalent
bonds, which in the case of electrides, would be multicentred bonds.

As another consequence of the multicnetred bonding theory, we now see why almost
all electride consists of cages that are made with group-I and II species --
they possess highly dispersive s-orbitals that can form these interstitial
states more easily, especially under pressure (e.g., high-pressure electride). 

## Comments on the jargon transferable to Solid-State Systems

In Ma et al's paper, the word "unbounded" and "near free electron" is
extensively used. However, I personally find that they could be misleading thus
requires more careful consideration.

### "Unbound" in Solid-State Systems

First, let's talk about the word "unbound" state and its relation to
"localisation".

The word "unbounded" was usually used in the context of isolated systems. For
example, consider a 1D finite potential well where the potential is zero at
infinity and $-V$ inside the well, the eigen-energies of bound states are
quantised and lower than zero (i.e., lower than potential at infinity), and the
eigen-energies of unbounded states are higher than the potential at infinity
(zero) and are continous (i.e., not quantised). In this case, the definition of
unbounded states is clear: **they are states that have eigen-energy higher than
the potential at infinity, and their wave functions are not localised, but
oscillate across the entire space.**

Furthermore, for isolated systems, the unbounded states are extended to
infinity, and the bound states can only appear near the potential well. This
offers a clear distinction between a localised state and a delocalised state:
**bounded states are localised and have lower energy than the potential well
maxium and unbounded states are delocalised nd have higher energy than the
potential well maximum.**

However, in solid state systems, due to Bloch's theorem, the electronic wave
functions are extended along all directions, regardless of their eigen-energies.
Hence, no longer a clear distinction can be drawn between a localised state and
a delocalised state in solid-state systems.

In solid state systems, "localisation" is usually interpreted in two ways:

1. The wavefunctions are peaked at a specific locations. This reflects the
   spatial distribution of the wave function.

2. The dispersion of the band is small, which means that it has very low group
   velocity. 

These two definitions do not contradict each other. If they are both satisfied,
we have a strict definition of a localised state. For example, semi-core states
are strongly peaked on the atomic sites and have very small dispersion. From a
LCAO perspective, these states are strongly localised because the atomic
orbitals that make them are spatially small, leading to negligible small
interaction with each other. As a consequence, the eigen-energy of these
states are more or less the same as the single atom energy level of the
corresponding atomic orbital.

From a more pratical (and perhaps more chemical) perspective, having peaks at a
specific locations is a more relaxed definition of localisation that is
connected to the physical observable of the system -- charge density. If the
wave function is normalisable and strongly peaked at specific locations, the
charge density will also be strongly peaked at those locations. I believe this
is the definition that should be used for the electride community.

From my understanding, Ma et al seem to use be confounded on the "unbounded"
nature of the interstitial states and them being "delocalised", because the true
unbounded states in isolated systems are indeed delocalised and they did not
consider that it is different in solid-state systems.

### "Near-free electron" in Solid-State Systems

Secondly, Ma et al used "near-free electron state" in relation to the
interstitial states, based on their observation that interstitial states have
eigen-energies higher than the potential maximum and **have parabolic
dispersion**, which I also find misleading.

First of all, the Kronig-Penny model does not have strict unbounded states that
give a pure continouse energy spectrum, and all states from the Kronig-Penny
model are normalisable hence are not scattering states -- In reality, all
electronic states are contained by the vacuum level as the system cannot be
truly periodic infinitely. 

I find it interesting that the vacuum level in solid state systems is defined as
the potential in the vacuum region far away from the atoms, but exactly how far
away is really "far away" is arbitary. As an analogy, consider breaking a bond
by increasing the distence between two atoms, the potential in the middle of the
bond will eventually converge towards the vacuum level, but at exactly what
distance is this bond considered broken is not well defined (similar to my
previsou "bond-breaking" study using 1D Li chain).

This contradict with Ma et al's new set of criteria to identify electride
systems: 

1. the Fermi level lies above the maximum of the effective potential barrier; 

2. the barrier maximum is located in a spatially open region far from nuclei; 

3. an appreciable density of occupied states exists between the Fermi level and
   the barrier maximum. 

Following my vacuum level argument, I find that **their central criteria (1), is
not valid to identify electrides as one can easily construct a system that does
NOT satisfies these criteria but should be considered an electride**. For
example, if we have a block of prototypical electride material, we can always
carve out a small portion inside the system and replace it with vacuum. The
resulting system will have a potential maximum at the vacuum level, which is
higher than the Fermi level of the electride, and hence does not satisfy the
criteria (1) which requires the Fermi level to be higher than the global
potential maximum.

Now regarding the parabolic dispersion, I have alreay stated before that the
dispersion reflects the group velocity of the state or the interaction strength
between the atomic orbitals that form the bonding state. As a natural
consequence, the parabolic dispersion is not a necessary condition for the
interstitial states and not all prototypical electrides have parabolic
dispersion. For example, YCl system (see
[10.1038/s41467-026-69049-0](https://www.nature.com/articles/s41467-026-69049-0)),
shows a flat band that is composed by the interstitial states at the Fermi
level, which is a signature of strong correlation and would not be considered a
"near-free electron" state. As a matter of fact, the correlation interaction is
an interesting topic in electrides and is actively being explored (see
[10.1103/PhysRevB.110.024413](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.110.024413)
and
[10.1021/acs.jpclett.1c03637](https://pubs.acs.org/jpclcd/article/12/50/12020/581019/Electronic-Correlation-Strength-of-Inorganic)).

