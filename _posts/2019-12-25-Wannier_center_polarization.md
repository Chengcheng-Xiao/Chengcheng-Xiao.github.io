---
layout: post
title: Using Wannier Charge center to calculate Ferroelectric polarization
date: 2019-12-25
tags: ["Polarization"]
categories: DFT
description: A brief guide for calculating macroscopic polarization using Wanneir functions and how to avoid it many pitfalls.
---

## Background

According to "the Modern theory of polarization", in a continous-k formulation, the polarizatin $$\mathbf{P}_{el}$$ value is $$ - f e / (2 \pi)^3$$ times the sum of valence-band Berry phase. On another note, Wannier charge center can be convieniently linked to the Berryphase of valence band via a Fourier transformation. Thus, we should be able to calculate the ferroelectric polarization using Wannier interpolation of Bloch bands.

## Objectives

 - To calculate the polarization value of $$BaTiO_{3}$$, compare it with the Berryphase one.
 - To give a rough idea of how periodicity affect the calculation of the ferroelectric polarization.
 - To get familiar with VASP2WANNIER interface

## Structure(s)
We need both centro symmetric and non-centro Ferroelectric structure.

![]({{site.baseurl}}/assets/img/post_img/2019-12-25-img1.png)
{: .center}

## Berryphase method result
To get polarization value using VASP, just add the following line to your SCF(static) calculation's  `INCAR`:

```
LCALCPOL=.T.
```
In the `OUTCAR` file, you will find a block like the following:
```
     CALCP:  cpu time   11.0656: real time   11.0798

            Ionic dipole moment: p[ion]=(     0.00000     0.00000   -11.57420 ) electrons Angst

 Total electronic dipole moment: p[elc]=(    -0.00000    -0.00000    -1.68410 ) electrons Angst
 ```

For the __result__, I refer back to one of my previous [post]({% post_url 2019-08-05-Berryphase_Ferroelectricity %}):
> By varying the atomic displacement from the centrosymmetric phase (CENT) to ferroelectric one (FE). VASP produce a series of ionic and electronic contribution to the total dipole moment.

|   Image  | Ion (elect*A) | Electron (elect*A) |
|----------|---------------|--------------------|
| 0 (CENT) | +00.00000     | +0.00000           |
| 1        | -12.01278     | -0.29138           |
| 2        | -11.92507     | -0.58047           |
| 3        | -11.83735     | -0.86532           |
| 4        | -11.74963     | -1.14461           |
| 5        | -11.66192     | -1.41757           |
| 6 (FE)   | -11.5742      | -1.68399           |
{: .center}
>we can easily calculate its ionic dipole moment at centrosymmetric phase should be -12.09 elect*A.

>After figure out which value is clearly wrong, we can now proceed to calculate total polarization:

```
Total ionic contribution = 0.5258 elect*A
Total electronic contribution = -1.68399 elect*A
Total dipole moment = -1.15819 elect*A
Volume = 64.35864801 A^3

Total polarization = 0.288293871 C/m^2
```

## Wannier result

In this section, I will introduce the usage of VASP2WANNIER interface as well as a general method to construct the valence band's Wannier functions.

- Wannier functions are a set of localized functions generated using Fourier transformation of periodic bloch functions.
- We only use valence bands to generate Wannier functions so that the square of it can represent the charge density.
- Each Wannier function "corresponds" to an energy band, hence, each Wannier function is occupied by 2 electrons (or 1 if we treat each spin channel separately).

### Fat band analysis
We need fat band analysis in order to get a sense of how our valence band are composed.

[!image]

This result coincide with our chemical intuition. From the electron configurations, we can see that:

|   Element  | Electron configuration  | Valency | Number in the unitcell|
|------------|-------------------------|---------|-----------------------|
| Ti         | 3s(2) 4s(1) 3p(6) 3d(3) |   +4    |      1                |
| Ba         | 5s(2) 6s(2) 5p(6)       |   +2    |      1                |
| O          | 2s(2) 3p(4)             |   -2    |      3                |
{: .center}

which means, our valence bands are composed by:
```
Ti         : 3s(2) 3p(6)
Ba         : 5s(2) 5p(6)
O          : 2s(2) 3p(6)
```
This can also be clearly seen on the projected band structure or projected density of states plot.

### Setting up `Wannier90.win`
VASP2WANNIER90 interface requires following parameters to run(at minimum):

```
num_wann        =  20

begin projections
Ba:s,p
Ti:s,p
O:s,p
end projections
```
Here, I use Ba's s and p orbitals, Ti's s and p orbitals and O's s and p orbitals a initial projection as discussed above.

Since we have a set of isolated valence bands, we can exclude the conduction bands by adding:
```
num_bands = 20
exclude_bands = 21-24
```
Other information such as unitcell information, atom's positions, k-point info's can be written automatically by VASP.

Furthermore, I added `num_iter        = 0` to use projection only scheme.

After written `wannier90.win` file, add the following line:
```
LWANNIER90 = .T.
```
to your `INCAR` and run it. VASP will produce `wannier90.mmn`, `wannier90.amn`, `wannier90.eig` files.

Then run WANNIER90 by:
```
wannier90.x wannier90
```
and it will generate wannier90.out file. Near the end of that file, there should be a block look like the following:
```
Final State
  WF centre and spread    1  (  0.000000,  0.000000, -0.000000 )     1.21037767
  WF centre and spread    2  ( -0.000000,  0.000000, -0.000000 )     1.28161513
  WF centre and spread    3  ( -0.000000, -0.000000, -0.000000 )     1.28337360
  WF centre and spread    4  ( -0.000000, -0.000000,  0.000000 )     1.28337360
  WF centre and spread    5  (  1.997250,  1.997250,  2.016750 )     0.79906780
  WF centre and spread    6  (  1.997250,  1.997250,  2.016750 )     0.50984278
  WF centre and spread    7  (  1.997250,  1.997250,  2.016750 )     0.51118782
  WF centre and spread    8  (  1.997250,  1.997250,  2.016750 )     0.51118782
  WF centre and spread    9  (  1.997250,  1.997250, -0.000000 )     0.80333011
  WF centre and spread   10  (  1.997250,  1.997250,  0.000000 )     1.41881817
  WF centre and spread   11  (  1.997250,  1.997250, -0.000000 )     1.35842712
  WF centre and spread   12  (  1.997250,  1.997250,  0.000000 )     1.35842711
  WF centre and spread   13  (  1.997250,  0.000000,  2.016750 )     0.80396422
  WF centre and spread   14  (  1.997250,  0.000000,  2.016750 )     1.35724005
  WF centre and spread   15  (  1.997250, -0.000000,  2.016750 )     1.35167690
  WF centre and spread   16  (  1.997250,  0.000000,  2.016750 )     1.40712275
  WF centre and spread   17  (  0.000000,  1.997250,  2.016750 )     0.80396421
  WF centre and spread   18  (  0.000000,  1.997250,  2.016750 )     1.35723996
  WF centre and spread   19  (  0.000000,  1.997250,  2.016750 )     1.40712272
  WF centre and spread   20  (  0.000000,  1.997250,  2.016750 )     1.35167681
  Sum of centres and spreads ( 23.967000, 23.967000, 24.201000 )    22.16903637
```
those three data between parentheses are the __Wannier Charge Centers__:

$$\mathbf{R}_{i} = \langle \psi_{i} | \mathbf{r} | \psi_{i} \rangle$$

Now we can proceed to calculate the macroscopic polarizations.

### Calculating polarization
According to "the modern theory of polarization", the macroscopic polarization can only be obtained by substracting the centrosymmetric phase's dipolemoment from the Ferroelectric one. Here, I'll do a little trick to circumvent this and eventually show you how everything fits.

### calculate polarization __without__ centrosymmetric phases
The centrosymmetric phase can be safely ignored when its polarization equals to __ZERO__, which is, as a matter of fact, true in our case, so we can safely ignore it if we are careful enough.

To calculate the electronic contribution to the polarization, just sum each __Wannier Charge Centers__ and then multiply if by a spin-degenerate factor 2:

$$\mathbf{P}_{elect}=2 * \Sigma_{i} \mathbf{R}_{i} $$

To calculate the ionic contribution to the polarization, first find each ions core chareges (positive), then multiply it to the atomic position and sum it up:

$$\mathbf{P}_{ion}=\Sigma_{I} C_{I}  \mathbf{R}_{I} $$

sincd r and R are vectors, in order to get the total polarization, we have to do this on three axis and then add them up using vector summation. Here, I only care the polarization at Z axis, so I ignored the other axis's contribution. My result follows [note the minus sign in Ionic part is due to electrons negative charge sign]:

```
Ionic dipolemoment(elect*A):     -72.0767  
electric dipolemoment(elect*A):   78.9870
Total dipolemoment(elect*A):      06.9103
Volume(A^3):                      64.3586
Total polarization(C/M^2):       -01.7200
```

This value is drastically large than the one we get using Berryphase method. There must be something wrong here!

And indeed, here, we encountered the so-called __polarization quantum__.

$$\mathbf{P}_{quantum}=N * Lattice\_parameters$$

Where N equals to some integer number that represent the number of electron get involved.

Taking a closer look at our structure, the FE one have one oxygen at ~3A while it goes to 0A in the centrosymmetric phase. An atom moving 3A durinng phase transition is not ideal! Intuitively, one may think "OK, thats alright, we have periodic boundary, so we only have to move this atom up-wards to the boundary." Yes, this is indeed the case, but our method cannot deal with this, that why the __polarization quantum__ is always linked with the lattice parameters and the polarization curve (displacement vs polarization) is multi-valued.

To solve this, simply substract one lattice parameter Z from the atomic position as well as the corresponding __Wannier Charge Centers__, we get [note the minus sign in Ionic part is due to electrons negative charge sign]:

```
Ionic dipolemoment(elect*A):     -48.8757  
electric dipolemoment(elect*A):   46.7191
Total dipolemoment(elect*A):     -01.1567
Volume(A^3):                      64.3586
Total polarization(C/M^2):        00.2879
```
This way, our polarization calculated via Wannier functions is almost identical to the Berry phase result.

### calculate polarization __with__ centrosymmetric phases
If we stick with the method described above, finding where went wrong can be tedious for a different, say, larger system, especially when you are confused of which wannier function belongs to which atom. And yes, there is another way of dealing with the __polarization quantum__, that is to subtract the centrosymmetric's dipolemoment from the Ferroelectric one.

Sill , we need to move the atom position to the same brach, here I move the centrosymmetric phase's Oxygen from 0A to 4.0335A which is one lattice constant on the Z axis. Resulting data are [note the minus sign in Ionic part is due to electrons negative charge sign]:
```
Ionic dipolemoment(elect*A):     -72.6030
electric dipolemoment(elect*A):   80.6700
Total dipolemoment(elect*A):      08.0670
Volume(A^3):                      64.3586
Total polarization(C/M^2):       -02.0080
```

substracting this from the FE's result, we get 0.2879C/M^2, exactly the same as our previous method yields.

>_**WARNING**_ The sign convention for the ionic part is very important. Please, for the love of god, remember change dot the dipole moment of each structure's result with a minus sign and **ADD** it to the electronic part (so that they are both in elect * A). And remember to flip the sign of the final result (in C/M^2).


## Conclusion
The calculation of the macroscopic electric polarizations can have many pitfalls, and almost all of them are related to the __polarization quantum__. Check your structures and make sure they are on the same brach can have many beneficial effect!

## Input

I've put all input file in a zip file for download: [VASP].

[VASP]:{{site.baseurl}}/assets/other/2019-12-25-Wannier_polarization.zip
