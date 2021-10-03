---
layout: post
title: Tweet quotes
date: 2021-10-02
categories: jekyll
description: Quoting Tweets elegantly with jekyll-twitter-plugin.
tags: Blog
---

`jekyll-twitter-plugin` allows easy and fast tweet quoting using liquid tags with Jekyll. For example, the quoted tweet will be shown as:

<!--  twitter https://twitter.com/rubygems/status/518821243320287232  -->

<div class="twitter-tweet twitter-tweet-rendered" style="display: flex; max-width: 550px; width: 100%; margin-top: 10px; margin-bottom: 10px;"><iframe id="twitter-widget-1" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" class="" title="Twitter Tweet" src="https://platform.twitter.com/embed/Tweet.html?dnt=false&amp;embedId=twitter-widget-1&amp;features=eyJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2hvcml6b25fdHdlZXRfZW1iZWRfOTU1NSI6eyJidWNrZXQiOiJodGUiLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X3NwYWNlX2NhcmQiOnsiYnVja2V0Ijoib2ZmIiwidmVyc2lvbiI6bnVsbH19&amp;frame=false&amp;hideCard=false&amp;hideThread=false&amp;id=518821243320287232&amp;lang=en&amp;origin=http%3A%2F%2F127.0.0.1%3A4000%2Fjekyll%2F2021%2F10%2F02%2Ftwitter_card.html&amp;sessionId=8e6d68d0172f6a97f655f8d2177cc7f97cda1fa0&amp;theme=dark&amp;widgetsVersion=fcb1942%3A1632982954711&amp;width=550px" data-tweet-id="518821243320287232" style="position: static; visibility: visible; width: 550px; height: 273px; display: block; flex-grow: 1;"></iframe></div> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

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

<div class="twitter-tweet twitter-tweet-rendered" style="width: 100%; margin: 10px auto; display: flex; max-width: 550px;"><iframe id="twitter-widget-0" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" class="" title="Twitter Tweet" src="https://platform.twitter.com/embed/Tweet.html?dnt=false&amp;embedId=twitter-widget-0&amp;features=eyJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2hvcml6b25fdHdlZXRfZW1iZWRfOTU1NSI6eyJidWNrZXQiOiJodGUiLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X3NwYWNlX2NhcmQiOnsiYnVja2V0Ijoib2ZmIiwidmVyc2lvbiI6bnVsbH19&amp;frame=false&amp;hideCard=false&amp;hideThread=false&amp;id=518821243320287232&amp;lang=en&amp;origin=http%3A%2F%2F127.0.0.1%3A4000%2Fjekyll%2F2021%2F10%2F02%2Ftwitter_card.html&amp;sessionId=04baceefc9d70dceec68ddc8a31790a074301876&amp;theme=light&amp;widgetsVersion=fcb1942%3A1632982954711&amp;width=550px" data-tweet-id="518821243320287232" style="position: static; visibility: visible; width: 550px; height: 273px; display: block; flex-grow: 1;"></iframe></div>

<!-- {% https://twitter.com/rubygems/status/518821243320287232 align=center %} -->


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

## Update
Okay, that's actually not it... Github pages has it's own list of allowed jekyll plugins, and it does not include `jekyll-twitter-plugin`. However, you still can add the card directly to your `.md` file using html (with iframe and some javascript):


```html
<div class="twitter-tweet twitter-tweet-rendered" style="width: 100%; margin: 10px auto; display: flex; max-width: 550px;"><iframe id="twitter-widget-0" scrolling="no" frameborder="0" allowtransparency="true" allowfullscreen="true" class="" title="Twitter Tweet" src="https://platform.twitter.com/embed/Tweet.html?dnt=false&amp;embedId=twitter-widget-0&amp;features=eyJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2hvcml6b25fdHdlZXRfZW1iZWRfOTU1NSI6eyJidWNrZXQiOiJodGUiLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X3NwYWNlX2NhcmQiOnsiYnVja2V0Ijoib2ZmIiwidmVyc2lvbiI6bnVsbH19&amp;frame=false&amp;hideCard=false&amp;hideThread=false&amp;id=518821243320287232&amp;lang=en&amp;origin=http%3A%2F%2F127.0.0.1%3A4000%2Fjekyll%2F2021%2F10%2F02%2Ftwitter_card.html&amp;sessionId=04baceefc9d70dceec68ddc8a31790a074301876&amp;theme=light&amp;widgetsVersion=fcb1942%3A1632982954711&amp;width=550px" data-tweet-id="518821243320287232" style="position: static; visibility: visible; width: 550px; height: 273px; display: block; flex-grow: 1;"></iframe></div>
```
