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
