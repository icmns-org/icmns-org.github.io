---
title: Steering committee
permalink: /steering-committee/
---
{%- assign regions = site.data.network | group_by: "region" -%}
<div class="wrap">
  <header class="page-head">
    <h1>Steering committee</h1>
    <p class="meta">{{ site.data.people | size }} people in {{ site.data.network | size }} countries, across {{ regions | size }} regions.</p>
  </header>

  {% include network.html %}

  {% include committee.html %}
</div>
</div>
