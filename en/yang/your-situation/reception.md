---
lang-ref: yang-situation-reception
layout: home
title: >-
    Reception
description: >-
    Vérifier l’adaptation aux besoins et la conformité à votre commande.
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
        Reception
    subtitle: >-
        Vérifier l’adaptation aux besoins et la conformité à votre commande
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

{%- assign data = site.data.situation.yang.reception["fr"] -%}
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
