import os
import pandas as pd
from sklearn.model_selection import train_test_split
from check_structure import check_existing_file, check_existing_folder
from sklearn.preprocessing import MinMaxScaler

def main():

    # Chemins d'accès
    train_path = 'data/processed_data/X_train.csv'
    test_path = 'data/processed_data/X_test.csv'
    scaled_train_path = 'data/processed_data/X_train_scaled.csv'
    scaled_test_path = 'data/processed_data/X_test_scaled.csv'

    # Charger les données
    X_train = pd.read_csv(train_path)
    X_test = pd.read_csv(test_path)

        
    output_folderpath = "data/processed_data/"


    # Appliquer le MinMaxScaler
    scaler = MinMaxScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

    
    # Créer les répertoires si nécessaire
    os.makedirs('data/processed_data', exist_ok=True)

    
        
    # Sauvegarder les données normalisées
    for file, filename in zip([X_train_scaled, X_test_scaled], ['X_train_scaled', 'X_test_scaled']):
        output_filepath = os.path.join(output_folderpath, f'{filename}.csv')
        if check_existing_file(output_filepath):
            file.to_csv(output_filepath, index=False) 


if __name__ == "__main__": main()
