---
lang-ref: yin-situation-litigation
layout: home
title: >-
    Action en Justice
description: >-
    Obtenir réparation amiable ou judiciaire de votre dommage.
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
        Action en Justice
    subtitle: >-
        Obtenir réparation amiable<br>
        Ou judiciaire de votre dommage
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.situation.yin.litigation["fr"] -%}
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
