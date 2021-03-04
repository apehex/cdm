---
lang-ref: yang-expertise-risk-management
layout: home
title: >-
    Risk Management
description: >-
    Prévoir, maîtriser et gérer les risques d’une organisation, d’une activité ou d’un projet et définir un plan de continuité d’activité PCA.
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
    title: Risk Management
    subtitle: >-
        Prévoir, maîtriser et gérer les risques d’une organisation, d’une activité ou d’un projet et définir un plan de continuité d’activité PCA
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

{%- assign data = site.data.expertise.yang.risk-management["fr"] -%}
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
