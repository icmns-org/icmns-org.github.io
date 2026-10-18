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
    <p class="meta">{{ site.data.people | size }} people at {{ site.data.network | size }} nodes in {{ countries | size }} countries, across {{ regions | size }} regions.</p>
  </header>

  {% include network.html %}

  {%- assign people = site.data.people | default: empty %}
  <div class="network-list">
    {%- for r in regions %}
    <section>
      <h2>{{ r.name }}</h2>
      {%- assign by_country = r.items | group_by: "country" %}
      {%- for c in by_country %}
      <h3>{{ c.name }}</h3>
      <ul>
        {%- for n in c.items %}
        <li>{{ n.city }}
          {%- assign here = people | where: "city", n.city -%}
          {%- if here.size > 0 %}<ul class="people">{% for p in here %}<li>{{ p.name }} <span>{{ p.institution }}</span></li>{% endfor %}</ul>{% endif %}
        </li>
        {%- endfor %}
      </ul>
      {%- endfor %}
    </section>
    {%- endfor %}
  </div>
</div>
