---
lang-ref: yang-expertise-risk-management
layout: home
title: >-
    Gestion des Risques
description: >-
    Identifier, évaluer, réduire et gérer les risques matériels et immatériels par une approche de type défense en profondeur et une vision duale unique stratégie / risques, c’est la sérénité d’exploitation retrouvée.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: Gestion des Risques
    subtitle: >-
        Prévoir, maîtriser et gérer les risques<br>
        d’une organisation, d’une activité ou d’un projet<br>
        et définir un plan de continuité d’activité PCA
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
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

{% include contact.html show_name=true show_email=false show_phone=true show_street_address=true class="inverted" %}
