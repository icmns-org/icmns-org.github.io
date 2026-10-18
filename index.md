---
title: Home
---
{% assign current = site.editions | where: "year", site.current_edition | first %}
<div class="wrap">
  <section class="landing">
    <div class="landing-mark">
      <img class="logo-light" src="{{ '/assets/logo/icmns_mark-light.svg' | relative_url }}?v={{ site.time | date: '%s' }}" alt="The ICMNS logo: a brain whose folds are a Turing pattern, drawn as fibres" width="880" height="880">
      <img class="logo-dark" src="{{ '/assets/logo/icmns_mark-dark.svg' | relative_url }}?v={{ site.time | date: '%s' }}" alt="" width="880" height="880">
    </div>
    <div>
      <h1>International Conference on Mathematical Neuroscience</h1>
      <p class="landing-next">Next: ICMNS {{ site.current_edition }} &middot;
        {% if current and current.dates != "TBA" %}{{ current.dates }}{% if current.location != "TBA" %} &middot; {{ current.location }}{% endif %}{% else %}dates and venue to be announced{% endif %}</p>
      <div class="cta">
        {% if current %}{% assign site_link = current.links | first %}<a class="button button-primary" href="{% if site_link %}{{ site_link.url }}{% else %}{{ current.url | relative_url }}{% endif %}">ICMNS {{ site.current_edition }}</a>{% endif %}
        <a class="button" href="{{ '/news/' | relative_url }}">News</a>
        <a class="button" href="{{ site.mailing_list }}">Mailing list</a>
      </div>
    </div>
  </section>
</div>
