---
layout: post
title: JSmol + Jekyll = Awesome
date: 2021-01-4
categories: jekyll
description: Want to learn how to display molecule in posts using JSmol/Jmol? You've come to the right place. This post provides a easy way to implement (add) JSmol to your Jekyll blogs!
tags: Blog
---

Before we dive in, let's take a look at the end result:

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

<!-- Here's a structure of the SARS-CoV-2 main protease in complex with inhibitor MPI4, enjoy! (BTW, fuck 2020.)

<script src="https://chemapps.stolaf.edu/jmol/jmol.php?pdbid=7DCC&script=load '';set frank off&inline=1&id=003&isfirst=false&width=650&height=400"></script> -->

##Update 2021-03-07

I found the old implementation is not food for mobile viewing, specifically, the width of the window is too large to be shown in mobile devices.
To overcome this, we can use `iframe` to embed it.

For example:
<iframe src="https://chengcheng-xiao.github.io/jsmol-models/embeddable.html#
molecule={{site.baseurl}}/assets/other/2021-01-04-jekyll_jsmol/Si_mp-149_computed.cif
&generic=set,bondTolerance,0.1
&supercell=3,3,3
&generic=set,frank,off
&generic=set,antialiasDisplay,true
&generic=set,background,white
&generic=set,displayCellParameters,FALSE
&generic=select,La;color,atoms,green;select,off
&generic=set,pickingStyle,SELECT,DRAG"
style="width: 100%; height: 400px"
scrolling="no"
marginwidth="0"
marginheight="0"
frameborder="0"
vspace="0"
hspace="0">
</iframe>

The whole script I used here is:

```html
<iframe src="https://chengcheng-xiao.github.io/jsmol-models/embeddable.html#
molecule={{site.baseurl}}/assets/other/2021-01-04-jekyll_jsmol/Si_mp-149_computed.cif
&generic=set,bondTolerance,0.1
&supercell=3,3,3
&generic=set,frank,off
&generic=set,antialiasDisplay,true
&generic=set,background,white
&generic=set,displayCellParameters,FALSE
&generic=select,La;color,atoms,green;select,off
&generic=set,pickingStyle,SELECT,DRAG"
style="width: 100%; height: 400px"
scrolling="no"
marginwidth="0"
marginheight="0"
frameborder="0"
vspace="0"
hspace="0">
</iframe>
```

the old `https://chemapps.stolaf.edu/jmol/jmol.php` cannot be used since its rejected automatically be the iframe protocal.
Instead, I'm using a embeddable version from [my repo deployed using Github page](https://chengcheng-xiao.github.io/jsmol-models/embeddable.html)

This implementation has different behaviour than the old one.
Full details about this implementation can be found [HERE](https://github.com/Chengcheng-Xiao/jsmol-models/blob/gh-pages/embeddable.html#).

Here, I'll do a simple line-by-line explanation:

1. all source code is wrapped in the string called `src`.
2. control parameters are behind `#` and linked by `&`.
3. the style of the ifram can be controled using:

```html
style="width: 100%; height: 400px"
scrolling="no"
marginwidth="0"
marginheight="0"
frameborder="0"
vspace="0"
hspace="0"
```

4. the previous [structure from online database] method cannot be used in this implementation,
and we have to always use the whole URL:

```html
molecule=FULL_URL
```

5. generic script can be called using `generic=`.
6. supercell creation is a specific command (it needs brakets `{}`) so I made a specific command for this:

```html
supercell=3,3,3
```
