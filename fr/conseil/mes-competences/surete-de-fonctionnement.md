---
lang-ref: yang-expertise-dependability
layout: home
title: >-
    Sûreté de Fonctionnement
description: >-
    Prévoir ou améliorer le comportement de votre outil de production et de vos équipements, en termes de fiabilité, Maintenabilité, disponibilité et sécurité dans une vision de performance technico-économique.
    Levier de rentabilité, 5% de disponibilité induit 25% d’EBE supplémentaire.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: Sûreté de Fonctionnement
    subtitle: >-
        Maîtriser le comportement prévisionnel ou opérationnel
    description: >-
        D’équipements et d’installations, selon les axes FMDS et LCC
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
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

{% include contact.html show_name=true show_email=false show_phone=true show_street_address=true class="inverted" %}
