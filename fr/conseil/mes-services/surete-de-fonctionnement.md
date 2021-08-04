---
lang-ref: yang-services-dependability
layout: home
title: >-
    Sûreté de Fonctionnement
description: >-
    Résoudre vos situations dysfonctionnelles lorsque vous avez épuisé vos ressources courantes sans succès, et maîtriser les risques de votre organisation ainsi que les axes FMDS de vos moyens, est ma valeur ajoutée à votre business intégrant optimisation de la politique de maintenance.
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
        Les questions qui se posent et auxquelles je pourrais répondre
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.services.yang.dependability["fr"] -%}
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
