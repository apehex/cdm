---
lang-ref: yang-services-3
layout: home
title: >-
    Service 3
description: >-
    ?
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: Service 3
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

{%- assign data = site.data.services.yang.service-3["fr"] -%}
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
