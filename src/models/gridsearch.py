import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Chargement des données
X_train = pd.read_csv('data/processed_data/X_train_scaled.csv')
y_train = pd.read_csv('data/processed_data/y_train.csv').values.ravel()

# Définition du modèle et des hyperparamètres
model = RandomForestRegressor(random_state=42)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}

# Exécution de GridSearchCV
grid_search = GridSearchCV(model, param_grid, cv=5, scoring='neg_mean_squared_error', verbose=2)
grid_search.fit(X_train, y_train)

# Enregistrement des meilleurs paramètres
best_params = grid_search.best_params_
with open('models/best_params.pkl', 'wb') as f:
    pickle.dump(best_params, f)

print("Meilleurs paramètres enregistrés dans models/best_params.pkl")
