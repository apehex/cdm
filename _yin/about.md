---
layout: page
title: About CDM
---
# Profile

Ingénieur Conseil à la tête du Cabinet éponyme CDM, je suis spécialisé en Gestion des Risques et Efficience Industrielle.

Par ailleurs je suis Expert Indépendant.

40 ans d’expérience professionnelle, 11 ans dans la Marine, 20 ans dans l’industrie et les services, 9 ans dans le Conseil.

Mon parcours s'est structuré autour des activités de maintenance.
=> expertise
=> gestion de projet
=> direction technique

assurer service continu (maintenance)
=> analyser les dysfonctionnements: expertise
=> adapter, améliorer la technique: direction technique
=> pallier les déficiences organisationnelles: gestion de projet
=> anticiper, planfier: stratégie

# Achievements

{% for achievement in site.achievements %}
<li>
    <h2>{{ achievement.title }}</h2>
    <h2>{{ achievement.category }}</h2>
    <p>{{ achievement.content | markdownify }}</p>
</li>
{% endfor %}

# They trust us

![AED][aed-logo]
![Areva][areva-logo]
![Benning][benning-logo]
![MMP][mmp-logo]
![Sealed Air][sealed-air-logo]

# Certifications

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