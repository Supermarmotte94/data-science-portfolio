import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Charger le dataset
df = pd.read_csv("Mall_Customers.csv")

# Afficher les premières lignes du dataset
print("Premières lignes du dataset :")
print(df.head())

# Afficher les informations générales sur le dataset
print("\nInformations générales sur le dataset :")
print(df.info())

# Vérifier les valeurs manquantes
print("\nValeurs manquantes :")
print(df.isnull().sum())

# Renommer les colonnes pour une meilleure lisibilité
df.rename(columns={
    "Annual Income (k$)": "Annual_Income_k",
    "Spending Score (1-100)": "Spending_Score",
    "Genre": "Gender"
}, inplace=True)

# Analyse exploratoire des données pour la segmentation
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.histplot(df["Age"], kde=True)
plt.title("Distribution de l\"Âge")

plt.subplot(1, 2, 2)
sns.histplot(df["Annual_Income_k"], kde=True)
plt.title("Distribution du Revenu Annuel (k$)")
plt.tight_layout()
plt.savefig("age_income_distribution.png")
plt.show()

plt.figure(figsize=(6, 5))
sns.histplot(df["Spending_Score"], kde=True)
plt.title("Distribution du Score de Dépense")
plt.savefig("spending_score_distribution.png")
plt.show()

plt.figure(figsize=(6, 5))
sns.countplot(x="Gender", data=df)
plt.title("Distribution du Genre")
plt.savefig("gender_distribution.png")
plt.show()

# Sélection des caractéristiques pour le clustering (Revenu Annuel et Score de Dépense)
X = df[["Annual_Income_k", "Spending_Score"]]

# Standardisation des données
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Détermination du nombre optimal de clusters avec la méthode du coude
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init="k-means++", random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker="o", linestyle="--")
plt.title("Méthode du Coude pour K-Means")
plt.xlabel("Nombre de Clusters (K)")
plt.ylabel("WCSS")
plt.savefig("elbow_method.png")
plt.show()

# Application de K-Means avec le nombre optimal de clusters (par exemple, 5 d\'après la méthode du coude)
k = 5  # Supposons que 5 est le nombre optimal de clusters
kmeans = KMeans(n_clusters=k, init="k-means++", random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Visualisation des clusters
plt.figure(figsize=(10, 8))
sns.scatterplot(x="Annual_Income_k", y="Spending_Score", hue="Cluster", data=df, palette="viridis", s=100)
plt.scatter(kmeans.cluster_centers_[:, 0] * scaler.scale_[0] + scaler.mean_[0],
            kmeans.cluster_centers_[:, 1] * scaler.scale_[1] + scaler.mean_[1],
            s=300, c="red", marker="X", label="Centroids")
plt.title("Segmentation Client par Revenu Annuel et Score de Dépense")
plt.xlabel("Revenu Annuel (k$)")
plt.ylabel("Score de Dépense (1-100)")
plt.legend()
plt.savefig("customer_segmentation_clusters.png")
plt.show()

# Analyse des caractéristiques de chaque cluster
print("\nCaractéristiques de chaque cluster :")
print(df.groupby("Cluster")[["Age", "Annual_Income_k", "Spending_Score"]].mean())
print(df.groupby("Cluster")["Gender"].value_counts(normalize=True).unstack())

print("\nAnalyse de segmentation client terminée. Les graphiques ont été sauvegardés.")

