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
</ul>
