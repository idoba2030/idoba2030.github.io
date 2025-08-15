---
layout: single
title: "Talks and Teaching"
permalink: /talks-teaching/
author_profile: true
---

## Selected talks
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

<!-- Manually added selected talks -->
  <li>Reduced Outcome-Irrelevant Learning in Autistic Spectrum Disorder — Israeli Computational Psychiatry Conference 2025, Tel Aviv, Israel (15-minute talk)</li>
  <li>Automatic and implicit outcome-irrelevant model-free learning in human behavior — Tel-Aviv School of Psychology Conference (15-minute talk)</li>
  <li>Computational reinforcement learning processes underlying the onset and maintenance of ritualistic behavior — Israeli Biological Psychiatry Conference, Jerusalem, Israel</li>
  <li>Automatic and implicit outcome-irrelevant model-free learning in human behavior — Israeli Cognitive Psychology Conference 2025, Akko, Israel (15-minute talk)</li>
  <li>Cognitive Mechanisms Underlying Outcome-Irrelevant Learning in Human Choice Behavior — Dynamic Cognition Lab, Tubingen, Germany (90-minute talk)</li>
  <li>Cognitive Mechanisms Underlying Outcome-Irrelevant Learning in Human Choice Behavior — Max Planck Institute for Biological Cybernetics, Tubingen, Germany (90-minute talk)</li>
  <li>Cognitive Mechanisms Underlying Outcome-Irrelevant Learning in Human Choice Behavior — European Mathematical Psychology Conference, Tubingen, Germany (15-minute talk)</li>
  <li>Computational mechanisms underlying latent inverse value updating of unchosen actions — 57th Annual Meeting of the Society for Mathematical Psychology (15-minute talk)</li>
  <li>Value-based mechanisms underlying compulsive rituals — Israeli Society for Computational Psychiatry (45-minute talk)</li>
  <li>Cognitive Overfitting — A Novel Theoretical Mechanism for Compulsive Rituals — International OCD Foundation Conference, San Francisco, USA (15-minute talk)</li>
  <li>Computational mechanisms underlying latent inverse value updating of unchosen actions — Israeli Society for Cognitive Psychology 2023, Akko, Israel (15-minute talk)</li>
  <li>Computational mechanisms underlying latent inverse value updating of unchosen actions — Sagol School of Neuroscience Retreat 2023, Nazareth, Israel (3-minute talk)</li>
  <li>Computational mechanisms underlying latent inverse value updating of unchosen actions — Neuromatch Computational Neuroscience Conference 2022 (5-minute talk)</li>
  <li>Cognitive resources predict value learning for outcome-irrelevant features — Neuromatch Computational Neuroscience Conference 2021 (5-minute talk)</li>
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
  </li>
  <li>
    <strong>Teaching Assistant, <a href="https://compneuro.neuromatch.io/tutorials/intro.html" target="_blank">Neuromatch Academy</a></strong> — 3-week course on Computational Neuroscience; mentored student projects  
  </li>
  <li>
    <strong>Teacher – XTRA student (Tel Aviv University)</strong> — Physiological Psychology B; curriculum development  
  </li>
</ul>

