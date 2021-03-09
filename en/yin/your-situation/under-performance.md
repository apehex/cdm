---
lang-ref: yin-situation-under-performance
layout: home
title: >-
    Under Performance
description: >-
    Restaurer vos marges, productivité et rentabilité.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Supporting Companies from Decision to Operations
banner:
    title: >-
        Under Performance
    subtitle: >-
        Restaurer vos marges, productivité et rentabilité
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
---

{%- assign data = site.data.situation.yin.under-performance["fr"] -%}
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
