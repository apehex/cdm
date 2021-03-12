---
lang-ref: yin-situation-equipment-failure
layout: home
title: >-
    Equipment Failure
description: >-
    Résoudre durablement des défaillances ponctuelles et critiques ou chroniques.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Outgrowing incidents
banner:
    title: >-
        Equipment Failure
    subtitle: >-
        Résoudre durablement des défaillances ponctuelles et critiques ou chroniques
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
---

{%- assign data = site.data.situation.yin.equipment-failure["fr"] -%}
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
