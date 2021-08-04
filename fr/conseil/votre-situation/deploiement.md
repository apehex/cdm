---
lang-ref: yang-situation-deployment
layout: home
title: >-
    Déploiement
description: >-
    Mettre en œuvre les décisions d’investissement requière l’utilisation des méthodes de management de projet pour en assurer le suivi, la maîtrise des modifications et la correction des éventuels écarts afin d’atteindre les objectifs du Cahier des Charges.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: >-
        Déploiement
    subtitle: >-
        &Ecirc;tre aidé dans la mise en œuvre des décisions
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.situation.yang.deployment["fr"] -%}
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
