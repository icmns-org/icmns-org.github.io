---
title: Past editions
permalink: /editions/
---
{% assign editions = site.editions | where_exp: "e", "e.year < site.current_edition" | sort: "year" | reverse %}
<div class="wrap">
  <header class="page-head">
    <h1>Past editions</h1>
    <p class="meta">ICMNS was launched in 2015 and has been held {{ editions | size }} times since.</p>
  </header>
  <section class="editions-list">
    <table class="data editions">
      <thead><tr><th>Year</th><th>Edition</th><th>Location</th><th>Dates</th><th><span class="visually-hidden">Open</span></th></tr></thead>
      <tbody>
        {% for e in editions %}
        <tr><td class="year"><a href="{{ e.url | relative_url }}">{{ e.year }}</a></td><td>{{ e.edition }}</td><td>{{ e.location }}</td><td>{{ e.dates }}</td><td class="go" aria-hidden="true">→</td></tr>
        {% endfor %}
      </tbody>
    </table>
  </section>
</div>
