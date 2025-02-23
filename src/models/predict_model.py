import pandas as pd
import numpy as np
import joblib
import json
import os
from sklearn.metrics import r2_score, mean_squared_error

# Charger les données et le modèle
loaded_model = joblib.load("models/trained_model.joblib")

X_test_scaled = pd.read_csv('data/processed_data/X_test_scaled.csv')
y_test = pd.read_csv('data/processed_data/y_test.csv')
y_test = np.ravel(y_test)

# Prediction
y_pred = loaded_model.predict(X_test_scaled)

# Vérifier si le dossier de sortie existe, sinon le créer
output_folderpath = "data/predictions/"
os.makedirs(output_folderpath, exist_ok=True)  # Crée le dossier s'il n'existe pas

# Enregistrer les prédictions
predictions_df = pd.DataFrame(y_pred, columns=['silica_concentrate'])
predictions_df.to_csv(output_folderpath + "predictions.csv", index=None)
print("Prédictions enregistrées dans data/predictions/predictions.csv")

# Metrics
scores = {
    "r2": r2_score(y_test, y_pred),
    "mse": mean_squared_error(y_test, y_pred)
}

# Sauvegarde des metrics
output_metrics_folder = "metrics"
os.makedirs(output_metrics_folder, exist_ok=True)  # Crée le dossier des metrics s'il n'existe pas
with open(output_metrics_folder + "/scores.json", 'w') as f:
    json.dump(scores, f)
    print("Les metrics sont sauvegardés avec succès!")
