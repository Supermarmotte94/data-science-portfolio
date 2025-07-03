import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Télécharger les ressources NLTK nécessaires
nltk.download("stopwords")
nltk.download("punkt")

# Charger le dataset
df = pd.read_csv("IMDB_Dataset.csv")

# Prendre un échantillon plus petit pour des raisons de performance
df = df.sample(n=5000, random_state=42) # Réduire à 5000 échantillons

# Afficher les premières lignes du dataset
print("Premières lignes du dataset :")
print(df.head())

# Afficher les informations générales sur le dataset
print("\nInformations générales sur le dataset :")
print(df.info())

# Vérifier les valeurs manquantes
print("\nValeurs manquantes :")
print(df.isnull().sum())

# Prétraitement du texte
stemmer = PorterStemmer()
stopwords_english = set(stopwords.words("english"))

def preprocess_text(text):
    # Supprimer les balises HTML
    text = re.sub(r"<.*?>", "", text)
    # Supprimer les caractères spéciaux et les chiffres
    text = re.sub(r"[^a-zA-Z]", " ", text)
    # Convertir en minuscules
    text = text.lower()
    # Tokenisation et suppression des mots vides (stopwords) et stemming
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stopwords_english]
    return " ".join(words)

print("\nPrétraitement du texte en cours...")
df["review_processed"] = df["review"].apply(preprocess_text)
print("Prétraitement du texte terminé.")

# Mapper les sentiments en valeurs numériques
df["sentiment"] = df["sentiment"].map({"positive": 1, "negative": 0})

# Séparer les données en ensembles d\\\'entraînement et de test
X = df["review_processed"]
y = df["sentiment"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorisation TF-IDF
print("\nVectorisation TF-IDF en cours...")
tfidf_vectorizer = TfidfVectorizer(max_features=5000) # Limiter le nombre de features pour la performance
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)
print("Vectorisation TF-IDF terminée.")

# Entraînement du modèle Naive Bayes Multinomial
print("\nEntraînement du modèle Naive Bayes Multinomial en cours...")
model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
print("Entraînement du modèle terminé.")

# Prédictions et évaluation
y_pred = model.predict(X_test_tfidf)

print("\nPerformance du modèle :")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report :")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix :")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Visualisation de la matrice de confusion
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Negative", "Positive"], yticklabels=["Negative", "Positive"])
plt.xlabel("Prédit")
plt.ylabel("Réel")
plt.title("Matrice de Confusion")
plt.savefig("confusion_matrix.png")
plt.show()

print("\nAnalyse de sentiments terminée. Les résultats et la matrice de confusion ont été sauvegardés.")

