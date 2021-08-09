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
[LaTex/Mathematics]:https://en.wikibooks.org/wiki/LaTeX/Mathematics
[rmarkdown]:http://rmarkdown.rstudio.com/authoring_basics.html

## 2021-08-08 update

Apparently, mathjax v3 is now available [🔗link](https://www.mathjax.org/?utm_source=cdnjs&utm_medium=cdnjs_link&utm_campaign=cdnjs_library#gettingstarted).
To use it, simply change:

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

to

```html
<script type="text/javascript">
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    processEscapes: true
  }
};
</script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
```
However, I find the new version doesn't automatically render horizontal scroll bar for long equations.

---

$\KaTeX$, as an alternative to [MathJax], can render equations with HTML format and it's much faster. Following [🔗this](https://www.xuningyang.com/blog/2021-01-11-katex-with-jekyll/) blog post, I was able to add it to my blog.

To use $\KaTeX$, add the following to `_config.yml`:
```
kramdown:
  math_engine: katex
```

Then add the following to the end of `_include/head.html`:

```html
<!--KaTeX-->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.13.13/dist/katex.min.css" integrity="sha384-RZU/ijkSsFbcmivfdRBQDtwuwVqK7GMOw6IMvKyeWL2K5UAlyp6WonmB8m7Jd0Hn" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.13.13/dist/katex.min.js" integrity="sha384-pK1WpvzWVBQiP0/GjnvRxV4mOb0oxFuyRxJlk6vVw146n3egcN5C925NCP7a7BY8" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.13.13/dist/contrib/auto-render.min.js" integrity="sha384-vZTG03m+2yp6N6BNi5iM4rW4oIwk5DfcNdFfxkk9ZWpDriOkXX8voJBFrAO7MpVl" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
          // customised options
          // • auto-render specific keys, e.g.:
          delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
              {left: '\\(', right: '\\)', display: false},
              {left: '\\[', right: '\\]', display: true}
          ],
          // • rendering keys, e.g.:
          throwOnError : false
        });
    });
</script>
```

and put the following to `css/main.scss` file to add scroll bar to long equations:

```css
.katex-display > .katex {
  display: inline-block;
  white-space: nowrap;
  max-width: 100%;
  overflow-x: scroll;
  overflow-y: visible;
  text-align: initial;
}
```
