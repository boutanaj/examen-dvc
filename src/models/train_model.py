import pandas as pd
import pickle
import joblib
from sklearn.ensemble import RandomForestRegressor

# Charger les données normalisées
X_train = pd.read_csv('data/processed_data/X_train_scaled.csv')
y_train = pd.read_csv('data/processed_data/y_train.csv').values.ravel()

# Charger les meilleurs paramètres
with open('models/best_params.pkl', 'rb') as f:
    best_params = pickle.load(f)

# Entraîner le modèle avec les meilleurs paramètres
model = RandomForestRegressor(**best_params, random_state=42)
model.fit(X_train, y_train)


# Sauvegarder le modèle entraîné
model_filename = 'models/trained_model.joblib'
joblib.dump(model, model_filename)
print("Modèle entraîné et sauvegardé avec succès dans models/trained_model.joblib")
