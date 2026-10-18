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
      <thead><tr><th>Year</th><th>Edition</th><th>Location</th><th>Dates</th></tr></thead>
      <tbody>
        {% for e in editions %}
        <tr data-href="{{ e.url | relative_url }}"><td class="year"><a href="{{ e.url | relative_url }}">{{ e.year }}</a></td><td>{{ e.edition }}</td><td>{{ e.location }}</td><td>{{ e.dates }}</td></tr>
        {% endfor %}
      </tbody>
    </table>
  </section>
</div>
<script>
  // Make each row of the table open its edition (the year is also a normal link)
  document.querySelectorAll('.editions tr[data-href]').forEach(function (row) {
    row.addEventListener('click', function (e) {
      if (e.target.closest('a') || (window.getSelection && String(window.getSelection()))) return;
      if (e.metaKey || e.ctrlKey || e.button === 1) window.open(row.dataset.href, '_blank');
      else location.href = row.dataset.href;
    });
  });
</script>
