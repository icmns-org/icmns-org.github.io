---
title: Past editions
permalink: /editions/
---
# Past editions

ICMNS was launched in 2015 and has been held {{ site.editions | where_exp: "e", "e.year < site.current_edition" | size }} times since.

{% assign editions = site.editions | where_exp: "e", "e.year < site.current_edition" | sort: "year" | reverse %}
| Year | Edition | Dates | Location |
|---|---|---|---|
{% for e in editions %}| [{{ e.year }}]({{ e.url | relative_url }}) | {{ e.edition }} | {{ e.dates }} | {{ e.location }} |
{% endfor %}
