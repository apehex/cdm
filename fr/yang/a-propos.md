---
lang-ref: yang-about
---
<section>
    <header class="major">
        <h2>About me</h2>
    </header>
    <span class="image right"><img src="{{ 'assets/images/portrait.jpg' | absolute_url }}" alt="" /></span>
    <p><strong>Ingénieur Conseil</strong>, je suis spécialisé en <strong>Gestion des Risques</strong> et <strong>Efficience Industrielle</strong> ; par ailleurs je suis <strong>Expert Indépendant</strong>.
    <p>J’ai donc deux <strong>activités complémentaires</strong> : le Conseil et l’Expertise.
    <p>Le Conseil prend forme à travers <strong>trois types de missions orientées</strong> :<br />
        - l’Audit RAR (Ressources-Activités-Résultats)<br />
        - l’Assistance à projet<br />
        - la Sûreté de Fonctionnement, à destination des PME et des ETI.</p>
    <p>Une diversité, une complémentarité et une cohérence de compétences de bout en bout issues de 40 ans d’expérience dans six domaines technologiques différents associée à une formation progressive depuis l’Ecole des Mousses / Marine à Bac+6 (Ingénieur, MBA, Droit, Risk Management).</p>
</section>

<section id="achievements">
    <header class="major">
        <h2>Réalisations Clefs</h2>
    </header>
    {% for achievement in site.achievements %}
    <h2>{{ achievement.title }}</h2>
    <!-- <h2>{{ achievement.category }}</h2> -->
    <p>{{ achievement.content | markdownify }}</p>
    {% endfor %}
</section>

<section>
    <header class="major">
        <h2>Ils me font Confiance</h2>
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

<section id="certifications">
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