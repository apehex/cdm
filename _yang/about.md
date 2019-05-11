---
layout: page
title: CDM
subtitle: Supporting companies from decision to operations
permalink: /yang/about
---
<section>
    <header class="major">
        <h2>About me</h2>
    </header>
    <span class="image right"><img src="{{ 'assets/images/portrait.jpg' | relative_url }}" alt="" /></span>
    <p>Ingénieur conseil à la tête du cabinet éponyme CDM, je suis spécialisé en Gestion des Risques et Efficience Industrielle.</p>
    <p>Mon parcours s'est articulé autour des activités de maintenance ; pour amener les industries au plus près du service continu, j'ai progressivement intégré les facettes
    => analyser les dysfonctionnements: expertise
    => adapter, améliorer la technique: direction technique
    => pallier les déficiences organisationnelles: gestion de projet
    => anticiper, planfier: stratégie
    40 ans d’expérience professionnelle, 11 ans dans la Marine, 20 ans dans l’industrie et les services, 9 ans dans le Conseil.</p>
    <p>Par ailleurs je suis Expert Indépendant.</p>
</section>

<section>
    <header class="major">
        <h2>Achievements</h2>
    </header>
    {% for achievement in site.achievements %}
    <li>
        <h2>{{ achievement.title }}</h2>
        <h2>{{ achievement.category }}</h2>
        <p>{{ achievement.content | markdownify }}</p>
    </li>
    {% endfor %}
</section>

<section>
    <header class="major">
        <h2>They trust me</h2>
    </header>
    <div class="box alt">
        <div class="row gtr-50 gtr-uniform">
            <div class="col-4"><span class="image fit">![AED][aed-logo]</span></div>
            <div class="col-4"><span class="image fit">![Areva][areva-logo]</span></div>
            <div class="col-4"><span class="image fit">![Benning][benning-logo]</span></div>
            <!-- Break -->
            <div class="col-4"><span class="image fit">![MMP][mmp-logo]</span></div>
            <div class="col-4"><span class="image fit">![Sealed Air][sealed-air-logo]</span></div>
            <div class="col-4"><span class="image fit"><img src="images/pic02.jpg" alt="" /></span></div>
            <!-- Break -->
            <div class="col-4"><span class="image fit"><img src="images/pic02.jpg" alt="" /></span></div>
            <div class="col-4"><span class="image fit"><img src="images/pic03.jpg" alt="" /></span></div>
            <div class="col-4"><span class="image fit"><img src="images/pic01.jpg" alt="" /></span></div>
        </div>
    </div>
</section>

<section>
    <header class="major">
        <h2>Certifications</h2>
    </header>
    <div class="features">
        <article>
            <span class="icon"><img src="{{ '/assets/images/ensem.png' | absolute_url }}" alt="" /></span>
            <div class="content">
                <h3>ENSEM</h3>
                <p>Diplôme d'ingénieur</p>
            </div>
        </article>
        <article>
            <span class="icon fa-paper-plane"></span>
            <div class="content">
                <h3>Sapien veroeros</h3>
                <p>Aenean ornare velit lacus, ac varius enim lorem ullamcorper dolore. Proin aliquam facilisis ante interdum. Sed nulla amet lorem feugiat tempus aliquam.</p>
            </div>
        </article>
        <article>
            <span class="icon fa-rocket"></span>
            <div class="content">
                <h3>Quam lorem ipsum</h3>
                <p>Aenean ornare velit lacus, ac varius enim lorem ullamcorper dolore. Proin aliquam facilisis ante interdum. Sed nulla amet lorem feugiat tempus aliquam.</p>
            </div>
        </article>
        <article>
            <span class="icon fa-signal"></span>
            <div class="content">
                <h3>Sed magna finibus</h3>
                <p>Aenean ornare velit lacus, ac varius enim lorem ullamcorper dolore. Proin aliquam facilisis ante interdum. Sed nulla amet lorem feugiat tempus aliquam.</p>
            </div>
        </article>
    </div>
</section>

![ENSEM][ensem-logo] Diplôme d'Ingénieur

![EISTI][eisti-logo] Mastère Spécialisé en Gestion des Risques sur les territoires.

![IEAM][ieam-logo] MBA en Gestion et Management Stratégique d’Entreprise.

![IFG][ifg-logo] 

![UB][ub-logo] capacité en Droit.

![CIE][cie-logo]

![CNEFIC][cnefic-logo] Experts certifié dans le Génie frigorifique, le Génie climatique, le domaine des pompes à chaleur, les transports frigorifiques et l’isolation.

[aed-logo]: /assets/images/aed.png
[areva-logo]: /assets/images/areva.png
[benning-logo]: /assets/images/benning.png
[mmp-logo]: /assets/images/mmp.png
[sealed-air-logo]: /assets/images/sealed-air.png

[cie-logo]: /assets/images/cie.png
[cnefic-logo]: /assets/images/cnefic.png
[eisti-logo]: /assets/images/eisti.png
[ensem-logo]: /assets/images/ensem.png
[ieam-logo]: /assets/images/ieam.png
[ifg-logo]: /assets/images/ifg.png
[ub-logo]: /assets/images/ub.png