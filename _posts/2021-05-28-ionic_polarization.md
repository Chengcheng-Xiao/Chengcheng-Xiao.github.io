---
layout: post
title: Fixing the ionic part of the polarization in VASP
date: 2021-05-28
categories: Other
description: Debugging VASP is way more fun than using it! Let me show you how I fixed the Ionic part of the polarization step by step! :-J
tags: Blog
---

VASP has a fantastical easy-to-use method to calculate the macroscopic polarization using Berryphase. However, there's been an long standing issue: __The ionic part of the polarization coming out of the `OUTCAR` does not match that calculated by hand.__

I'v dug in deep into the source code and actually found the origin (and of course a solution) of this problem and in the blog post, I'm going to show you how I discovered this step by step.

---
TL;DR

It's a unintentional bug, should be fixed by commenting out the following code in `dipol.F`

```
IF (ABS(ABS(X)-0.5_q)<TINY/LATT_CUR%ANORM(1)) X=0
IF (ABS(ABS(Y)-0.5_q)<TINY/LATT_CUR%ANORM(2)) Y=0
IF (ABS(ABS(Z)-0.5_q)<TINY/LATT_CUR%ANORM(3)) Z=0
```
---

## Chapter 1: "The Problem"

VASP allows has a easy-to-use method (invoked by setting input tag `LCALCPOL` to True) to calculate the macroscopic polarization using the famous Berryphase method. What this routine essentially does is that it runs three sinlge string Berryphase calculations (can also be done manually using `LBERRY` tag) on three lattice directions consecutively.

 The output of this `LCALCPOL` method can be found in both `stdout` and `OUTCAR` file:

- In `stdout`:

 ```
 p_tot=( xxxxxxxxxx xxxxxxxxxx xxxxxxxxxx )
 ```
 will be printed out after the calculation is converged.

- In `OUTCAR`

```
------------------------ aborting loop because EDIFF is reached ----------------------------------------


     CALCP:  cpu time    9.2059: real time    9.2061

            Ionic dipole moment: p[ion]=(   xxx.xxxxx   xxx.xxxxx   xxx.xxxxx ) |e| Angst

 Total electronic dipole moment: p[elc]=(   xxx.xxxxx   xxx.xxxxx   xxx.xxxxx ) |e| Angst

```

The values in `stdout` are simply adding the ionic part to the electric part of the polarization in `OUTCAR` file.

The problem, resides in the Ionic part of the polarization. Specifically, it does not match the values that we can easily calculated by hand.

Let's take the cubic phase of $\mathrm{BaTiO_3}$ for example. The structure I used is:

```
Ti   Ba   O
   1.00000000000000
   3.9944999999999999   0.0000000000000000   0.0000000000000000
   0.0000000000000000   3.9944999999999999  -0.0000000000000000
   0.0000000000000000   0.0000000000000000   4.0335000000000001
Ti   Ba   O
1  1  3
Direct
  0.5000000000000000  0.5000000000000000  0.5000000000000000
  0.0000000000000000  0.0000000000000000  0.0000000000000000
  0.5000000000000000  0.5000000000000000  0.0000000000000000
  0.5000000000000000  0.0000000000000000  0.5000000000000000
  0.0000000000000000  0.5000000000000000  0.5000000000000000
```

### By hand

If we set the dipole origin at the center of the unit cell ([0.5,0.5,0.5]), the Ionic dipole moment can be calculated by dotting the valency (`ZVAL` value in `POTCAR` file) of each atom to the distance between them and the origin. i.e.:

$$
D_{ion} = Z_{val} \cdot \left(r_{atom} - r_{DIPOL}\right),
$$

where $r$ are the position for atoms and dipole center in __Cartesian coordinate__.

For example, $Ba$ atom in our BTO system has 10 valence electrons (`ZVAL = 10`), its ionic dipole moment is:

$$
\begin{aligned}
D_{Ti} &= 22 \cdot [([0.0,0.0,0.0] - [0.5,0.5,0.5]) \cdot [3.99445, 3.9945, 4.0335]] \\
&= [-23.9667, -23.967 , -24.201 ] \quad |e| \cdot \text{Angst}
\end{aligned}
$$

Doing the same procedure for each atoms and adding them together yields:

$$
D_{tot} = [-31.9556,	-31.9556,	-32.268] \quad |e| \cdot \text{Angst}
$$

### By VASP

As before, I've set `IDIPOL` to [0.5,0.5,0.5]. The input relates to the calculation of macroscopic polarization is:

```
DIPOL = 0.5 0.5 0.5
LCALCPOL = .T.
```

The output I got is:

```
Ionic dipole moment: p[ion]=(     0.00000    0.00000     0.00000 ) |e| Angst

Total electronic dipole moment: p[elc]=(     0.00000     0.00000    -0.00000 ) |e| Angst
```

Which, does not match the values we calculated by hand.

One might be tempted to think: "Oh, that's easy, just add an integer number of the lattice vector length to each of the dipole component until they match, no biggie, they are on different branch of the polarization curve!"

Nice thinking, however that does not work in this case (or in any other case when this mismatch happens).


---


## Chapter 2: "The Investigation"

To see how VASP calculates these values, I firstly need to find the exact routine that printed these stuff.

In the `src` directory, enter:

```
grep -oRl "Ionic dipole" ./
```

tells me the printing process is done in `pead.F`. Specifically, in subroutine `PEAD_POLARIZATION_WRITE`:

```
WRITE(IO%IU6,90) IONIC_DIPOLE
CALL XML_VEC_REAL(IONIC_DIPOLE,'PION')
90  FORMAT('            Ionic dipole moment: p[ion]=(',3F12.5,' ) |e| Angst')
```

Now, we have traced it back to `IONIC_DIPOLE` value, which is calculated (conveniently) in the subroutine `PEAD_POLARIZATION_CALC` right above `PEAD_POLARIZATION_WRITE`:

```
CALL POINT_CHARGE_DIPOL(T_INFO,LATT_CUR,P%ZVALF,POSCEN,DIPOLE_DIRECT,RDUM)

IONIC_DIPOLE=0
DO I=1,3
   DO J=1,3
      IONIC_DIPOLE(J)=IONIC_DIPOLE(J)-DIPOLE_DIRECT(I)*LATT_CUR%A(J,I)
   ENDDO
ENDDO
```

Again, we see that `IONIC_DIPOLE` is calculated by dotting `DIPOLE_DIRECT` with lattice vectors `LATT_CUR%A` and `DIPOLE_DIRECT` is calculated by subroutine `POINT_CHARGE_DIPOL`.

Since `POINT_CHARGE_DIPOL` is not in `pead.F` we need to scan the `src` folder again:

```
grep -oRl "POINT_CHARGE_DIPOL" ./
```

`POINT_CHARGE_DIPOL` is in `dipol.F`.

In `POINT_CHARGE_DIPOL` subroutine:

```
NIS=1
typ: DO NT=1,T_INFO%NTYP
   DO NI=NIS,NIS+T_INFO%NITYP(NT)-1
      X= MOD( T_INFO%POSION(1,NI)-POSCEN(1)+10.5_q,1._q)-0.5_q
      Y= MOD( T_INFO%POSION(2,NI)-POSCEN(2)+10.5_q,1._q)-0.5_q
      Z= MOD( T_INFO%POSION(3,NI)-POSCEN(3)+10.5_q,1._q)-0.5_q
```

the code first loops over all element types (`T_INFO%NTYP`), then loops over atoms that belong to that specific type.

Then, it calculates the fractional coordinates of atoms relative to the dipole center (`POSCEN`): +0.5 or -0.5 means the atom is at the boundary of the periodic boundary (now defined by putting `POSCEN` aka `DIPOL` at the center (0.0).

The next few lines of comments are the culprit of our problem:

```
!jF: the atoms at the cell boundary (position -0.5) cause a problem since
!    one also had to add a contribution from the equivalent position at the
!    opposite cell boundary (position +0.5) effectively adding up to zero
!    (due to "position + -position") what should be fixed by following code.
!    Such problems only occur for bulk cells. For isolated molecules etc.
!    there are no atoms at the cell boundary, just vacuum :-). It is also no
!    problem for the quadrupole moment (due to "position**2"). If you still
!    fail to get the correct dipole moment play around with parameter TINY
!    which defines the "thickness of the cell boundary region" ...
            IF (ABS(ABS(X)-0.5_q)<TINY/LATT_CUR%ANORM(1)) X=0
            IF (ABS(ABS(Y)-0.5_q)<TINY/LATT_CUR%ANORM(2)) Y=0
            IF (ABS(ABS(Z)-0.5_q)<TINY/LATT_CUR%ANORM(3)) Z=0
```

It states that, if we have atoms at the boundary (-0.5 or +0.5), we should count both side of the periodic cell and average them to the center of the cell (Oh, and by the way, good emoji jF :-J).

Now, this is really unintended, moving the atoms at the boundary to the center of the cell will add a non-integer copy of the cell vector (aka polarization quantum) to the final value. Specifically, __HALF__ of the polarization quantum is added for __SPECIFIC__ atoms __AT THE BOUNDARY__.

---

## Chapter 3: "The Solution"

Simply comment these lines the three `IF` conditional codes will do the trick, simple as that.

With this modification applied, the polarization I get now is:

```
Ionic dipole moment: p[ion]=(   -31.95600   -31.95600   -32.26800 ) |e| Angst

Total electronic dipole moment: p[elc]=(     0.00000     0.00000    -0.00000 ) |e| Angst
```

Notice that the ionic dipole moment is now exactly the same as what we got from our manual calculations.

All solved!

(Okay maybe not, I still haven't figured out why the electronic part of the polarization does not depend on `IDIPOL`, but that's another adventure, see ya later!)
