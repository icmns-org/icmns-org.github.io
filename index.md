---
title: Home
---
{% assign current = site.editions | where: "year", site.current_edition | first %}

<section class="hero">
  <h1>ICMNS {{ site.current_edition }}</h1>
  {% if current %}<p class="meta">{{ current.dates }} &middot; {{ current.location }}</p>{% endif %}
</section>

{{ site.description }}

<!-- TODO: welcome text, key dates, invited speakers, registration links -->

## Key dates

| Milestone | Date |
|---|---|
| Abstract submission opens | TBA |
| Abstract deadline | TBA |
| Registration deadline | TBA |
| Conference | TBA |

{% if current %}[More about ICMNS {{ site.current_edition }} →]({{ current.url | relative_url }}){% endif %}
