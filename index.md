---
layout: page
title: Home
nav_order: 1
description: Artificial Intelligence in Medicine II

---

# Artificial Intelligence in Medicine II 

{: .mb-2 }
Harvard - [BMIF 203](https://dbmi.hms.harvard.edu/education/courses/bmif-203) and [BMI 702](https://dbmi.hms.harvard.edu/education/courses/bmi-702), Spring 2025
{: .mb-0 .fs-6 .text-grey-dk-000 }

<div>
Advances in AI will have a broad and profound impact on science and medicine, offering new approaches to transform medical research and practice. This course provides a comprehensive overview of cutting-edge AI paradigms, including self-supervised learning, generative models, and multimodal techniques that integrate diverse data types. Beyond foundational methods, the course dives into a range of real-world applications in natural language processing, medical image analysis, relational and structure understanding, and longitudinal patient data.
</div>

#### Faculty Instructor

{% assign instructors = site.staffers | where: 'role', 'Faculty Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div>

#### Curriculum Fellow

{% assign instructors = site.staffers | where: 'role', 'Curriculum Fellow' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div>

<br>

{% for module in site.modules %}
{{ module }}
{% endfor %}