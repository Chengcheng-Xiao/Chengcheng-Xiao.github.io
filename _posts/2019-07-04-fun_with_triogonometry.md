---
layout: post
title: Little math side-quest [No.1]
date: 2019-07-04
tags: ["Math"]
categories: Side_projects
description: A geomotry problem that's seemingly easy to solve, yet cannot be solved without some "advanced" tools. Solved with integration and trigonometry.
---

## Problem

![]({{site.baseurl}}/assets/img/post_img/2019-07-04-img1.svg)
{: .center}

__Find the area of the shaded part.__

----

At first, I tried to solve this using simple geometry without trigonometry, but eventually gave up.

----
## Solution
Then, brining the big gun:

1. Using integration:

    - First, define a coordinate system:

    ![Alt text]({{site.baseurl}}/assets/img/post_img/2019-07-04-img2.svg)
    {: .center}

    - Then, write the function describing the blue circle and the red arc.
      * Blue circle: $$x^2+(y+5*\sqrt{2})^2=100$$
      * Red arc: $$x^2+(y)^2=25$$

    - The coordinate of two crossing point can be found:
      * Point A: $$[-\frac{5\sqrt{\frac{7}{2}}}{2},\frac{5}{2\sqrt{2}}]$$
      * Point B: $$[\frac{5\sqrt{\frac{7}{2}}}{2},\frac{5}{2\sqrt{2}}]$$

    - Using the $$x$$ corrdinate of point A and B as lower and upper limit, the integration could be written as:

      $$\frac{Area_{total}}{2}=\int^A_B [\sqrt{25-x^2}-(\sqrt{100-x^2}-5\sqrt{2})]  dx $$

    - And the total area:

      $$Area_{total}=2*\frac{\sqrt{25}}{2}[\sqrt{7}-8\arcsin{(\frac{\sqrt{\frac{7}{2}}}{4})}+2\arcsin{(\sqrt{7})}]$$

      or: $$29.2763 cm^2$$

2. Using trigonometry:
    - Auxiliary lines can be usefull:

    ![Alt text]({{site.baseurl}}/assets/img/post_img/2019-07-04-img3.svg)
    {: .center}

    - We know:

       $$AC=CB=10$$

       $$AD=DB=5$$

       $$CD=5\sqrt{2}$$
    - Using Cosin Law, we get the angle of $$\angle ACD$$:

      $$\angle ACD=\arccos{\frac{AC^2+CD^2-AD^2}{2AC*CD}}$$

    - Hence the area of sector ACBFA:

      $$Area_{ACBFA}=\frac{2*{\angle ACD}}{2 \pi } \pi  10^2 $$

    - The area of the triangle ACBA:

      $$Area_{ACBA}=\frac{1}{2} \text{AC}*\text{CB}*\sin (2*\text{$\angle $ACD})$$

    - Area ABFA can be obtained:

      $$Area_{ABFA}=Area_{ACBFA}-Area_{ACBA}$$

    - Now we perform similar procedure to obtain area of ABEA:

      $$\text{$\angle $ADC}=\arccos\left(\frac{\text{AD}^2+\text{DC}^2-\text{AC}^2}{2 \text{AD}*\text{DC}}\right)$$

      $$\text{$\angle $ADB}=2 (\pi -\text{$\angle $ADC})$$

      $$Area_{ADBEA}=\frac{\pi* 5^2 * \text{$\angle $ADB}}{2 \pi }$$

      $$Area_{ADBA}=\frac{1}{2} \text{AD}^2 \sin (\text{$\angle $ADB})$$

      $$Area_{ABEA}=Area_{ADBEA}-Area_{ADBA}$$

      $$Area_{AFBEA}=2*Area_{ABEA}-Area_{ABFA}$$

    - Result:

      $$29.2763 cm^2$$

It is intriguing that this problem cannot be simply solved without trigonometry.

I've wrote down the whole process in Wolfram Mathematica for [download].

[download]:{{site.baseurl}}/assets/other/2019-07-04-Little_math_side-quest.1.nb
