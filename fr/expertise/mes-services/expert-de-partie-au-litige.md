---
lang-ref: yin-services-support-during-litigation
layout: home
title: >-
    &Eacute;valuer les Dégâts
description: >-
    Sauvegarder les intérêts en demande ou en défense et fonder ou combattre la réclamation.
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
        &Eacute;valuer les Dégâts
    subtitle: >-
        Sauvegarder les intérêts en demande ou en défense et fonder ou combattre la réclamation
    description: " "
    button:
        url: >-
            #contact
        label: >-
            Demandez Conseil
---

{%- assign data = site.data.services.yin.support-during-litigation["fr"] -%}
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
