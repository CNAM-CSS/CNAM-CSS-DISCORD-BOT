# Discord Bot Project

Bienvenue sur le projet du Bot discord du Cnam de Chalon-sur-Saône

- [prérequis](#prérequis)
- [Création du Bot sur Discord](#création-du-bot-sur-discord)
- [Contribuer au projet](#contribuer-au-projet)
- [Activation d'un environnement virtuel](#activation-dun-environnement-virtuel)
- [Installation du projet](#installation-du-projet )
- [Exécution du Bot](#exécution-du-bot)
- [Dépannage](#dépannage)

---

## Prérequis

1. **Python 3.8 ou supérieur** : Assurez-vous que Python est installé sur votre machine. Vous pouvez vérifier la version en exécutant :
    ```
    python --version
    ```

2. **Git** : Installez Git pour cloner ce projet et soumettre des Pull Requests.

## Création d'un Bot sur Discord

1. Allez sur le [Discord Developer Portal](https://discord.com/developers/applications) et connectez-vous.
2. Cliquez sur **New Application** et nommez votre bot.
3. Dans l'onglet **Bot**, cliquez sur **Add Bot**.
4. Copiez le **TOKEN** du bot et collez-le dans votre fichier `.env`.
5. Dans l'onglet **OAuth2**, allez dans **URL Generator** :
    - Cochez `bot` sous **SCOPES**.
    - Cochez les permissions que vous voulez sous **BOT PERMISSIONS**.
    - Copiez l'URL générée et invitez le bot sur votre serveur.

---

## Contribuer au projet

Voici comment vous pouvez contribuer :

1. **Forkez le dépôt** [CNAM-CSS-DISCORD-BOT](https://github.com/CNAM-CSS/CNAM-CSS-DISCORD-BOT) sur GitHub.
2. Créez une nouvelle branche pour vos modifications :

   ```
   git checkout -b nom-de-votre-branche
   ```
2. suivez les étapes  [Activation d'un environnement virtuel](#activation-dun-environnement-virtuel)
3. Faites vos modifications et testez votre bot localement.
4. **Committez** vos changements :

```
git add .
git commit -m "Description des changements"
```

5. **Pushez** vos changements sur votre branche :

```
git push origin nom-de-votre-branche
```

6. Créez une **Pull Request** sur le dépôt principal. Ajoutez une description des changements apportés.

## Installation du projet
### Création du fichier `.env`

Vous devez configurer les variables d'environnement, en particulier le token de Discord. Créez un fichier `.env` à la racine du projet avec les informations suivantes :
```
DISCORD_TOKEN=Votre_Token_Discord
```
---
### Activation d'un environnement virtuel

Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances du projet. Voici comment créer et activer un environnement virtuel avec venv par exemple :

### Création de l'environnement virtuel

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
3. Pour désactiver l'environnement virtuel, exécutez simplement :
```
deactivate
```
### Installer les dépendances 
à la racine du projet :
 ```
 pip install -r requirements.txt
  ```

## Exécution du Bot
Une fois l’installation terminée et les configurations effectuées, vous pouvez lancer le bot avec la commande suivante :

```bash
python main.py
```

pour run le bot discord tapez python main.py
## Dépannage

- **Dépannage** : Si vous rencontrez des problèmes ou avez des questions rendez vous sur le disord 

