---
title: Network
permalink: /network/
robots: noindex
sitemap: false
---
{%- assign regions = site.data.network | group_by: "region" -%}
{%- assign countries = site.data.network | map: "country" | uniq -%}
<div class="wrap">
  <header class="page-head">
    <h1>The ICMNS network</h1>
    <p class="meta">{{ site.data.network | size }} nodes in {{ countries | size }} countries, across {{ regions | size }} regions.</p>
  </header>

  {% include network.html %}

  <div class="network-list">
    {% for r in regions %}
    <section>
      <h2>{{ r.name }}</h2>
      <ul>{% for n in r.items %}<li>{{ n.city }} <span>{{ n.country }}</span></li>{% endfor %}</ul>
    </section>
    {% endfor %}
  </div>
</div>
