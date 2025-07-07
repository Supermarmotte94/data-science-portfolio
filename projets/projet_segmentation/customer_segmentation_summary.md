## Résumé de l'Analyse de Segmentation Client

Ce projet a utilisé un ensemble de données de clients de centre commercial pour effectuer une segmentation client à l'aide de l'algorithme K-Means. L'objectif est d'identifier des groupes de clients distincts basés sur leur âge, revenu annuel et score de dépense, afin d'aider les équipes marketing à cibler leurs stratégies plus efficacement.

### Aperçu du Dataset
Le dataset `Mall_Customers.csv` contient 200 entrées avec les colonnes suivantes : `CustomerID`, `Gender`, `Age`, `Annual Income (k$)`, et `Spending Score (1-100)`. Aucune valeur manquante n'a été détectée.

### Analyse Exploratoire des Données (AED)
- **Distribution de l'Âge** : La majorité des clients ont entre 20 et 40 ans, avec une distribution légèrement asymétrique.
- **Distribution du Revenu Annuel** : Le revenu annuel est principalement concentré entre 40k$ et 80k$, avec quelques clients ayant des revenus plus élevés.
- **Distribution du Score de Dépense** : Le score de dépense est assez uniformément réparti, avec des pics autour de 40-50 et 70-80.
- **Distribution du Genre** : Il y a légèrement plus de clientes (Femmes) que de clients (Hommes) dans le dataset.

### Segmentation Client avec K-Means
Pour la segmentation, les caractéristiques `Annual Income (k$)` et `Spending Score (1-100)` ont été utilisées. Les données ont été standardisées avant l'application de K-Means.

La **méthode du coude** a été utilisée pour déterminer le nombre optimal de clusters. Le graphique de la WCSS (Within-Cluster Sum of Squares) en fonction du nombre de clusters a montré un coude prononcé à **K=5**, suggérant que 5 clusters sont optimaux pour ce dataset.

L'algorithme K-Means a ensuite été appliqué avec 5 clusters, et les clusters ont été visualisés sur un graphique de dispersion du revenu annuel par rapport au score de dépense.

### Caractéristiques des Clusters
L'analyse des caractéristiques moyennes de chaque cluster a révélé les profils suivants :

- **Cluster 0 (Revenu Moyen, Dépense Moyenne)**:
  - Âge moyen: ~42.7 ans
  - Revenu annuel moyen: ~55.3 k$
  - Score de dépense moyen: ~49.5
  - Majoritairement des femmes (59.3%)
  - *Profil*: Clients établis, avec un revenu et un score de dépense dans la moyenne. Potentiel pour des offres ciblées.

- **Cluster 1 (Revenu Élevé, Dépense Élevée - 

Clients Cibles)**:
  - Âge moyen: ~32.7 ans
  - Revenu annuel moyen: ~86.5 k$
  - Score de dépense moyen: ~82.1
  - Légèrement plus de femmes (53.8%)
  - *Profil*: Jeunes adultes avec un revenu et un score de dépense élevés. Ce sont les clients les plus précieux, à cibler avec des offres premium et des programmes de fidélité.

- **Cluster 2 (Revenu Faible, Dépense Élevée - Nouveaux Clients / Impulsifs)**:
  - Âge moyen: ~25.3 ans
  - Revenu annuel moyen: ~25.7 k$
  - Score de dépense moyen: ~79.4
  - Majoritairement des femmes (59.1%)
  - *Profil*: Jeunes clients avec un faible revenu mais un score de dépense très élevé. Ils pourraient être des acheteurs impulsifs ou des nouveaux clients. Des promotions et des offres attractives pourraient les fidéliser.

- **Cluster 3 (Revenu Élevé, Dépense Faible - Clients Prudents)**:
  - Âge moyen: ~41.1 ans
  - Revenu annuel moyen: ~88.2 k$
  - Score de dépense moyen: ~17.1
  - Légèrement plus d'hommes (54.3%)
  - *Profil*: Clients plus âgés avec un revenu élevé mais un faible score de dépense. Ils sont probablement plus prudents dans leurs dépenses. Des offres personnalisées sur des produits de luxe ou des services haut de gamme pourraient les intéresser.

- **Cluster 4 (Revenu Faible, Dépense Faible - Clients Économes)**:
  - Âge moyen: ~45.2 ans
  - Revenu annuel moyen: ~26.3 k$
  - Score de dépense moyen: ~20.9
  - Majoritairement des femmes (60.9%)
  - *Profil*: Clients plus âgés avec un faible revenu et un faible score de dépense. Ils sont probablement très sensibles aux prix. Des promotions, des réductions et des programmes de fidélité basés sur le volume pourraient les encourager à dépenser davantage.

### Conclusions et Recommandations Marketing
Cette segmentation permet au centre commercial de mieux comprendre ses clients et d'adapter ses stratégies marketing :
- **Ciblage précis** : Développer des campagnes marketing spécifiques pour chaque segment.
- **Optimisation des offres** : Proposer des produits et services qui correspondent aux préférences et au pouvoir d'achat de chaque groupe.
- **Fidélisation** : Mettre en place des programmes de fidélité adaptés aux comportements de dépense.
- **Acquisition** : Identifier les caractéristiques des segments à fort potentiel pour attirer de nouveaux clients similaires.

Ce projet démontre des compétences en nettoyage de données, analyse exploratoire, clustering (K-Means), et interprétation des résultats pour des recommandations commerciales concrètes.

