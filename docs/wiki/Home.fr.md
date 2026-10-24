# Nexus Office 6.45.20 · révision 6

## [▶ Ouvrir Nexus Office](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/Nexus_Office_v6_45_20_Browser.html)

Ce lien ouvre directement l'application. L'édition pour navigateur ne nécessite ni installation ni Python. Utilisez un navigateur Chromium de bureau récent, lisez l'avis de l'application et décidez de continuer ou non. Le temps de chargement dépend de votre appareil et de votre connexion.

[English](https://github.com/RDunbar01/Nexus-Office/wiki/Home) · [日本語](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ja) · [한국어](https://github.com/RDunbar01/Nexus-Office/wiki/Home.ko) · [Fichiers de la version](https://github.com/RDunbar01/Nexus-Office/tree/main/releases/6.45.20)

## Documents, feuilles et signatures

La révision 6 ajoute des onglets en bas de Writer et Paint. Utilisez **+** pour en ajouter un ; double-cliquez sur un onglet ou appuyez sur F2 pour le renommer. Chaque onglet conserve son contenu et son historique d'annulation pendant la session. Dans Paint, Clear et l'export d'image ne concernent que la feuille active. Writer enregistre tous les onglets dans un `.nxwriter`, et Paint toutes les feuilles dans un `.nxpaint`. Les projets collectifs acceptent jusqu'à 25 onglets et 120 MiB ; l'historique d'annulation n'est pas enregistré. Leur ouverture remplace la collection de l'application après confirmation. Les onglets Sheets se renomment aussi directement, avec mise à jour des références par le mécanisme existant.

L'import PDF reconstruit du texte modifiable et conserve la mise en page originale dans Compatibility view. Cette vue ne reflète pas les modifications ultérieures dans Nexus. Les fichiers originaux restent téléchargeables. L'import et l'aperçu PDF sont limités à 300 pages ; aucune reconnaissance de caractères n'est incluse pour les PDF numérisés. Les originaux contenant des macros sont conservés, mais VBA, ActiveX et le code embarqué ne s'exécutent pas.

Writer peut insérer une signature dessinée, importée ou enregistrée avec la date locale courante. **Une image de signature n'est pas une signature cryptographique. La conversion des anciens formats, le téléchargement direct d'un PDF paginé et la signature PKI nécessitent l'assistant local facultatif, pas seulement la page hébergée.** Cet assistant nécessite Python 3.10+ et LibreOffice ; la signature par certificat demande une configuration supplémentaire propre au paquet. Consultez le [guide des documents et signatures](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/OFFICE_DOCUMENTS.md).

## Thèmes et espaces de travail conservés

Les dix thèmes restent disponibles dans **Settings → Office themes**. Porcelain est le choix par défaut sans préférence enregistrée. Les thèmes modifient l'interface, pas le contenu créé. La préférence est enregistrée pour ce navigateur et cette origine ; si le stockage est bloqué, elle reste valable pour la session. Gardez les illustrations à côté du HTML. [Guide des thèmes Office](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/OFFICE_THEMES.md).

- **Dashboard Studio → Aviation example → Use template** : 14 tables modifiables, 101 enregistrements fictifs, six pages, 15 mesures et 23 visualisations. Fleet overview et Safety & risks contiennent une matrice de risques dynamique de 5 × 5. Modifier Impact ou Likelihood déplace le risque ; sélectionner une cellule filtre la page. [Ouvrir l'exemple modifiable indépendant](https://rdunbar01.github.io/Nexus-Office/releases/6.45.20/examples/NEXUS_General_Aviation_Dashboard.html).
- **Paint → Design Studio** : 629 modèles, 2 720 éléments et 19 polices conservés depuis la révision 2. **Photos → Before & after collections** propose 100 paires d'images générées, réparties en deux collections de 100 mises en page modifiables. Les photos et les textes restent sur des calques distincts. Les images illustrent des styles de sourcils, pas des résultats réels de traitement.

Le guide Word inclus décrit toujours les fonctions de la révision 3 ; OFFICE_DOCUMENTS.md décrit la révision 6. [Consulter les changements](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/docs/CHANGELOG_6.45.20.md).

## Utilisation hors ligne et installation

Le fichier HTML du navigateur fait 19 976 619 octets, mais **il ne contient pas à lui seul le moteur PDF, les illustrations des thèmes et toute la collection de photos**. Conservez `document_assets`, `theme_assets` et `comparison_assets` à côté du HTML. Le dossier `document_assets` complet fournit le moteur PDF, son manifeste et sa licence tierce pour l’import et l’aperçu locaux. Les 12 PNG de `theme_assets` fournissent les illustrations des thèmes ; s’ils manquent, les aperçus vectoriels intégrés prennent le relais sans désactiver les thèmes ni les commandes de lancement. Conservez les fichiers `comparison_assets/photos-01.js` à `photos-10.js` dans le dossier `comparison_assets`, à côté du HTML. Ces dix fichiers fournissent les 100 paires générées. S'ils manquent, utilisez **Load comparison photos** pour importer les packs `.nxcomparisons` correspondants. Les projets `.nxpaint` enregistrés intègrent les photos qu'ils utilisent.

Pour tout télécharger, choisissez **Code → Download ZIP** dans le dépôt, extrayez l'archive puis ouvrez `releases/6.45.20/Nexus_Office_v6_45_20_Browser.html`. Conservez l'arborescence. Aucun serveur local n'est nécessaire. Le navigateur doit prendre en charge DecompressionStream, TextEncoder/TextDecoder et Web Crypto. Les données décompressées et la mémoire utilisée dépassent la taille du HTML téléchargé.

La version complète contient 482 fichiers, soit 500 273 126 octets après extraction. Chaque fichier distribué fait moins de 20 000 000 d'octets. Les grandes archives ZIP d'origine ne sont pas ajoutées au dépôt ; leurs composants extraits y figurent. Pour l'installation facultative des sources, regroupez l'installateur, le manifeste et **les 23 parties `.nxd`**. Chaque partie fait au maximum 10 000 000 d'octets. Suivez [INSTALL.txt](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/INSTALL.txt) avec CPython 3.12 standard. Conservez ensemble `candidate.html`, `source_scripts`, `document_assets`, `theme_assets` et `comparison_assets` après extraction.

Sauvegardez vos documents et projets avant de changer de version. Cette version ne réécrit pas les projets enregistrés. Les [versions antérieures](https://github.com/RDunbar01/Nexus-Office/tree/main/releases) restent disponibles.

## Validation et limites

Les [résultats fournis pour la révision 6](https://github.com/RDunbar01/Nexus-Office/blob/main/releases/6.45.20/RELEASE_VALIDATION.json) indiquent 25 contrôles des documents dans le navigateur, 14 des thèmes, 21 de Design Studio et 9 des risques, plus 6 contrôles du service, 6 des sources et 5 cas du chargeur, sous Chromium sur Linux. Ils comprennent des conversions réelles avec LibreOffice et un certificat de test autosigné. Les fichiers de test Pages avec aperçu intégré et les macros sont synthétiques ; ils ne prouvent pas la compatibilité avec tous les fichiers réels. Les anciens résultats restent des éléments historiques, pas de nouveaux tests de la révision 6.

La [vérification distincte du paquet](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/PUBLICATION_VERIFICATION_6.45.20.json) contrôle les octets, empreintes, inventaires, données reconstruites et chemins des fichiers associés sans exécuter l'application fournie ni ses tests fonctionnels. Ce n'est pas une qualification multiplateforme. Le matériel Windows et macOS n’a pas été testé ; ces résultats ne qualifient ni les performances Radeon ni les écrans 4K physiques. La vitesse de démarrage et la fidélité des formats de documents ne sont pas garanties. [Empreintes exactes et détails du navigateur](https://github.com/RDunbar01/Nexus-Office/blob/main/docs/BROWSER_TRIAL.md).

## Autorisations

L'utilisation personnelle ainsi que les tests et évaluations commerciaux internes sont autorisés pour les éléments appartenant à Nexus. La redistribution, la modification, le déploiement en production et les autres usages commerciaux exigent un consentement écrit exprès. Les licences tierces et les droits accordés antérieurement restent inchangés. Consultez la [licence](https://github.com/RDunbar01/Nexus-Office/blob/main/LICENSE), l'[autorisation d'évaluation](https://github.com/RDunbar01/Nexus-Office/blob/main/COMMERCIAL_EVALUATION_PERMISSION.md) et les avis inclus.
