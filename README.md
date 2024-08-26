# WEBAPP_CHAT

## Description

WEBAPP_CHAT est une application web de chat multi-utilisateurs développée avec Flask. L'application permet aux utilisateurs de s'inscrire, de se connecter, et de discuter dans trois canaux de chat distincts : Général, Loisir, et Tech. Les utilisateurs peuvent envoyer des messages texte ainsi que des images dans les canaux de discussion.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- Python 3.x
- `pip` (gestionnaire de paquets Python)


## Installation

1. **Installer les dépendances** :

    ```bash
   pip install -r requirements.txt

2. **Initialiser la base de données** :

   Sur macOS/Linux : 

   ```bash
   export FLASK_APP=app.py

   ```
   Sur Windows : 
   
   ```bash
   set FLASK_APP=app.py

   ```

3. **Initialiser les migrations** :

   ```bash
   flask db init

   ```

4. **Créer une migration : ** :

   ```bash
   flask db migrate -m "Initial migration"


   ```
   
5. **Appliquer la migration** :

   ```bash
   flask db upgrade


   ```
6. **Lancer l'application** :

   Il suffit maintenant d'exécuter app.py.
