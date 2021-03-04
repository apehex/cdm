---
lang-ref: yin-services-finding-palliative-solutions
layout: home
title: >-
    Finding Palliative Solutions
description: >-
    Accompagner dans la négociation
header:
    title: CDM
    subtitle: >-
        Supporting Companies from Decision to Operations
    style:
        class: inverted
        image:
            url: /assets/images/content/yin/station-ep.webp
            position: right
            size: auto 100vh
banner:
    title: >-
        Finding Palliative Solutions
    subtitle: >-
        Accompagner dans la négociation
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
    style:
        class: inverted
        image:
            url: /assets/images/content/yin/station-ep.webp
            position: right
            size: auto 100vh
---

{%- assign data = site.data.services.yin.finding-palliative-solutions["fr"] -%}
{%- for tab in data.tabs -%}
{%- assign is-inverted = forloop.index | modulo: 2 -%}
<section id="{{ tab.id }}" {% if is-inverted == 0 %}class="inverted"{% endif %}>
    <header class="major">
        <h2>{{ tab.title }}</h2>
    </header>
    {{ tab.content }}
</section>
{%- endfor -%}

{% include about/clients.html %}

{% include contact.html class="inverted" %}
