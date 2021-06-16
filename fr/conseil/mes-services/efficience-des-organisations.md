---
lang-ref: yang-services-operations-efficiency
layout: home
title: >-
    Efficience des Organisations
description: >-
    Améliorer la performance court, moyen et long terme de votre organisation selon les axes humains, organisationnels et techniques, par une approche de management des processus (type BPM), et formaliser le tout par un tableau de bord (type BSC) vous guidera sur le chemin de la performance.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: Efficience
    subtitle: >-
        Les questions qui se posent et auxquelles je pourrais répondre
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.services.yang.operations-efficiency["fr"] -%}
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
