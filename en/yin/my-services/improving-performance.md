---
lang-ref: yin-services-improving-performance
layout: home
title: >-
    Improving Performance
description: >-
    Quantifier les performances des systèmes et formaliser les processus de création de valeur.
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
    title: Improving Performance
    subtitle: >-
        Quantifier les performances des systèmes et formaliser les processus de création de valeur
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
