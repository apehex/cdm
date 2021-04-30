---
lang-ref: yin-expertise-mediation
layout: home
title: >-
    Médiation et Conciliation
description: >-
    Résoudre par la voie amiable et conventionnelle un désaccord
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Dépasser les incidents
    style:
        class: inverted
banner:
    title: >-
        Médiation et Conciliation
    subtitle: >-
        Résoudre par la voie amiable et conventionnelle un désaccord
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.expertise.yin.mediation["fr"] -%}
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
