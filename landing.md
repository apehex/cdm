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
        .upper-half svg {
            fill: rgba(10,100,130,0.4);
        }
        .lower-half svg {
            fill: rgba(130,0,130,0.4);
        }
        svg .test:hover {
            fill: rgba(255,0, 0, 0.6);
        }
    </style>
    <!-- Wrapper -->
    <div id="wrapper">
        <div class="links" style="z-index: 100; position: fixed; top:0; left: 0; width: 100vw; height: 100vh; display: flex; flex-direction: column;">
            <a href="{{ '/en/yang' | absolute_path }}" style="position: absolute; top:-70vh; left: -70vw; width: 140vw; height: 140vh; border-radius: 50%; background: rgba(255,0,0,0.0);"></a>
            <a href="{{ '/en/yin' | absolute_path }}" style="position: absolute; bottom:-70vh; right: -70vw; width: 140vw; height: 140vh; border-radius: 50%; background: rgba(0,255,0,0.0);"></a>
        </div>
        <div class="background" style="position: fixed; z-index: 0; top:0; left: 0; width: 100vw; height: 100vh; display: flex; flex-direction: column;">
            {% include landing.svg %}
        </div>
    </div>
    {% include footer.html %}
</body>
</html>
