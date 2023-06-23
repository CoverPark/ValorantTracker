# Valorant Tracker

Description du projet.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

- Python (version 3.11)
- Docker (version 24.0) *(uniquement si vous utilisez Docker)*

## Installation

1.Clonez ce dépôt de code sur votre machine locale :

```shell
git clone https://github.com/CoverPark/ValorantTracker
```

2.Acceder au repertoire
```shell
cd ValorantTracker
```

3.Installez les dépendances :

```shell
pip install -r requirements.txt
```
4.Remplacer le token dans config.json par votre discord bot token,pour creer :https://discord.com/developers/docs/intro

5.Uniquement si vous utilisez Docker : Construisez l'image Docker :

```shell
docker build -t image_name:1.0.0 .
```

## Utilisation:

Si vous utilisez Docker:

```shell
docker run -d image_name:1.0.0
```

## Sinon:
```shell
py main.py
```





