---
layout: post
title: Writing equations in Jeklly
date: 2019-07-04
tags: ["web","code"]
categories: jekyll_tutorial
---

Writing [$$\LaTeX$$] on Jeklly is not hard, but it can be tricky. After some light surfing on the internet, I found what works for me.

### Use [MathJax] for Jekyll

- insert the code in the `_layouts/default.html`

```html
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  tex2jax: {
    inlineMath: [['$','$'], ['\\(','\\)']],
    processEscapes: true
  }
});
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
```

```javascript
/* Some pointless Javascript */
var rawr = ["r", "a", "w", "r"];
```

Note in the last line, a cdn or content delivery network line was used to invoke interpretation of the $$\LaTeX$$ style writing, and eventually convert it to figure.

### Use LaTex to write equations

I found [LaTex/Mathematics] is wildly used to write equations on the website, such as [rmarkdown].

For example, use `$$mean = \frac{\displaystyle\sum_{i=1}^{n} x_{i}}{n}$$` to write

$$mean = \frac{\displaystyle\sum_{i=1}^{n} x_{i}}{n}$$

Use `$$k_{n+1} = n^2 + k_n^2 - k_{n-1}$$` to write

$$k_{n+1} = n^2 + k_n^2 - k_{n-1}$$

### Reference

1. [http://blog.lostinmyterminal.com/webpages/2015/01/09/math-support-in-jekyll.html](http://blog.lostinmyterminal.com/webpages/2015/01/09/math-support-in-jekyll.html)
2. [https://zjuwhw.github.io/2017/06/04/MathJax.html](https://zjuwhw.github.io/2017/06/04/MathJax.html)
3. [https://docs.mathjax.org/en/latest/tex.html](https://docs.mathjax.org/en/latest/tex.html)

[$$\LaTeX$$]: https://www.latex-project.org/
[MathJax]:https://www.mathjax.org/
[LaTex/Mathematics]:https://en.wikibooks.org/wiki/LaTeX/Mathematics) is wildly used to write equations on the website, such as [rmarkdown](http://rmarkdown.rstudio.com/authoring_basics.html
[rmarkdown]:http://rmarkdown.rstudio.com/authoring_basics.html
