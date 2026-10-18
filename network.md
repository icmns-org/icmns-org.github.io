---
title: Network
permalink: /network/
robots: noindex
sitemap: false
---
{%- assign regions = site.data.network | group_by: "region" -%}
<div class="wrap">
  <header class="page-head">
    <h1>The ICMNS network</h1>
    <p class="meta">{{ site.data.people | size }} people in {{ site.data.network | size }} countries, across {{ regions | size }} regions.</p>
  </header>

  {% include network.html %}

  {%- assign people = site.data.people | default: empty | sort: "surname" %}
  <div class="network-list">
    {%- for r in regions %}
    <section class="network-region">
      <h2>{{ r.name }}</h2>
        {%- assign countries_here = r.items | sort: "country" %}
        {%- for n in countries_here %}
        {%- assign here = people | where: "country", n.country %}
        <div class="network-country">
          <h3>{{ n.country }}</h3>
          <ul>{% for p in here %}<li><span class="who">{{ p.name }}</span><span class="where">{{ p.institution }}</span></li>{% endfor %}</ul>
        </div>
        {%- endfor %}
    </section>
    {%- endfor %}
  </div>
</div>
</div>
