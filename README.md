# Examen DVC et Dagshub
Dans ce dépôt vous trouverez l'architecture proposé pour mettre en place la solution de l'examen.
Les données sont téléchargées à travers le lien suivant : https://datascientest-mlops.s3.eu-west-1.amazonaws.com/mlops_dvc_fr/raw.csv.

```bash       
├── examen_dvc          
│   ├── data
│   │   ├── predictions       <-  contient le fichier "predictions.csv" résultat du script "evaluate_model.py"
│   │   ├── processed_data    <-  contient les données entrainées et normalisées résultat du script 
|   |                             "split_scale_data.py"
│   │   └── raw_data          <-  contient le jeux de données initial importé via le script "import_raw_data.
|   |                             py"
│   │     
│   ├── metrics               <-  contient le fichier "scores.json" qui calcule "r2" et "mse" par le script 
|   |                             "evaluate_model.py"
│   │
│   ├── models                <-  contient les fichiers: "best_params.pkl" résultat du script "gridsearch.
|   |                             py" et "trained_model.joblib" résultat du script "train_model.py"
│   │
│   ├── src                    
│   │   ├── data              <-  contient les scripts pour la préparation des données : 
│   │   │   ├── check_structure.py
|   |   |   ├── split_scale_data.py
│   │   └── models            <-  contient les scripts pour entrainer les données, pour le calcul des 
|   |                             meilleurs paramèters et des predictions:
│   │       ├── gridsearch.py
│   │       ├── train_model.py
│   │       └── evaluate_model.py
│   └── README.md             
```
