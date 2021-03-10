---
lang-ref: yang-situation-development
layout: home
title: >-
    Development
description: >-
    &Ecirc;tre aidé dans l’évaluation et l’organisation du projet.
header:
    title: CDM
    subtitle: >-
        Supporting Companies from Decision to Operations
    style:
        class: inverted
        image:
            url: /assets/images/content/yang/station-ep.webp
            position: right
            size: auto 100vh
banner:
    title: >-
        Development
    subtitle: >-
        &Ecirc;tre aidé dans l’évaluation et l’organisation du projet
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
    style:
        class: inverted
        image:
            url: /assets/images/content/yang/station-ep.webp
            position: right
            size: auto 100vh
---

{%- assign data = site.data.situation.yang.development["fr"] -%}
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
