---
lang-ref: yang-expertise-efficiency
layout: home
title: >-
    Efficience
description: >-
    Améliorer la performance court, moyen et long terme de votre organisation selon les axes humains, organisationnels et techniques, par une approche de management des processus BPM, et formaliser le tout par un tableau de bord de type BSC.
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
        Prévoir ou améliorer la performance d’une entreprise,<br>
        d’une activité, d’une fonction ou d’un projet.
    description: >-
        Typiquement, la démarche complète conduit à un<br>
        doublement d’activité à périmètre de ressources fixes constant.
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.expertise.yang.efficiency["fr"] -%}
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
