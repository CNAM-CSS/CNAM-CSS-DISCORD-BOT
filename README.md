# Discord Bot Project

Bienvenue sur le projet du Bot Discord du Cnam de Chalon-sur-Saône ! Voici le guide complet pour débuter, installer, exécuter et contribuer au bot. Si vous contribuez au bot et qu'une de vos Pull Requests est acceptée, vous obtiendrez le rôle "dev" sur le Discord du CNAM et serez mentionné parmi les contributeurs.

- [Prérequis](#prérequis)
- [technos](#technos)
- [Contribuer au projet](#contribuer-au-projet)
  - [Créer le bot sur discord](#1-créer-le-bot-sur-discord)
  - [Forker et cloner le projet](#2-forker-et-cloner-le-projet)
  - [Créer le fichier `.env`](#3-créer-le-fichier-env)
  - [Activer un environnement virtuel](#4-activer-un-environnement-virtuel)
  - [Installer les dépendances](#5-installer-les-dépendances)
  - [Exécuter le Bot](#6-exécuter-le-bot)
  - [Faire des modifications](#7-faire-des-modifications)
- 
- [Aide](#aide)
- [Contributeurs](#contributeurs)

---

## Prérequis

1. **Python 3.8 ou supérieur** : Assurez-vous que Python est installé sur votre machine. Vous pouvez vérifier la version en exécutant :
    ```
    python --version
    ```

2. **Git** : Installez Git pour cloner ce projet et soumettre des Pull Requests.

---
## technos

Le projet utilise principalement deux bibliothèques Python : **Discord.py** et **Pycord**.

- [**Discord.py**](https://discordpy.readthedocs.io/en/stable/) est une bibliothèque conçue pour créer des bots Discord en Python. Elle permet de gérer les événements, les commandes et les permissions au sein des serveurs Discord.
  
- [**Pycord**](https://docs.pycord.dev/en/stable/) est un fork de Discord.py, qui prend en charge les **slash commands** et les interactions modernes. Elle est plus adaptée aux nouvelles fonctionnalités introduites par Discord et bénéficie d'une maintenance active.


## Contribuer au projet

### 1. Créer le Bot sur Discord

1. Allez sur le [Discord Developer Portal](https://discord.com/developers/applications) et connectez-vous.
2. Cliquez sur **New Application** et nommez votre bot.
3. Dans l'onglet **Bot**, cliquez sur **Add Bot**.
4. Copiez le **TOKEN** du bot et garder le pour l'étape suivante.
5. Dans l'onglet **OAuth2**, allez dans **URL Generator** :
    - Cochez `bot` sous **SCOPES**.
    - Cochez les permissions que vous voulez sous **BOT PERMISSIONS**.
    - Copiez l'URL générée et invitez le bot sur votre serveur.


### 2. Forker et cloner le projet

**Forkez le dépôt** [CNAM-CSS-DISCORD-BOT](https://github.com/CNAM-CSS/CNAM-CSS-DISCORD-BOT) sur GitHub pour obtenir votre propre copie du projet.
voici la commande git pour cloner le repository sur votre ordinateur. exécute la dans ton terminal . Remplace "ton_compte" par ton compte . 
```
git clone https://github.com/ton_compte/CNAM-CSS-DISCORD-BOT.git
```
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
### 6. Exécuter le bot
Une fois l'installation terminée et les configurations effectuées, vous pouvez lancer le bot avec la commande suivante :

```bash
python main.py
```
### 7. Faire des modifications

1. **Créer une branche pour vos modifications**

   Créez une nouvelle branche pour travailler sur vos modifications :

   ```
   git checkout -b nom-de-votre-branche
   ```

2. **Faire vos modifications et tester le bot**

   Faites vos modifications et testez le bot localement pour vous assurer qu'il fonctionne correctement. **ATTENTION suivez bien les conventions de codage. ```docs/Convention.md```**

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

   Créez une **Pull Request** sur le dépôt principal pour proposer vos modifications. Ajoutez une description claire des changements que vous avez apportés.sous peine de vous voir refuser votre Pull request.

---
## Fonctionnalités nécessitant des étapes supplémentaires
### Météo
Pour pouvoir utiliser /meteo, il faut ajouter la clé d'API de votre compte [openweathermap](https://openweathermap.org/)
dans votre .env de la manière suivante:
'''
METEO_API = VOTRE_CLE_API
'''
Contactez [MARTENNE Anatole](https://github.com/AnatMarX) si vous voulez utiliser une clé associée au compte du discord.

## Aide
### Problèmes fréquents
- Si vous rencontrez un problème de TOKEN pour votre application, rendez-vous sur le [Discord Developer Portal](https://discord.com/developers/applications).
Dans l'onglet 'Bot', choisissez 'Reset Token', puis copiez votre nouveau TOKEN dans votre fichier .env.

- Si vous rencontrez des problèmes ou avez des questions, rendez-vous sur le [Discord du cnam](https://discord.gg/spMXekm9bq)🙏

## Contributeurs
[KANTZER jules](https://github.com/diezeJhon) ,[Abdellah Dighab](https://github.com/adwge99), [MARTENNE Anatole](https://github.com/AnatMarX)
