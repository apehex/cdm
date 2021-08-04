---
lang-ref: yang-expertise-maintenance
layout: home
title: >-
    Maintenance
description: >-
    Maintenir, rétablir et développer vos performances technico-économique globale d’organisation, et résoudre les situations dysfonctionnelles lorsque vos ressources courantes internes et fournisseurs ont été épuisées sans succès.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Accompagner de la Décision à l'Exploitation
banner:
    title: Maintenance
    subtitle: >-
        Développer la fonction en tant que levier de rentabilité de l’entreprise
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.expertise.yang.maintenance["fr"] -%}
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
