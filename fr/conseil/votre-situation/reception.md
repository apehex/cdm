---
lang-ref: yang-situation-reception
layout: home
title: >-
    Réception
description: >-
     Réceptionner partiellement, valider les jalons et réceptionner définitivement les livrables doit faire l’objet de protocoles dans une démarche de conception en « V » permettant de vérifier le respect de toutes les exigences du Cahier des Charges de départ ou amendé.
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
        Réception
    subtitle: >-
        Vérifier l’adaptation aux besoins et la conformité à votre commande
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.situation.yang.reception["fr"] -%}
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
