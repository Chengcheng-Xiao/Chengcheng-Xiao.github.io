---
layout: post
title: Twitter Cards
date: 2021-10-02
categories: jekyll
description: Adding a bit of flare to your blog posts when sharing on Twitter.
tags: Blog
---

Twitter supports showing custom metadata for websites in a form of "cards". To take full advantage of this feature with jekyll, we are going to use `jekyll-seo-tag` plugin.

Before diving in, the final twitter card should look like:

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Twitter card, testing 1 2 3.<a href="https://t.co/6ewYiXLhDb">https://t.co/6ewYiXLhDb</a></p>&mdash; Chengcheng (@iconxicon) <a href="https://twitter.com/iconxicon/status/1444647398794539010?ref_src=twsrc%5Etfw">October 3, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


## 1. Install

The `jekyll-seo-tag` plugin can be added to a Jekyll site using `gem`. Since I'm not using `Gemfile` for my site, I need to do the following:

```
gem install jekyll-seo-tag  --user-install
```

And then add the following to my `_config.yml`:

```
plugins:
  - jekyll-seo-tag
```

That's it, you are (or I am?) all set!

## 2. Using the plugin

To add an interactive tweet to your blog, simply put the following to the "head" section of your jekyll template. For me this is in `_includes/head.html`:

{% raw %}
```
{% seo %}
```
{% endraw %}

Then, we need to add an image (needs to be in `png`, `jpeg` format, and 1200:600 aspect ration) to `assets/img/` called `jekyll-seo.png` as this is our image for the twitter card.

Then, all we need to do is to set the default card image as the image we just uploaded. To do this, simply add the following to your `_config.yml`:

```
defaults:
  - scope:
      path: ""
    values:
      image: /assets/img/jekyll-seo.png
```

Alternatively, you can also add the following to the front master section of your `index.html` file:

```
image: "/assets/img/jekyll-seo.png"
```

To test the card before you sending our your twitter, use [:link: the card validator](https://cards-dev.twitter.com/validator).

And that's it! Enjoy!
