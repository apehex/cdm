---
layout: page
title: CDM
subtitle: Outgrowing incidents and litigation
permalink: /yin/about
---
<section>
    <header class="major">
        <h2>About me</h2>
    </header>
    <span class="image right"><img src="{{ 'assets/images/portrait.jpg' | relative_url }}" alt="" /></span>
    <p>Ingénieur conseil à la tête du cabinet éponyme CDM, je suis spécialisé en Gestion des Risques et Efficience Industrielle.</p>
    <p>Mon parcours s'est articulé autour des activités de maintenance ; pour amener les industries au plus près du service continu, j'ai progressivement intégré toutes les facettes de la production :
    <ul>
        <li>la <strong>direction technique</strong> à force d'adapter, intégrer les parcs machines</li>
        <li>la <strong>gestion de projet</strong> en alignant les équipes sur les objectifs</li>
        <li>la <strong>stratégie</strong> en anticipant, réglant la production</li>
        <li>l'<strong>expertise</strong> par l'analyse des dysfonctionnements, l'arbitrage des différents</li>
    </ul></p>
    <p>Fort de 40 ans d’expérience professionnelle, 11 ans dans la Marine, 20 ans dans l’industrie et les services, 9 ans dans le Conseil, j'ai maintenant développé une approche holistique.</p>
    <p>Par ailleurs je suis Expert Indépendant.</p>
</section>

<section>
    <header class="major">
        <h2>Achievements</h2>
    </header>
    {% for achievement in site.achievements %}
    <h2>{{ achievement.title }}</h2>
    <!-- <h2>{{ achievement.category }}</h2> -->
    <p>{{ achievement.content | markdownify }}</p>
    {% endfor %}
</section>

<section>
    <header class="major">
        <h2>They trust me</h2>
    </header>
    <div class="box alt">
        <div class="row gtr-50 gtr-uniform">
            <div class="col-4"><span class="image fit"><img src="{{ '/assets/images/aed.png' | absolute_url }}" alt="" /></span></div>
            <div class="col-4"><span class="image fit"><img src="{{ '/assets/images/areva.png' | absolute_url }}" alt="" /></span></div>
            <div class="col-4"><span class="image fit"><img src="{{ '/assets/images/benning.png' | absolute_url }}" alt="" /></span></div>
            <!-- Break -->
            <div class="col-4"><span class="image fit"><img src="{{ '/assets/images/mmp.png' | absolute_url }}" alt="" /></span></div>
            <div class="col-4"><span class="image fit"><img src="{{ '/assets/images/sealed-air.png' | absolute_url }}" alt="" /></span></div>
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
                <h3>EISTI</h3>
                <p>Mastère Spécialisé en Gestion des Risques sur les territoires</p>
            </div>
        </article>
        <article>
            <span class="icon fa-rocket"></span>
            <div class="content">
                <h3>IEAM</h3>
                <p>MBA en Gestion et Management Stratégique d’Entreprise</p>
            </div>
        </article>
        <article>
            <span class="icon fa-signal"></span>
            <div class="content">
                <h3>IFG</h3>
                <p>?</p>
            </div>
        </article>
        <article>
            <span class="icon fa-signal"></span>
            <div class="content">
                <h3>UB</h3>
                <p>Capacité en droit</p>
            </div>
        </article>
        <article>
            <span class="icon fa-signal"></span>
            <div class="content">
                <h3>CIE</h3>
                <p>?</p>
            </div>
        </article>
        <article>
            <span class="icon fa-signal"></span>
            <div class="content">
                <h3>CNEFIC</h3>
                <p>Experts certifié dans le Génie frigorifique, le Génie climatique, le domaine des pompes à chaleur, les transports frigorifiques et l’isolation</p>
            </div>
        </article>
    </div>
</section>