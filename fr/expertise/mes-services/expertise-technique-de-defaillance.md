---
lang-ref: yin-services-rectifying-failures
layout: home
title: >-
    Expertise technique de défaillance
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
        Expertise technique<br>
        de Défaillance
    subtitle: >-
        Les questions qui se posent,<br>
        auxquelles je pourrais répondre
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.services.yin.rectifying-failures["fr"] -%}
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
