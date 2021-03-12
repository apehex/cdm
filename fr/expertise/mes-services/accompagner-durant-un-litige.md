---
lang-ref: yin-services-supporting-during-litigation
layout: home
title: >-
    Accompagner durant un Litige
description: >-
    Argumenter factuellement votre réclamation ou votre absence / exonération de responsabilité.
background:
    class: inverted
    image:
        url: /assets/images/content/yin/station-ep.webp
header:
    title: CDM
    subtitle: >-
        Dépasser les incidents
banner:
    title: >-
        Accompagner durant un Litige
    subtitle: >-
        Argumenter factuellement votre réclamation ou votre absence / exonération de responsabilité
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.services.yin.supporting-during-litigation["fr"] -%}
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
