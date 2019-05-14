---
layout: page
title: CDM
subtitle: Outgrowing incidents and litigation
permalink: /yin/blog
---
{%- if site.posts.size > 0 -%}
<section>
    <header class="major">
        <h2>Blog</h2>
    </header>
    <div class="posts">
    {%- for post in site.posts -%}
    <article>
        {% if post.image %}
        <a href="{{ post.url | absolute_url }}" class="image"><img src="{{ post.image | absolute_url }}" alt="" /></a>
        {% endif %}
        <h3>{{ post.title }}</h3>
        <p>{{ post.summary }}</p>
        <ul class="actions">
            <li><a href="{{ post.url | absolute_url }}" class="button">More</a></li>
        </ul>
    </article>
    {%- endfor -%}
    </div>
    <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | absolute_url }}">via RSS</a></p>
</section>
{%- endif -%}