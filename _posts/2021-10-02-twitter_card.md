---
layout: post
title: Tweet quotes
date: 2021-10-02
categories: jekyll
description: Quoting Tweets elegantly with jekyll-twitter-plugin.
tags: Blog
---

`jekyll-twitter-plugin` allows easy and fast tweet quoting using liquid tags with Jekyll. For example, the quoted tweet will be shown as:

{% twitter https://twitter.com/rubygems/status/518821243320287232 %}

You can find the Github repo for `jekyll-twitter-plugin` [:link: here](https://github.com/rob-murray/jekyll-twitter-plugin).

## 1. Install

The `jekyll-twitter-plugin` plugin can be added to a Jekyll site using `gem`. Since I'm not using `Gemfile` for my site, I need to do the following:

```
gem install jekyll-twitter-plugin  --user-install
```

And then add the following to my `_config.yml`:

```
plugins:
  - jekyll-twitter-plugin
```

That's it, you are (or I am?) all set!

## 2. Using the plugin

To add an interactive tweet to your blog, simply put the following to your `.md` file:

{% raw %}
```
{% twitter https://twitter.com/rubygems/status/518821243320287232 %}
```
{% endraw %}

The syntax is:

{% raw %}
```
{% plugin_type twitter_url *options %}
```
{% endraw %}

where you can get `twitter_url` from by clicking the share button and then `copy link to Tweet` button on Twitter.

There are several `options` to tune the style of the quoting tweet, to see them, click [:link: here](https://developer.twitter.com/en/docs/twitter-for-websites/embedded-tweets/guides/embedded-tweet-parameter-reference).


For example, I like to use:

```
align=center
```

to center the tweet card:

{% twitter https://twitter.com/rubygems/status/518821243320287232 align=center %}


## Automatic theme

The theme, however, does not change automatically upon switching the `prefers-color-scheme` html tag.
To overcome this, I found this [:link: blog post] from Luke Lowrey that by adding the following to your `_layouts/default.html`:

```
<!-- automatic change theme for jekyll-twitter-plugin liquid tag -->
<script>
var storedTheme = localStorage.getItem('theme') || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

setTimeout(function() {
  var targetTheme = storedTheme == "dark" ? "light" : "dark";
  switchTweetTheme(targetTheme, storedTheme);
}, 1000);

function switchTweetTheme(currentTheme, targetTheme) {
  var tweets = document.querySelectorAll('[data-tweet-id]');

  tweets.forEach(function(tweet) {
    var src = tweet.getAttribute("src");
    tweet.setAttribute("src", src.replace("theme=" + currentTheme, "theme=" + targetTheme));
  });
}
</script>
```

We can automate the theme switching. However, note that it only works statically meaning if you change `prefers-color-scheme` after the website is loaded, you'll need to refresh the page to see the change.

That's it! Easy peasy! Enjoy sharing your tweets!
