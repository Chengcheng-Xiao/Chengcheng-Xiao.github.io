---
layout: post
title: Adomonition in Jekyll
date: 2024-09-29
categories: jekyll
description: Adding admonition to your jekyll blog.
tags: Blog
---

Admonitions are a great way to draw attention to important information in your
blog. They are often used to highlight warnings, tips, notes, and other
important information. In this post, I will show you how to add admonitions to
your Jekyll blog using html and css based on 
[:link: this blog](https://www.adamsdesk.com/posts/admonitions-jekyll/) and 
[:link: this repo](https://github.com/sercangezer/jekyll-admonitions-css). 

<!-- Before diving in, the final twitter card should look like:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Twitter card, testing 1 2 3.<a href="https://t.co/6ewYiXLhDb">https://t.co/6ewYiXLhDb</a></p>&mdash; Chengcheng (@iconxicon) <a href="https://twitter.com/iconxicon/status/1444647398794539010?ref_src=twsrc%5Etfw">October 3, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> -->


## 1. Install

Download `admonition.html` and put it in your `_includes` folder. Then, download
`_admonition.scss` and put it in your `_sass` folder and add the following to
your `main.scss`:

```scss
@import "_admonition";
```
However, in my case, I have to add the folloiwng to `css/main.scss` instead:
```scss
@import
        "normalize",
        "base",
        "layout",
        "color",
        "admonition"
;
```


Finally, download the [icons from the
repo](https://github.com/sercangezer/jekyll-admonitions-css/tree/main/assets/img/icons)
and put them in your `assets/img/icons` folder. And that's it! You are all set!


## 2. Using the plugin

To add an interactive tweet to your blog, simply put the following to the body
of your blog post:

{% raw %}
```
{% include admonition.html type="note" title="Info" body="This is information intended to draw attention." %}
```
{% endraw %}

The list of admonitions types that you can use are:

{% include admonition.html type="note" title="note" body="This is information intended to draw attention." %}
{% include admonition.html type="abstract" title="abstract" body="This is information intended to draw attention." %}
{% include admonition.html type="info" title="Info" body="This is information intended to draw attention." %}
{% include admonition.html type="tip" title="tip" body="This is information intended to draw attention." %}
{% include admonition.html type="success" title="success" body="This is information intended to draw attention." %}
{% include admonition.html type="question" title="question" body="This is information intended to draw attention." %}
{% include admonition.html type="warning" title="warning" body="This is information intended to draw attention." %}
{% include admonition.html type="failure" title="failure" body="This is information intended to draw attention." %}
{% include admonition.html type="danger" title="danger" body="This is information intended to draw attention." %}
{% include admonition.html type="bug" title="bug" body="This is information intended to draw attention." %}
{% include admonition.html type="example" title="example" body="This is information intended to draw attention." %}
{% include admonition.html type="quote" title="quote" body="This is information intended to draw attention." %}

And that's it! Enjoy!

