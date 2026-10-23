# Version actuelle 6.45.4

[Ouvrir l’essai navigateur](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_4_Browser.html) · [Paquet complet](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.4)

L’accueil présente six cartes : Writer, Grid, Dashboard Studio, NexusPoint, Paint et Compatibility. Les panneaux de l’assistant et des éléments récents sont masqués et leur ouverture automatique est désactivée ; les documents et l’historique sont conservés. Le ruban de la version 6.45.3 est conservé. Cette mise à jour décrit l’interface actuelle, sans annoncer de nouvelles capacités de modèle ou d’édition.

L’utilisation personnelle et les tests et évaluations commerciaux internes du contenu Nexus sont autorisés. La distribution, la modification, le déploiement en production et les autres usages commerciaux exigent un consentement écrit exprès. Les licences tierces et les droits déjà accordés restent inchangés. [Autorisation d’évaluation](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).

## Documentation des versions précédentes (conservée sans modification)

# Version corrective actuelle 6.45.2

[Essai navigateur](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_2_Browser.html) · [Paquet complet](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.2)

La version 6.45.2 corrige les règles de débordement du ruban Writer pour rendre effective la zone d’outils défilante et limitée en hauteur. Les champs numériques de la règle forment une bande horizontale compacte, défilante si nécessaire, afin de préserver l’espace du document. Tous les outils restent accessibles, mais ne sont pas nécessairement visibles en même temps. Les améliorations de l’assistant de la version 6.45.1 sont inchangées. La disposition publiée en 6.45.1 est remplacée par cette correction visuelle.

L’utilisation personnelle et les tests et évaluations commerciaux internes du contenu Nexus sont autorisés. La distribution, la modification, le déploiement en production et les autres usages commerciaux exigent un consentement écrit exprès. Les licences tierces et les droits déjà accordés restent inchangés. [Autorisation d’évaluation](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).

[6.45.2](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/CHANGELOG_6.45.2.md) · [LICENSE](https://github.com/RDunbar01/Nexus-Office/blob/main/LICENSE) · [COMMERCIAL_EVALUATION_PERMISSION](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md)

## Documentation précédente (disposition remplacée ; conservée sans modification)

# Version actuelle 6.45.1

[Essayer dans le navigateur](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_1_Browser.html) · [Composants de l’installateur complet](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.1) · [Notes de version](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/CHANGELOG_6.45.1.md)

L’application installée et la version navigateur intègrent le panneau de l’assistant, son en-tête et sa zone de saisie remaniés. Writer répartit les groupes du ruban sur la largeur disponible et adapte les commandes et la règle aux fenêtres étroites, y compris lorsque l’assistant est épinglé. Les commandes, formats, modèles et fonctions d’édition restent inchangés.

Les éditions navigateur et installée actuelles comportent les mêmes changements visuels. Le ZIP complet contient l’installateur et tous les fichiers de données ; conservez-les ensemble. Chaque fichier de données fait au plus 10 000 000 octets et chaque composant distribué moins de 20 000 000 octets. Cette mise à jour n’ajoute pas de modèles compatibles et ne constitue pas une qualification sur du matériel Windows/Radeon physique.

L’utilisation personnelle et les tests et évaluations commerciaux internes du contenu Nexus sont autorisés. La distribution, la modification, le déploiement en production et les autres usages commerciaux exigent un consentement écrit exprès. Les licences tierces et les droits déjà accordés restent inchangés. [Autorisation d’évaluation](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).

## Notes de la version précédente (conservées sans modification)

# Nexus Office

[Essayer dans le navigateur](https://rdunbar01.github.io/Nexus-Office/Nexus_Office_v6_45_0_Browser.html) · [Dépôt](https://github.com/RDunbar01/Nexus-Office)

Nexus Office 6.45.0 réunit Writer, Grid, Present, Paint et Dashboard. La version d'essai, révision d'emballage 1, conserve le code et les ressources de l'application dans un seul fichier HTML. Ce format facilite l'évaluation en ligne et l'utilisation locale après téléchargement.

## Fonctions et limites

Modifiez des documents et des classeurs, utilisez des modèles de présentation, des ressources graphiques et des tableaux de bord. Les commandes Office sont limitées à des actions définies, avec saisie littérale, aperçu et approbation avant modification. Les modifications Writer utilisent le mécanisme d'annulation existant. Le petit modèle inclus n'est ni qualifié ni activé comme agent Office généraliste.

L'importation et l'exportation dépendent du format. La fidélité parfaite à Microsoft Office n'est pas garantie. Le presse-papiers, l'impression et le rendu dépendent du navigateur. Les tableaux de bord importés sont des instantanés, pas des connexions actives.

## Démarrage

Utilisez un navigateur de bureau récent avec DecompressionStream, TextEncoder/TextDecoder et Web Crypto. Le fichier vérifie et décompresse ses ressources localement avant d'afficher l'avis de l'application. Aucun serveur, Python, PyTorch ou CDN n'est requis au démarrage. Le fichier distribué fait moins de 20 000 000 octets ; l'application décompressée et la mémoire nécessaire sont plus volumineuses. Le délai de démarrage varie selon l'appareil.

Le paquet complet 6.45.0 est conservé sans modification. CPython 3.12 est recommandé pour son installateur facultatif. Son ancien candidate.html nécessite deux scripts compagnons, contrairement au nouvel essai autonome.

## Validation et autorisation

Consultez les [détails de construction et de test](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/BROWSER_TRIAL.md). L'utilisation personnelle et les tests et évaluations commerciaux internes du contenu Nexus sont autorisés. La distribution, la modification, le déploiement en production et les autres usages commerciaux exigent un consentement écrit exprès. Les licences tierces et les droits déjà accordés restent inchangés. Voir l'[autorisation d'évaluation](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md).

[English](https://github.com/RDunbar01/Nexus-Office/wiki/Home) · [日本語](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ko)
