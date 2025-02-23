import os
import pandas as pd
from sklearn.model_selection import train_test_split
from check_structure import check_existing_file, check_existing_folder
from sklearn.preprocessing import MinMaxScaler


def main():
    df = pd.read_csv("data/raw_data/raw.csv", index_col=0)
    #if 'date' in df.columns:
       # df.drop('date', axis=1, inplace=True)
    X = df.drop("silica_concentrate", axis=1)
    y = df['silica_concentrate']

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, random_state=0, test_size=0.20)

    output_folderpath = "data/processed_data/"

    if check_existing_folder(output_folderpath):
        os.makedirs(output_folderpath)

    for file, filename in zip([X_train, X_test, y_train, y_test], ['X_train', 'X_test', 'y_train', 'y_test']):
        output_filepath = os.path.join(output_folderpath, f'{filename}.csv')
        if check_existing_file(output_filepath):
            file.to_csv(output_filepath, index=False) 


    

    # Appliquer le MinMaxScaler
    scaler = MinMaxScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

    
    # Créer les répertoires si nécessaire
    #os.makedirs('data/processed_data', exist_ok=True)

    
        
    # Sauvegarder les données normalisées
    for file, filename in zip([X_train_scaled, X_test_scaled], ['X_train_scaled', 'X_test_scaled']):
        output_filepath = os.path.join(output_folderpath, f'{filename}.csv')
        if check_existing_file(output_filepath):
            file.to_csv(output_filepath, index=False) 


if __name__ == "__main__": main()
