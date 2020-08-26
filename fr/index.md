---
layout: landing
lang-ref: landing-page
title: >-
    Ingénierie et Expertise Indépendantes
subtitle: >-
    Une Approche Holistique Des Affaires
description: >-
    Todo
---
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
</style>
<div class="links">
    <a class="upper-left" href="{{ '/en/yang' | absolute_path }}"></a>
    <a class="lower-right" href="{{ '/en/yin' | absolute_path }}"></a>
</div>
<div class="background" style="">
    {% include landing.svg %}
</div>
