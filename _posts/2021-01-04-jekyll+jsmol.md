---
layout: post
title: JSmol + Jekyll = Awesome
date: 2021-01-4
categories: jekyll_tutorial
description: Want to learn how to display molecule in posts using JSmol/Jmol? You've come to the right place.
---

Before we dive in, let's take a look at the end result:

<!-- <script src="https://chemapps.stolaf.edu/jmol/jmol.php?source={{site.baseurl}}/assets/other/test/test.cif&script=set bondingVersion 1;set minBondDistance (3);set bondTolerance (0.2);load '' {3 3  1}&inline=1&id=001&isfirst=true&width=650&height=400"></script> -->

- Bulk silicon [structure stored in repo]:
<script src="https://chemapps.stolaf.edu/jmol/jmol.php?source={{site.baseurl}}/assets/other/2021-01-04-jekyll_jsmol/Si_mp-149_computed.cif&script=load '' {2 2 2 };set frank off&inline=1&id=001&isfirst=true&width=650&height=400"></script>

- Caffeine [structure from online database]:
<script src="https://chemapps.stolaf.edu/jmol/jmol.php?model=caffeine&script=set frank off&inline=1&id=002&isfirst=false&width=650&height=400"></script>

Neat hum? Not only do these models are shown in 3D, you can also toggle the viewing angle with your mouse!. I have always found that 2D visualization can be misleading and may cause confusion (in academic paper nonetheless!). IMHO, 3D interactive plots should be included in every modern-day scientific publications. Opinions aside, let me show you how to do this with Jekyll!

In my implementation (and frankly, in most other implementations), [JSmol](http://jmol.sourceforge.net/) does the heavy lifting of constructing 3D models for visualizations using java.
The process is actually fairly easy (don't get me wrong, there are more sophisticated methods out there like the one implemented in [`SeeK-path`](https://www.materialscloud.org/work/tools/seekpath)), simply put in the following lines into your `post.md`:
```html
<script src="https://chemapps.stolaf.edu/jmol/jmol.php?model=caffeine&inline=1&id=002&isfirst=false&width=650&height=400"></script>
```
and the same thing for bulk silicon:
```html
<script src="https://chemapps.stolaf.edu/jmol/jmol.php?source={{site.baseurl}}/assets/other/test/Si_mp-149_computed.cif&script=load '' {2 2 2};set frank off&inline=1&id=001&isfirst=true&width=650&height=400"></script>
```

These commands are html snippets containing scripts which look like complicated. Don't be afraid! Let's break it down:

- .php address. This is described [here](http://wiki.jmol.org/index.php/Jmol_PHP).
```
https://chemapps.stolaf.edu/jmol/jmol.php
```
after the php address, a `?` indicates the following arguments are to be fed to the php address. Each arguments is separated by `&`.
- online source:
```
model=caffeine
```
- [OR] local source:
```
source={{site.baseurl}}/assets/other/test/Si_mp-149_computed.cif
```

- simple script `script=` separated with `;` to:
  - control supercell:
  ```
  load '' {2 2 2}
  ```

  - turn off `Jmol` logo:
  ```
  set frank off
  ```

  - change bond detection algorithm:
  ```
  set minBondDistance (3);set bondTolerance (0.2)
  ```
  - more scripting options can be found [here](https://chemapps.stolaf.edu/jmol/docs/).

- use inline mode:
```
inline=1
```

- if we have multiple plots in one page we need to label each one using:
```
id=002
```
and wether this plot is the first one:
```
isfirst=false
```
- control plot window size.
```
width=650&height=400
```

Okay, that's cool! Want to see something cooler? Try right click the plot, you'll see much more option to control the plot! Also, hover your mouse on one of the atom, you'll see the element label and number of that specific atom. Double click one atom and move you mouse to another atom and double click again, a bond length indicator will pop up. Double click one atom and move you mouse to another atom and click one and move to another atom and double click, a bond angle indicator will popup!

Here's a structure of the SARS-CoV-2 main protease in complex with inhibitor MPI4, enjoy! (BTW, fuck 2020.)

<script src="https://chemapps.stolaf.edu/jmol/jmol.php?pdbid=7DCC&script=load '';set frank off&inline=1&id=003&isfirst=false&width=650&height=400"></script>
