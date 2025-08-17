---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---


<div style="text-align:center; margin-top: 2em;">
  <embed src="/files/cv.pdf" type="application/pdf" width="80%" height="700px" style="border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); border: 1px solid #ddd;" />
  <div style="margin-top: 1.5em;">
    <a href="/files/cv.pdf" download style="display:inline-block; padding: 1em 2em; background: #6c63ff; color: #fff; border-radius: 8px; font-size: 1.2em; text-decoration: none; box-shadow: 0 2px 8px rgba(0,0,0,0.08);">
      Download CV (PDF)
    </a>
  </div>
</div>
  * Sub-skill 2.3
* Skill 3

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
