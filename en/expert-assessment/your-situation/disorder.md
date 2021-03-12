---
lang-ref: yin-situation-disorder
layout: home
title: >-
    Disorder
description: >-
    Identifier les causes et les imputabilités, prendre des mesures conservatoires, sauver la situation.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Outgrowing incidents
banner:
    title: >-
        Disorder
    subtitle: >-
        Identifier les causes et les imputabilités, prendre des mesures conservatoires, sauver la situation
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
---

{%- assign data = site.data.situation.yin.disorder["fr"] -%}
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
