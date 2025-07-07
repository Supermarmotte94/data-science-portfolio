import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le dataset
df = pd.read_csv('StudentsPerformance.csv')

# Afficher les premières lignes du dataset
print('Premières lignes du dataset :')
print(df.head())

# Afficher les informations générales sur le dataset
print('\nInformations générales sur le dataset :')
print(df.info())

# Afficher les statistiques descriptives
print('\nStatistiques descriptives :')
print(df.describe())

# Vérifier les valeurs manquantes
print('\nValeurs manquantes :')
print(df.isnull().sum())

# Analyse de la distribution des scores
plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 1)
sns.histplot(df['math score'], kde=True)
plt.title('Distribution des scores en mathématiques')

plt.subplot(1, 3, 2)
sns.histplot(df['reading score'], kde=True)
plt.title('Distribution des scores en lecture')

plt.subplot(1, 3, 3)
sns.histplot(df['writing score'], kde=True)
plt.title('Distribution des scores en écriture')

plt.tight_layout()
plt.savefig('score_distributions.png')
plt.show()

# Analyse des scores par genre
plt.figure(figsize=(12, 6))
sns.boxplot(x='gender', y='math score', data=df)
plt.title('Scores en mathématiques par genre')
plt.savefig('math_score_by_gender.png')
plt.show()

# Analyse des scores par niveau d\'éducation parental
plt.figure(figsize=(14, 7))
sns.boxplot(x='parental level of education', y='math score', data=df)
plt.title('Scores en mathématiques par niveau d\'éducation parental')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('math_score_by_parental_education.png')
plt.show()

# Analyse des scores par groupe ethnique
plt.figure(figsize=(14, 7))
sns.boxplot(x='race/ethnicity', y='math score', data=df)
plt.title('Scores en mathématiques par groupe ethnique')
plt.tight_layout()
plt.savefig('math_score_by_ethnicity.png')
plt.show()

# Analyse de l\'impact du cours de préparation au test
plt.figure(figsize=(12, 6))
sns.boxplot(x='test preparation course', y='math score', data=df)
plt.title('Scores en mathématiques par cours de préparation au test')
plt.savefig('math_score_by_test_prep.png')
plt.show()

print('\nAnalyse exploratoire des données terminée. Les graphiques ont été sauvegardés.')

