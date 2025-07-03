## Résumé de l'Analyse de Sentiments des Revues de Films

Ce projet a pour objectif de classer le sentiment (positif ou négatif) des revues de films en utilisant des techniques de traitement du langage naturel (TLN) et un modèle d'apprentissage automatique. Il démontre les compétences en prétraitement de texte, vectorisation et modélisation pour la classification de texte.

### Aperçu du Dataset
Le dataset `IMDB_Dataset.csv` contient 50 000 revues de films, chacune associée à un sentiment (`positive` ou `negative`). Pour des raisons de performance et de temps d'exécution dans cet environnement, un échantillon aléatoire de **5 000 revues** a été utilisé pour l'analyse.

### Prétraitement du Texte
Les étapes de prétraitement suivantes ont été appliquées aux revues :
1.  **Suppression des balises HTML** : Les balises HTML (`<br />`) ont été retirées du texte.
2.  **Nettoyage des caractères spéciaux et chiffres** : Seuls les caractères alphabétiques ont été conservés.
3.  **Conversion en minuscules** : Tout le texte a été converti en minuscules pour uniformiser les mots.
4.  **Tokenisation et suppression des mots vides (stopwords)** : Le texte a été divisé en mots individuels (tokens), et les mots courants sans signification sémantique (comme 'le', 'la', 'un', 'une' en anglais) ont été supprimés.
5.  **Stemming** : Les mots ont été réduits à leur racine (par exemple, 'running', 'runs', 'ran' deviennent 'run') pour réduire la complexité du vocabulaire.

### Vectorisation TF-IDF
Après le prétraitement, les revues ont été converties en représentations numériques à l'aide de **TF-IDF (Term Frequency-Inverse Document Frequency)**. Cette technique attribue un poids à chaque mot en fonction de sa fréquence dans une revue et de sa rareté dans l'ensemble du corpus, permettant au modèle de comprendre l'importance relative des mots.

### Modélisation et Évaluation
Un modèle **Naive Bayes Multinomial** a été entraîné sur 80% des données (4 000 revues) et évalué sur les 20% restants (1 000 revues).

Les performances du modèle sont les suivantes :
-   **Accuracy (Précision globale)** : 0.8370 (83.7%)
-   **Rapport de Classification** :
    -   **Sentiment Négatif (0)** : Précision de 0.84, Rappel de 0.83, F1-score de 0.84
    -   **Sentiment Positif (1)** : Précision de 0.83, Rappel de 0.84, F1-score de 0.84

### Matrice de Confusion
La matrice de confusion fournit une vue détaillée des prédictions du modèle :

|             | Prédit Négatif | Prédit Positif |
| :---------- | :------------- | :------------- |
| **Réel Négatif** | 421            | 85             |
| **Réel Positif** | 78             | 416            |

-   **Vrais Positifs (TP)** : 416 revues positives ont été correctement identifiées comme positives.
-   **Vrais Négatifs (TN)** : 421 revues négatives ont été correctement identifiées comme négatives.
-   **Faux Positifs (FP)** : 85 revues négatives ont été incorrectement identifiées comme positives (Erreur de Type I).
-   **Faux Négatifs (FN)** : 78 revues positives ont été incorrectement identifiées comme négatives (Erreur de Type II).

### Conclusions
Le modèle entraîné a démontré une bonne capacité à classer le sentiment des revues de films, avec une précision d'environ 83.7%. Les performances sont équilibrées pour les deux classes (positif et négatif), ce qui indique que le modèle ne favorise pas un sentiment par rapport à l'autre.

Ce projet met en évidence les étapes clés d'un pipeline d'analyse de sentiments, de la collecte de données au déploiement d'un modèle de classification, en passant par le prétraitement du texte et l'évaluation des performances. Il est un excellent exemple de l'application du TLN à des problèmes commerciaux réels, comme la compréhension des retours clients ou l'analyse de l'opinion publique.

