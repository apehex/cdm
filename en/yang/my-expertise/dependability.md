---
lang-ref: yang-expertise-dependability
layout: home
title: >-
    Dependability
description: >-
    Maîtriser le comportement prévisionnel ou opérationnel d’équipements et d’installations, selon les axes FMDS et LCC.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Supporting Companies from Decision to Operations
banner:
    title: Dependability
    subtitle: >-
        Maîtriser le comportement prévisionnel ou opérationnel
    description: >-
        D’équipements et d’installations, selon les axes FMDS et LCC
    button:
        url: >-
            #contact
        label: >-
            Ask for Advice
---

{%- assign data = site.data.expertise.yang.dependability["fr"] -%}
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
