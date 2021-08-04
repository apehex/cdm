---
lang-ref: yang-expertise-contracting-authority
layout: home
title: >-
    Maîtrise d'Ouvrage
description: >-
    Assistance à la maîtrise d’ouvrage pour le pilotage de projets d’équipement industriels depuis la conception jusqu’à la mise en service, incluant éventuellement la réalisation de bâtiments, infrastructures et réseaux.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: Maîtrise d'Ouvrage
    subtitle: >-
        Organiser, Planifier les projets et<br>
        Maîtriser les objectifs BQCDS d’un projet
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.expertise.yang.contracting-authority["fr"] -%}
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
