---
lang-ref: yang-services-project-support
layout: home
title: >-
    Assistance à Projet
description: >-
    Définir et formaliser vos besoins, vos objectifs stratégiques et opérationnels, vos exigences par Cahier des Charges, tout en intégrant l’évolutivité future de votre projet vous apporte la maîtrise des axes BQCDS de ceux-ci.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: Assistance à Projet
    subtitle: >-
        Les questions qui se posent et auxquelles je pourrais répondre
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.services.yang.project-support["fr"] -%}
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
