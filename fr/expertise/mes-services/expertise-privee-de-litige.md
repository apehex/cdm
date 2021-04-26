---
lang-ref: yin-services-private-expert-assessment
layout: home
title: >-
    Expertise privée de litige
description: >-
    Quantifier les performances des systèmes et formaliser les processus de création de valeur.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Dépasser les incidents
banner:
    title: >-
        Expertise Privée de Litige
    subtitle: >-
        Les questions qui se posent,<br>
        auxquelles je pourrais répondre
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.services.yin.private-expert-assessment["fr"] -%}
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
