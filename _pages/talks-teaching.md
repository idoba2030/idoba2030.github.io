---
layout: single
title: "Talks and Teaching"
permalink: /talks-teaching/
author_profile: true
---

## Talks
<ul>
{% for talk in site.talks %}
  <li>
    <strong>{{ talk.title }}</strong>
    {% if talk.venue %} — {{ talk.venue }}{% endif %}
    {% if talk.date %} ({{ talk.date | date: "%B %d, %Y" }}){% endif %}
    {% if talk.link %} — <a href="{{ talk.link }}" target="_blank">View</a>{% endif %}
  </li>
{% endfor %}
</ul>

## Teaching
<ul>
{% for teaching in site.teaching %}
  <li>
    <strong>{{ teaching.title }}</strong>
    {% if teaching.venue %} — {{ teaching.venue }}{% endif %}
    {% if teaching.date %} ({{ teaching.date | date: "%B %d, %Y" }}){% endif %}
    {% if teaching.link %} — <a href="{{ teaching.link }}" target="_blank">View</a>{% endif %}
  </li>
{% endfor %}

  <!-- Manually added entries -->
  <li>
    <strong>Teaching Assistant</strong> — Statistics and Research Methods; Basics of Programming in R (Psychology and Neuroscience graduate students)  
    <em>2022 – Present</em>
  </li>
  <li>
    <strong>Teaching Assistant, Neuromatch Academy</strong> — 3-week course on Computational Neuroscience; mentored student projects  
    <em>2022</em>
  </li>
  <li>
    <strong>Teacher – XTRA student (Tel Aviv University)</strong> — Physiological Psychology B; curriculum development  
    <em>2020</em>
  </li>
</ul>
