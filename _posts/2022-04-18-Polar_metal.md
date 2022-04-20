---
layout: post
title: Polar metals and hybrid Wannier functions
date: 2022-04-18
categories: Post
description: Polar metals are metallic systems that have non-centrosymmetric polar structures. It has been theorized to exist and experimentally demonstrated to be possible. This post discusses the options of calculating the polarization of these materials using Berryphase or Wannier charge center method.
tags: DFT
---
## What is a "Polar metal"?
> Polar metals are polar systems that are metallic, i.e. systems with Fermi energy crossing one or seveal bands across the Brillioun zone (Fermi crossing).

This behavior is unusual because the long range Coulomb interatcions which are usually considered to be the driving force of polar distortion is screened by having itenary electrons. Nevertheless, a whole lot of polar metals have been either experiementally identified or theoretically predicted.

The explaination of such behavior currently relies on the so-called “decoupled electron mechanism” (DEM) model. [:link: Proposed by Puggioni and Rondinelli in 2014](https://www.nature.com/articles/ncomms4432), the DEM model states that the existence of polar metals relies on the coupling between the electrons at the Fermi level, and the phonons responsible for removing inversion symmetry to be weak. I.e. the origin of the conductivity and the origin of polar distortion are not related. For example, in some polar metal the conduction is constrain within a plane and the polarization is out-of-plane.

The usual Berryphase calculations are conducted by setting a string of k-points along a particular k direction ($k_z$) while sampling the other two k directions ($k_x$ and $k_y$). After obtaining the WCC along each string, average the results with respect to the k-point weight along $k_x$ and $k_y$.

![img1]({{site.baseurl}}/assets/img/post_img/2022-04-18-img1.png){: .center}

For polar metals that are conducting at one direction and insulating at another direction, people argues that one can calculate the polarization because the Berryphase (Wannier charge center) is still well defined in the out-of-plane direction $k_z$.

For a review of polar metals, I recommend [the work of W. X. Zhou and A. Ariando](https://iopscience.iop.org/article/10.35848/1347-4065/ab8bbf/meta).

## Polarization conundrum

However, I don't think this should work, even theoretically. As long as there are hopping between atoms along the polarization direction (let's be real, there'll always hoppings in all directions😬), there is going to be band dispersion. And as long as there is band dispersion, we can always find a k-point (in conductive plane) that are close to the Fermi crossing so that the bands cross the Fermi level along the polarization direction.

To illustrate this point, imagine we have a band crossing the Fermi level as:

![img2]({{site.baseurl}}/assets/img/post_img/2022-04-18-img2.png){: .center}

And near the Fermi crossing point, along $k_c$, we have a downward dispersion, then we can choose a k-point where the band energy is slightly above the Fermi level, so that the dispersion along $k_c$ will get cut by the Fermi level.

Note that this choice is arbitrary, we can always find such k-point that are close enough to the Fermi crossing so that the dispersion along $k_c$ direction will cause problem for us.

This tells us that, as long as we have a perfect large crystal that's conductive along some direction, we can always expect to have some conductive properties along other directions. (Thinking about this, the number of electrons that are actually there to screen the polarization along this axis can potentially estimated by calculating the percentage of these conductive k-points of all k-points?) So, theoretically, as long as there's band crossing (no matter where they appear), polarization cannot be calculated.

However, technically, we can still calculate the polarization as long as we don't sample the k-points around the Fermi crossing I mentioned.

## Berryphase method
VASP's `LBERRY` can (theoretically) be used to do this calculation. This tag is used in combination with `IGPAR` and `NPPSTR` where `IGPAR` determines direction (in k-space) we want to calculate the polarization and `NPPSTR` determines how many k-points along the directions we want to calculate are used.

To illustrate the working principle of these routine, let's assume we want to calculate the polarization along $k_c$ direction.
First, if we keep the automatic k-point generation in `KPOINTS` file, like:
```
K-point
0
G
3      3      3
0      0      0
```

Then, VASP will single out unique $k_a$ and $k_b$ combinations, then assign `NPPSTR` points along $k_c$ form $0$ to $0.5$. The total number of k-points is also recalculated.
Internally, the k-points is ordering loops over the `IGPAR` direction the fastest:
```
      DO ISTR=1,NSTR
         DO IK=1,NPPSTR
            NK=NK+1
            KPTSTR(IK,ISTR)=NK
         ENDDO
      ENDDO
```

Then, the code resets `ISMEAR` and `SIGMA`:
```
! overwrite user defaults for ISMEAR and SIGMA
! this should be save in all cases
         ISMEAR  = 0
         SIGMA   = 0.0001
```

Then, the code runs as usual with this sets of k-points and smearing. After SCF converged, we get a set of wavefunctions and occupations.

After the convergence of SCF cycle, at each $k_a$ and $k_b$ along $k_c$ direction, the berry connection is calculated between neighboring k-points. Corresponding routine can be found in `elpol.F`:
Note that along each string, the last k-point is connected to the first k-point:
```
         NK=KPTSTR(IK,ISTR)
         IF (IK.LT.NPPSTR) THEN
            NKP=KPTSTR(IK+1,ISTR)
            IG=0
         ELSE
            NKP=KPTSTR(1,ISTR)
            IG=0
            IG(IGPAR)=-1
         ENDIF
```

And finally the polarization is calculated by summing over the Berryphase over the weight of $k_a$ and $k_b$.

Often, when calculating systems with Fermi level crossing the band structure, we would see error like:

```
 Error in subroutine BERRY: did not find all determinants

Matrix CMK is not an nxn matrix for
ISTR =    1 j =    0
```

This is caused by the code identifying an occupation change along one string of k-points. In the following code, VASP is trying to find the number of occupied band between two nearest k-points:
```
         N=0;MN=0
         loop_n: DO N1=1,WDES%NB_TOT
            IF (W%FERTOT(N1,NK,ISP).LE.TINY) CYCLE loop_n
            N=N+1;M=0
            loop_m: DO N2=1,WDES%NB_TOT  
               IF (W%FERTOT(N2,NKP,ISP).LE.TINY) CYCLE loop_m
               M=M+1
               CMK(N,M)=CMK_(N1,N2)
            ENDDO loop_m
            MN=MN+M
         ENDDO loop_n
```

we see that in the end `N` and `M` corresponds to the number of occupied bands at `NK` and `NKP` points. If they are different, then:

```
         IFAIL=0
         IF (MN.EQ.N**2) THEN
		 ...
		     ELSE
            IFAIL=1     ! Matrix M_k is not a nxn matrix
         ENDIF
		   IF (IFAIL.NE.0) GOTO 1000 ! Error in calculation of determinant

```

will raise the error.

`ISTR` in the error is the label of of $k_a$ and $k_b$ subset, and `j` is the k-point label along the k-string.

We can try playing with the k-points a bit but this is not a "guaranteed-to-work" method since the location of the Fermi crossing differs for different materials and the convergence can get spoiled if using too sparse of a k-grid.

<!-- ## changing k-points
I've tried changing the k-points so that we avoid those that have crossing along the polarization direction, however, if we do this then the Fermi level calculated will move and the occupation will move as well.

## fixing occupation
We can, in theory, we can use  `ISMEAR=-2` and `FERWE` to fix the occupation by commenting out:

```
! overwrite user defaults for ISMEAR and SIGMA
! this should be save in all cases
         ISMEAR  = 0
         SIGMA   = 0.0001
```

With this we can change the occupation of specific k-points so that they are consistant over the polarizatio direction.
However, if we do this, it seems like the occupation in BERRY module is still not fixed... not sure why, needs more investigation.

## fixing both
We can change the k-points so that we can ignore the k-points that have band crossing the fermi level and to circumvent the changing fermi level after we change the k-point set, we need to fix the occupation.

But because the fixing occupation does not work, this does not work as well. -->

## Hybrid Wannier functions
Alternatively, we can use hybrid Wannier functions (and their centers) to calculate the polarization.

First let's remember the Wannier transformation (with subspace mixing):

$$
\ket{\phi_{\vec R,n}} = \int_\text{BZ} e^{-i \vec k \vec R} \sum_m U^{\vec k}_{mn} \ket{\psi_{\vec k, m}} d\vec k \tag{1}
$$

where $\phi$ is the Wannier functions, $\vec R$ labels the cell index, $n$ is the index of the Wannier functions, $m$ is the index of the Bloch WF $\psi$.

Inversely, one can obtain the Bloch functions from a set of Wannier functions by:

$$
\ket{\psi_{\vec k',m'}} = \int_\text{all cell} e^{i \vec k' \vec R} \sum_n U^{\vec k *}_{nm'} \ket{\phi_{\vec R,n}} d \vec R \tag{2}
$$

we can see this inverse transformation works because if we substitute $\phi$ in Eq. 2 with Eq. 1, we get:

$$
\begin{aligned}
\ket{\psi_{\vec k',m'}} &= \int_\text{all cell} e^{i \vec k' \vec R} \sum_n U^{\vec k *}_{nm'} \ket{\phi_{\vec R,n}} d \vec R \\

&=  \int_\text{all cell} e^{i \vec k' \vec R} \sum_n U^{\vec k' *}_{nm'} \int_\text{BZ} e^{-i \vec k \vec R} \sum_m U^{\vec k}_{mn} \ket{\psi_{\vec k, m}} d\vec k d \vec R \\


&=  \int_\text{BZ} \sum_n U^{\vec k' *}_{nm'} \left [ \int_\text{all space} e^{-i (\vec k' - \vec k) \vec R} d \vec R \right ] \sum_m U^{\vec k}_{mn} \ket{\psi_{\vec k, m}} d\vec k \\

&=  \int_\text{BZ} \sum_n U^{\vec k' *}_{nm'} \delta(\vec k' - \vec k) \sum_m U^{\vec k}_{mn} \ket{\psi_{\vec k, m}} d\vec k \\

&=  \sum_n U^{\vec k' *}_{nm'}  \sum_m U^{\vec k'}_{mn} \ket{\psi_{\vec k', m}}  \\

&= \sum_{nm} U^{\vec k' *}_{nm'} U^{\vec k'}_{mn} \ket{\psi_{\vec k', m}} \\

&= \ket{\psi_{\vec k', m'}}

\end{aligned}
$$


The formal definition of the hybrid Wannier functions is:

$$
\begin{aligned}
\ket{\phi_{R_c, k_a, k_b, n}} &= \int e^{-i k_c R_c} \sum_m U^{\vec k}_{mn} \ket{\psi_{\vec k, m}} d k_c \\
&= \int e^{-i k_c R_c} \sum_m U^{k_a,k_b,k_c}_{mn} \ket{\psi_{k_a,k_b,k_c, m}} d k_c
\end{aligned} \tag{3}
$$

In Eq. 3, we have only Wannier transformed one direction $k_c$ and left the ohter two directions $k_a$ nad $k_b$ as individual parameters. This means we'll get different "Wannier centers" along $c$ direction when choosing different $k_a$ nad $k_b$.

We can also get this difinition from a set of "fully transformed" Wannier functions $\phi_{\vec R,n}$:

$$
\begin{aligned}
\ket{\phi_{R_c, k_a, k_b, n}} &= \int e^{ik_a' R_a} \int e^{ik_b' R_b} \ket{\phi_{\vec R,n}} dR_a dR_b\\

&= \int e^{ik_a' R_a} \int e^{ik_b' R_b} \ket{\phi_{R_a, R_b, R_c ,n}} dR_a dR_b\\
\end{aligned} \tag{4}
$$

Note that in Eq. 4, we no longer need $U^{\vec k *}_{nm'}$ like in Eq. 2, this is because we are going to keep using $n$ instead of switching to $m'$.

Eq. 4 also tells us that once we have the fully transformed Wannier functions, reverting to the hybrid form will not affect the Wannier charge center along the direction that hasn't been inverse transformed (here $c$ direction).

The good thing about $\ket{\phi_{R_c, k_a, k_b, n}}$ is that it depends on $k_a$ and $k_b$. This comes in handy for polar metals where bands crossover the Fermi level along $k_a$ and $k_b$ plane. For example, at $k_a$ and $k_b$ we have $n$ bands occupied, but at $k_a'$ and $k_b'$ we have $n+1$ bands occupied. If we want to calculate the polarization along $c$ axis, we need to calculate the WCCs along a string of k-points in $k_c$ direction at each set of $k_a$ and $k_b$ points.

To actually calculate the total polarization along the "non-conductive" axis, we first needs to divide the $k_a$ and $k_b$ plane by the number of bands occupied at each point.

![img1]({{site.baseurl}}/assets/img/post_img/2022-04-18-img3.png){:height="400px" .center}

For each subset, the WCC can be obtained using Eq. 4. Specifically, we need to Wannierize the system with the number bands equal to the number of occupied bands in the subset. __Note that this Wannierization process should be done with all k points considered (including $k_c$) for each $k_a$ and $k_b$ set.__

Specifically, for example, if I want to get the WCCs at the $k_a$ and $k_b$ where $n$ bands are occupied. I need to Wannierize the whole system by considering $n$ Wannier functions and get WCCs in three dimension, the $c$ component is the one that we are looking for. Then, moving to the next set of $k_a$ and $k_b$s where $n+1$ bands are occupied, I need to Wannierize the whole system again but with $n+1$ Wannier functions.

Once we've obtained the WCCs for each subset of the BZ, we can weight them by the k-points' weight and obtain the finally WCCs along $c$ direction of the system.

## Direct integration of Charge density.

For systems that are non-conductive along one direction, it is possible calculate the polarization by doing a planar average of the __conduction__ charge density (one can obtains this using [:link: band decomposed charge densities](https://www.vasp.at/wiki/index.php/Band_decomposed_charge_densities)) along the non-conductive direction. However, this only works if there's a clear "near zero" point cutting the planes apart so that the charge density center is well defined.

For example, the conduction charge density of $\mathrm{Bi_5Ti_5O_{17}}$ goes down to around zero as seen in [:link: the work of Alessio Filippetti and co-workers](https://www.nature.com/articles/ncomms11211):

![img1]({{site.baseurl}}/assets/img/post_img/2022-04-18-img4.png){:height="70%" width="70%" .center}

[:link: Pankaj Sharma and co-workers](https://www.science.org/doi/10.1126/sciadv.aax5080) also used this method on $\mathrm{WTe_2}$ systems and they find that the electron pocket is more or less centro-symmetric so even though they have significant value on all points along $c$ axis, electron conduction channel doesn't contribute to the polarization and only hole channel contributes:

![img1]({{site.baseurl}}/assets/img/post_img/2022-04-18-img5.png){:height="45%" width="45%" .center}

This result is not that surprising. To understand it, we need to first consider Maximally Localized Wannier function (MLWF). What MLWF does is essentially finding the optimum band connections so that we can regroup the bands, get rid of the band crossing and obtain a set of   wavefunctions that give rises to a well localized Wannier functions.

Now, not all Wannier functions contributes to the polarization (some of then have centers that don't move much), which means some of the (re-organized) bands does not contribute to the polarization either. If we can single out those bands, then combined with the knowledge of occupation in k-space we can obtain the polarization too.
