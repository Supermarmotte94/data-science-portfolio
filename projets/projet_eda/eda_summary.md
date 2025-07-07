## Résumé de l'Analyse Exploratoire des Données (AED) - Performance des Étudiants

Ce projet a exploré un ensemble de données sur la performance des étudiants aux examens, en se concentrant sur les scores en mathématiques, lecture et écriture, ainsi que sur des facteurs démographiques et socio-économiques.

### Aperçu du Dataset
Le dataset contient 1000 entrées et 8 colonnes, sans valeurs manquantes. Les colonnes incluent le genre, l'origine ethnique, le niveau d'éducation parental, le déjeuner, le cours de préparation au test, et les scores aux examens de mathématiques, lecture et écriture.

### Statistiques Descriptives des Scores
- **Scores moyens** : Les scores moyens sont similaires pour les trois matières : Mathématiques (66.09), Lecture (69.17), Écriture (68.05).
- **Écart-type** : Les scores en mathématiques et en écriture ont un écart-type légèrement plus élevé (environ 15) que les scores en lecture (environ 14.6), indiquant une plus grande dispersion des résultats.
- **Scores minimums** : Un score minimum de 0 en mathématiques indique des cas d'échec complet, ce qui pourrait nécessiter une investigation plus approfondie.

### Distribution des Scores
Les histogrammes des scores (mathématiques, lecture, écriture) montrent une distribution globalement normale, légèrement décalée vers la gauche pour les mathématiques, et plus symétrique pour la lecture et l'écriture. Cela suggère que la majorité des étudiants se situent dans la moyenne, avec quelques valeurs aberrantes aux extrémités.

### Impact du Genre sur les Scores
Les boîtes à moustaches montrent que les filles ont tendance à obtenir de meilleurs scores en lecture et en écriture, tandis que les garçons ont des scores légèrement supérieurs en mathématiques. Cependant, les différences ne sont pas drastiques et les distributions se chevauchent considérablement.

### Impact du Niveau d'Éducation Parental
Il semble y avoir une corrélation positive entre le niveau d'éducation parental et les scores des étudiants. Les étudiants dont les parents ont un niveau d'éducation plus élevé (par exemple, master's degree, bachelor's degree) ont tendance à avoir des scores moyens plus élevés dans toutes les matières, par rapport à ceux dont les parents ont un niveau d'éducation inférieur (par exemple, high school, some high school).

### Impact du Groupe Ethnique
Les scores varient entre les différents groupes ethniques. Le groupe E semble avoir les scores moyens les plus élevés dans toutes les matières, tandis que le groupe A a les scores moyens les plus bas. Cela pourrait indiquer des disparités socio-économiques ou des différences dans les ressources éducatives disponibles pour ces groupes.

### Impact du Cours de Préparation au Test
Les étudiants ayant suivi un cours de préparation au test ont généralement des scores moyens plus élevés dans toutes les matières par rapport à ceux qui n'en ont pas suivi. Cela suggère que ces cours peuvent être bénéfiques pour améliorer la performance aux examens.

### Conclusions et Prochaines Étapes
Cette AED a permis d'identifier plusieurs facteurs influençant la performance des étudiants. Pour les prochaines étapes, il serait intéressant de :
- Effectuer une analyse de régression pour quantifier l'impact de chaque variable sur les scores.
- Examiner les corrélations entre les scores des différentes matières.
- Approfondir l'analyse des valeurs aberrantes, notamment le score de 0 en mathématiques.
- Explorer des techniques de modélisation prédictive pour anticiper la performance des étudiants.

