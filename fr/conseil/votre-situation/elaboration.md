---
lang-ref: yang-situation-development
layout: home
title: >-
    &Eacute;laboration
description: >-
    &Ecirc;tre aidé dans l’évaluation et l’organisation du projet.
background:
    class: inverted
    image:
        url: /assets/images/content/yang/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: >-
        &Eacute;laboration
    subtitle: >-
        &Ecirc;tre aidé dans l’évaluation et l’organisation du projet
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
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
