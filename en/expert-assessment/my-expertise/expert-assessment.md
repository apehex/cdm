---
lang-ref: yin-expertise-expert-assessment
layout: home
title: >-
    Expert Assessment
description: >-
    ?
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Outgrowing incidents
banner:
    title: Expert Assessment
    subtitle: >-
        ?
    description: >-
        ?
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
---

{%- assign data = site.data.expertise.yin.expert-assessment["fr"] -%}
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
