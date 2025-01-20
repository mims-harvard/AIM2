---
layout: page
title: Staff
description: Aritificial Inteligence in Medicine II course staff
nav_order: 16
---

# Staff

## Faculty Instructor

{% assign instructors = site.staffers | where: 'role', 'Faculty Instructor' %}
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}

## Curriculum Fellow

{% assign cur_fellows = site.staffers | where: 'role', 'Curriculum Fellow' %}
{% for staffer in cur_fellows %}
{{ staffer }}
{% endfor %}

## Teaching Assistants

{% assign staff = site.staffers | where: 'role', 'Staff' %}
<div class="role">
  {% for staffer in staff %}
  {{ staffer }}
  {% endfor %}
</div>