---
title: News
permalink: /news/
---
<div class="wrap">
  <header class="page-head">
    <h1>News</h1>
    <p class="meta">Follow updates with the <a href="{{ '/feed.xml' | relative_url }}">news feed</a>, or subscribe to the <a href="{{ site.mailing_list }}">mailing list</a>.</p>
  </header>
  {% include post-list.html posts=site.posts excerpts=true %}
</div>
