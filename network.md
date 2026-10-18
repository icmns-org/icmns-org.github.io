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
    <section>
      <h2>{{ r.name }}</h2>
      {%- assign countries_here = r.items | sort: "country" %}
      {%- for n in countries_here %}
      <h3>{{ n.country }}</h3>
      {%- assign here = people | where: "country", n.country %}
      <ul class="people">{% for p in here %}<li>{{ p.name }} <span>{{ p.institution }}</span></li>{% endfor %}</ul>
      {%- endfor %}
    </section>
    {%- endfor %}
  </div>
</div>
</div>
