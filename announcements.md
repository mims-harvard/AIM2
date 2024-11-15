---
layout: page
title: Announcements
nav_exclude: true
description: BMIF 203 - Aritificial Inteligence in Medicine II class 
  announcements
---

# Announcements

Announcements are stored in the `_announcements` directory and rendered according to the layout file, `_layouts/announcement.html`.

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}
