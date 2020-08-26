---
layout: null
---
{%- assign lang = page.lang | default: site.lang | default: 'en' -%}
{%- assign title = page.title | default: site.title -%}
{%- assign description = page.description | default: site.description -%}
<!DOCTYPE html>
<!--
    Consulting template by MOODULE
    https://github.com/moodule/jekyll-theme-consulting
    Free for personal and commercial use under the CCA 4.0 license
-->
<html lang="{{ lang }}">
{% include head.html title=title subtitle=subtitle %}
<body>
    <style type="text/css">
        svg .test:hover {
            fill: rgba(255,0, 0, 0.6);
        }
        .background {
            z-index: 0;
            position: absolute;
            top:0;
            left: 0;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .links {
            z-index: 100;
            position: absolute;
            top:0;
            left: 0;
            width: 100vw;
            height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        .links a {
            position: absolute;
            width: 140vw;
            height: 140vh;
            border-radius: 50%;
            background: rgba(0,0,0,0.0);
            border: none !important;
        }
        a.upper-left {
            top:-70vh;
            left: -70vw;
        }
        a.lower-right {
            bottom:-70vh;
            right: -70vw;
        }
        .showcase {
            position: absolute;
            top: 100vh;
            left: 0;
            display: flex;
            flex-direction: column;
        }
        .showcase > div {
            width: 23vw;
            height: 31vh;
            border: none;
            margin:auto;
        }
    </style>
    <div class="links">
        <a class="upper-left" href="{{ '/en/yang' | absolute_path }}"></a>
        <a class="lower-right" href="{{ '/en/yin' | absolute_path }}"></a>
    </div>
    <div class="background" style="">
        {% include landing.svg %}
    </div>
    <div class="showcase">
        <div>{% include landing.svg %}</div>
        <div>{% include landing.svg %}</div>
        <div>{% include landing.svg %}</div>
    </div>
    {% include footer.html %}
</body>
</html>
