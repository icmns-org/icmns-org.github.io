---
title: Past editions
permalink: /editions/
---
# Editions

{% assign editions = site.editions | sort: "year" | reverse %}
| Year | Dates | Location |
|---|---|---|
{% for e in editions %}| [{{ e.year }}]({{ e.url | relative_url }}) | {{ e.dates }} | {{ e.location }} |
{% endfor %}
