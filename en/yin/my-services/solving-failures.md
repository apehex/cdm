---
lang-ref: yin-services-solving-failures
layout: home
title: >-
    Solving Failures
description: >-
    Traiter les causes plutôt que les effets et déployer une stratégie de défense en profondeur.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Supporting Companies from Decision to Operations
banner:
    title: >-
        Solving Failures
    subtitle: >-
        Traiter les causes plutôt que les effets et déployer une stratégie de défense en profondeur
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
---

{%- assign data = site.data.services.yin.solving-failures["fr"] -%}
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
