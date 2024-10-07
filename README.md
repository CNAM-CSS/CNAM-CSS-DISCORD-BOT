# Discord Bot Project

Bienvenue sur le projet du Bot Discord du Cnam de Chalon-sur-Saône ! Voici le guide complet pour commencer, installer, exécuter et contribuer au bot.

- [Prérequis](#prérequis)
- [Contribuer au projet](#contribuer-au-projet)
  - [Forker le projet](#forker-le-projet)
  - [Créer le fichier `.env`](#créer-le-fichier-env)
  - [Activer un environnement virtuel](#activer-un-environnement-virtuel)
  - [Installer les dépendances](#installer-les-dépendances)
  - [Créer le Bot sur Discord](#créer-le-bot-sur-discord)
  - [Faire des modifications](#faire-des-modifications)
- [Exécution du Bot](#exécution-du-bot)
- [Dépannage](#dépannage)

---

## Prérequis

1. **Python 3.8 ou supérieur** : Assurez-vous que Python est installé sur votre machine. Vous pouvez vérifier la version en exécutant :
    ```
    python --version
    ```

2. **Git** : Installez Git pour cloner ce projet et soumettre des Pull Requests.

---

## Contribuer au projet

### 1. Créer le Bot sur Discord

1. Allez sur le [Discord Developer Portal](https://discord.com/developers/applications) et connectez-vous.
2. Cliquez sur **New Application** et nommez votre bot.
3. Dans l'onglet **Bot**, cliquez sur **Add Bot**.
4. Copiez le **TOKEN** du bot et collez-le dans votre fichier `.env`.
5. Dans l'onglet **OAuth2**, allez dans **URL Generator** :
    - Cochez `bot` sous **SCOPES**.
    - Cochez les permissions que vous voulez sous **BOT PERMISSIONS**.
    - Copiez l'URL générée et invitez le bot sur votre serveur.


### 2. Forker le projet

**Forkez le dépôt** [CNAM-CSS-DISCORD-BOT](https://github.com/CNAM-CSS/CNAM-CSS-DISCORD-BOT) sur GitHub pour obtenir votre propre copie du projet.


### 3. Créer le fichier `.env`

Vous devez configurer les variables d'environnement, en particulier le token de Discord. Créez un fichier `.env` à la racine du projet avec les informations suivantes :
```
DISCORD_TOKEN=Votre_Token_Discord
```

### 4. Activer un environnement virtuel

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet. Voici comment créer et activer un environnement virtuel avec `venv` :

1. Créez un environnement virtuel à la racine du projet :

   ```
   python -m venv venv
   ```

2. Activez l'environnement virtuel :

   - Sur **Windows** :
     ```
     venv\Scripts\activate
     ```
   - Sur **Linux/macOS** :
     ```
     source venv/bin/activate
     ```

3. Pour **désactiver** l'environnement virtuel, exécutez simplement :
   ```
   deactivate
   ```
### 5. Installer les dépendances

À la racine du projet, installez les dépendances :

```sh
pip install -r requirements.txt
```
### 6. Faire des modifications

1. **Créer une branche pour vos modifications**

   Créez une nouvelle branche pour travailler sur vos modifications :

   ```
   git checkout -b nom-de-votre-branche
   ```

2. **Faire vos modifications et tester le bot**

   Faites vos modifications et testez le bot localement pour vous assurer qu'il fonctionne correctement.

3. **Committer vos changements**

   Enregistrez vos modifications avec un commit :

   ```
   git add .
   git commit -m "Description des changements"
   ```

4. **Pusher vos changements**

   Envoyez vos modifications vers votre branche sur GitHub :

   ```
   git push origin nom-de-votre-branche
   ```

5. **Créer une Pull Request**

   Créez une **Pull Request** sur le dépôt principal pour proposer vos modifications. Ajoutez une description claire des changements que vous avez apportés.

---

## Exécution du Bot

Une fois l'installation terminée et les configurations effectuées, vous pouvez lancer le bot avec la commande suivante :

```bash
python main.py
```

Ton bot est maintenant prêt à agir sur ton serveur ! 🥳

---

## Dépannage

- **Dépannage** : Si vous rencontrez des problèmes ou avez des questions, rendez-vous sur le [Discord du cnam](https://discord.gg/spMXekm9bq)🙏

---

Et voilà, votre bot est prêt à animer votre serveur ! Amusez-vous bien et n'oubliez pas, la programmation est encore plus sympa quand on s'amuse en le faisant. 🚀😄
