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

  {%- assign people = site.data.people | default: empty %}
  <div class="network-list">
    {% for r in regions %}
    <section>
      <h2>{{ r.name }}</h2>
      <ul>{% for n in r.items %}<li>{{ n.city }} <span>{{ n.country }}</span>
        {%- assign here = people | where: "city", n.city -%}
        {%- if here.size > 0 %}<ul class="people">{% for p in here %}<li>{{ p.name }} <span>{{ p.institution }}</span></li>{% endfor %}</ul>{% endif %}
      </li>{% endfor %}</ul>
    </section>
    {% endfor %}
  </div>

  {%- assign node_cities = site.data.network | map: "city" -%}
  {%- capture elsewhere -%}{% for p in people %}{% unless node_cities contains p.city %}<li>{{ p.name }} <span>{{ p.institution }}, {{ p.city }}</span></li>{% endunless %}{% endfor %}{%- endcapture -%}
  {%- if elsewhere != "" %}
  <div class="network-elsewhere">
    <h2>Not yet on the map</h2>
    <p class="meta">People whose city is not one of the nodes above.</p>
    <ul class="people">{{ elsewhere }}</ul>
  </div>
  {%- endif %}
</div>
