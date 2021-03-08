---
layout: home
lang-ref: landing-page
title: >-
    Independant Engineering and Expertise
description: >-
    A Holistic Take On Business
---
<style type="text/css">
    .vector {
        z-index: 0;
        position: absolute;
        top:0;
        left: 0;
        width: 100vw;
        height: 100vh;
        display: flex;
        flex-direction: column;
    }
    svg#yin-yang {
        width: 100%;
        height: 100%;
    }
    svg .background {
        fill: #123456;
        stroke: #ffffff;
        transition: 0.3s;
    }
    svg .title {
        fill: #ffffff;
        transition: 0.3s;
    }
    svg .subtitle {
        fill: #ffffff;
        opacity: 0.0;
        transition: 0.6s;
    }
    svg .yin-yang:hover .background {
        fill: #0044dd;
    }
    svg .yin-yang:hover .title {
        fill: #ffdd44;
    }
    svg .yin-yang:hover .subtitle {
        opacity: 1.0;
    }
</style>
<div class="vector" style="">
    {% include landing/flat.svg %}
</div>
