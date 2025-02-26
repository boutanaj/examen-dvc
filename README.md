# Examen DVC et Dagshub
Dans ce dépôt vous trouverez l'architecture proposée pour mettre en place la solution de l'examen.

## Architecture Readme:

```bash       
├── examen_dvc          
│   ├── data
│   │   ├── predictions       <-  contient le fichier predictions.csv résultat du script evaluate_model.py
│   │   ├── processed_data    <-  contient les données entrainées et normalisées résultat du script 
|   |   |                          split_scale_data.py
│   │   └── raw_data          <-  contient le jeux de données initial importé
│   │     
│   ├── metrics               <-  contient le fichier scores.json qui calcule r2 et mse par le script 
|   |                             evaluate_model.py
│   │
│   ├── models                <-  contient les fichiers best_params.pkl et trained_model.joblib résultat 
|   |                              respectivement des scripts gridsearch.py et train_model.py
│   │
│   ├── src                    
│   │   ├── data              <-  contient les scripts pour la préparation des données : 
│   │   │   ├── check_structure.py
|   |   |   ├── split_scale_data.py
│   │   └── models            <-  contient les scripts pour entrainer les données, pour le calcul des 
|   |       |                      meilleurs paramètres et des prédictions:
│   │       ├── gridsearch.py
│   │       ├── train_model.py
│   │       └── evaluate_model.py
│   └── README.md             
```

## Reproduction de la Pipeline DVC

Ce document décrit les étapes à suivre pour reproduire la pipeline DVC de ce projet.


### Prérequis

Les données sont téléchargées à travers le lien suivant : https://datascientest-mlops.s3.eu-west-1.amazonaws.com/mlops_dvc_fr/raw.csv.


* Python 3.6+
* DVC (Data Version Control)
* Git
* Un compte Dagshub

### Étapes à suivre

1.  **Cloner le dépôt :**

    ```bash
    git clone https://github.com/boutanaj/examen-dvc.git
    cd examen-dvc/
    ```

2.  **Création et activation de l'environnement virtuel :**

    ```bash
    virtualenv env
    source env/bin/activate
    ```

3.  **Installation des packages nécessaires :**

    ```bash
    cd examen-dvc
    pip install -r requirements.txt
    ```

4.  **Configuration des identifiants DVC :**

    ```bash
    dvc remote modify origin --local access_key_id VOTRE_ACCESS_KEY
    dvc remote modify origin --local secret_access_key VOTRE_SECRET_ACCESS_KEY
    ```

    * Remplacez `VOTRE_ACCESS_KEY` et `VOTRE_SECRET_ACCESS_KEY` par vos véritables identifiants Dagshub.

5.  **Reproductibilité de la pipeline :**



    * **Nettoyer le cache et les données :**

        ```bash
        rm -rf data/raw_data
        rm -rf .dvc/cache
        ```

        Ces commandes suppriment les données locales et le cache DVC, forçant DVC à récupérer les données du stockage distant.


    * **Récupérer les données :**

        ```bash
        dvc pull
        ```

        Cette commande récupère les données mises en cache depuis le stockage distant Dagshub.

    * **Exécuter la pipeline :**

        ```bash
        dvc repro
        ```

        DVC utilisera les informations stockées dans le fichier `dvc.yaml` pour déterminer quelles étapes doivent être réexécutées.

    * **Localisation des données :**

        * Les informations qui pointent vers l'endroit où se trouvent les données sont stockées dans le fichier `dvc.yaml`. Ce fichier contient les métadonnées (sommes de contrôle, tailles, etc.) des données de sortie de chaque étape.
        * Les données elles-mêmes sont stockées dans le répertoire `.dvc/cache`. DVC utilise les sommes de contrôle (MD5 par défaut) des données pour les stocker dans le cache.
        * Pour vérifier l'état des données et des étapes, vous pouvez utiliser la commande `dvc status`.

    * **Pousser les modifications (si nécessaire) :**

        ```bash
        dvc push
        ```