---
lang-ref: yang-expertise-contracting-authority
layout: home
title: >-
    Contracting Authority
description: >-
    Organiser, Planifier les projets et Maîtriser les objectifs BQCDS d’un projet.
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
    title: Contracting Authority
    subtitle: >-
        Organiser, Planifier les projets et Maîtriser les objectifs BQCDS d’un projet
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

{%- assign data = site.data.expertise.yang.contracting-authority["fr"] -%}
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
