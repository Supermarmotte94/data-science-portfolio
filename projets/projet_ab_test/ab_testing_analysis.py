import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind
import numpy as np

# Charger le dataset
df = pd.read_csv('ab_data.csv')

# Nettoyage et préparation des données
# Supprimer les lignes où la page d'atterrissage n'est pas cohérente avec le groupe
df = df[((df['group'] == 'treatment') == (df['landing_page'] == 'new_page')) | \
        ((df['group'] == 'control') == (df['landing_page'] == 'old_page'))]

# Vérifier les doublons d'utilisateurs
df = df.drop_duplicates(subset=['user_id'], keep=False)

# Calculer les métriques de conversion
control_group = df[df['group'] == 'control']
treatment_group = df[df['group'] == 'treatment']

control_conversion_rate = control_group['converted'].mean()
treatment_conversion_rate = treatment_group['converted'].mean()

print(f"Taux de conversion du groupe de contrôle : {control_conversion_rate:.4f}")
print(f"Taux de conversion du groupe de traitement : {treatment_conversion_rate:.4f}")

# Effectuer un test Z pour comparer les proportions
# Nombre de conversions et de non-conversions pour chaque groupe
n_control = control_group.shape[0]
n_treatment = treatment_group.shape[0]

x_control = control_group['converted'].sum()
x_treatment = treatment_group['converted'].sum()

# Calculer la statistique Z et la p-value
from statsmodels.stats.proportion import proportions_ztest

stat, pval = proportions_ztest([x_control, x_treatment], [n_control, n_treatment])

print(f"Statistique Z : {stat:.4f}")
print(f"P-value : {pval:.4f}")

# Interprétation des résultats
alpha = 0.05
if pval < alpha:
    print("Rejeter l'hypothèse nule. Il y a une différence significative entre les taux de conversion.")
else:
    print("Ne pas rejeter l'hypothèse nule. Il n'y a pas de différence significative entre les taux de conversion.")

# Analyse supplémentaire (si nécessaire, par exemple, pour les revenus ou autres métriques)
# Pour ce dataset, 'converted' est la métrique principale, mais on pourrait étendre à d'autres si disponibles.

# Sauvegarder les résultats si besoin
# pd.DataFrame({'metric': ['control_conversion_rate', 'treatment_conversion_rate', 'z_statistic', 'p_value'],
#               'value': [control_conversion_rate, treatment_conversion_rate, stat, pval]}).to_csv('ab_test_results.csv', index=False)

print("Analyse du test A/B terminée.")


