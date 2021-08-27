---
layout: post
title: Compile VASP[v6.1.2] with libxc[v4.3.4]
date: 2020-12-11
tags: ["VASP compilation"]
categories: Other
description: A tutorial on how to compile VASP[v6.1.2] with libxc[v4.3.4].
---

## Reason

I cannot find any information on how to compile VASP with libxc on the VASP wiki, so I'll document my experience of it here.

**Please note that VASP [v6.1.2] does not work with the latest version of libxc[v5.0.0], but it does support libxc[v4.3.4]

## Compile libxc
First, compile libxc[v4.3.4]:
1. Download the source code from [:link: HERE](https://gitlab.com/libxc/libxc/-/archive/4.3.4/libxc-4.3.4.tar.gz).
2. untar the tarball with:
```
tar zxvf libxc-4.3.4.tar.gz
```
3. generate configure:
```
cd libxc-4.3.4
autoreconf -i
```
4. configure and compile. Note that I'm using intel compilers.
```
./configure --prefix=PATH/TO/LIBXC CC=icc FC=ifort
make
make check
make install
```

## Compile VASP[v6.1.2] w/ libxc[v4.3.4]
To compile VASP[v6.1.2] with libxc[v4.3.4], modify your makefile.include file:
1. add `-DUSELIBXC` to the precompiler flags (`CPP_OPTIONS`).
2. append path to libxc's include directory to `INCS`:
```
INCS       =-I$(MKLROOT)/include/fftw -I/PATH/TO/LIBXC/include
```
3. append compiled librarys to `LLIBS`:
```
LLIBS      = $(SCALAPACK) $(LAPACK) $(BLAS) /PATH/TO/LIBXC/lib/libxcf90.a /PATH/TO/LIBXC/lib/libxc.a
```
4. compile as usual.

## Usage
To use libxc with VASP[v6.1.2], add the following to your INCAR file:
1. `LIBXC1`: id/name of the exchange part
2. `LIBCX2`: id/name of the correlation part

The definition of the id/name for `LIBXC1` and `LIBXC2` can be found [HERE](https://www.tddft.org/programs/libxc/functionals/).
And yes, you can use either the name or the id of your desired xc functional.
