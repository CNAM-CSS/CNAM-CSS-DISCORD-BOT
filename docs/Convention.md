# Convention de Nommage

## Sommaire
- [1. Nommage des fichiers](#1-nommage-des-fichiers)
- [2. Nommage des variables](#2-nommage-des-variables)
- [3. Nommage des constantes](#3-nommage-des-constantes)
- [4. Nommage des fonctions](#4-nommage-des-fonctions)
- [5. Nommage des classes](#5-nommage-des-classes)
- [6. Nommage des méthodes privées](#6-nommage-des-méthodes-privées)
- [7. Nommage des branches Git](#7-nommage-des-branches-git)
- [8. Nommage des tests](#8-nommage-des-tests)
- [Règles générales](#règles-générales)

---

## 1. Nommage des fichiers
- Utiliser le **snake case** (minuscules avec des underscores entre les mots).
- Exemples :
  - `utilitaire_math.py`
  - `gestion_utilisateur.py`
- Les fichiers contenant des classes doivent être nommés en fonction de la principale classe, en **snake case**.

## 2. Nommage des variables
- Utiliser le **snake case** pour les variables.
- Les noms doivent être explicites et décrire clairement leur rôle.
- Exemples :
  - `nombre_utilisateurs`
  - `valeur_maximale`

## 3. Nommage des constantes
- Utiliser des **lettres majuscules** avec des underscores pour séparer les mots.
- Les constantes sont placées au début du fichier ou dans un fichier dédié.
- Exemples :
  - `TEMPERATURE_MAX`
  - `API_BASE_URL`

## 4. Nommage des fonctions
- Utiliser le **snake case**.
- Le nom doit indiquer clairement ce que fait la fonction.
- Exemples :
  - `calculer_moyenne()`
  - `envoyer_email()`

## 5. Nommage des classes
- Utiliser le **Pascal case** (Camel case avec la première lettre de chaque mot en majuscule).
- Le nom doit être un nom, représentant un objet ou un concept.
- Exemples :
  - `Utilisateur`
  - `GestionnaireDeSession`

## 6. Nommage des méthodes privées
- Utiliser le **snake case** précédé d’un underscore (`_`) pour indiquer qu’il s’agit d’une méthode privée.
- Exemples :
  - `_valider_entree()`
  - `_mettre_a_jour_etat()`

## 7. Nommage des branches Git
- Utiliser des conventions claires et lisibles pour le travail collaboratif.
- Exemples :
  - Pour une fonctionnalité : `feature/nom_fonctionnalite`
  - Pour une correction de bug : `fix/description_bug`
  - Pour une tâche spécifique : `task/nom_tache`

## 8. Nommage des tests
- Utiliser le **snake case** et nommer les tests en fonction de la fonctionnalité testée, avec un préfixe `test_`.
- Exemples :
  - `test_calcul_moyenne()`
  - `test_creation_utilisateur()`

---

## Règles générales
- **Longueur des noms** : Les noms doivent être aussi descriptifs que nécessaire, mais éviter d’être trop longs.
- **Abbréviations** : Éviter les abréviations non évidentes ; privilégier des noms clairs.

