---
lang-ref: yin-services-improving-performance
layout: home
title: >-
    Improving Performance
description: >-
    Quantifier les performances des systèmes et formaliser les processus de création de valeur.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Supporting Companies from Decision to Operations
banner:
    title: Improving Performance
    subtitle: >-
        Quantifier les performances des systèmes et formaliser les processus de création de valeur
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
---

{%- assign data = site.data.services.yin.improving-performance["fr"] -%}
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
