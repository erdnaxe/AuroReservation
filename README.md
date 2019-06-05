# Booking Project

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Build Status](https://api.travis-ci.com/erdnaxe/AuroReservation.svg?branch=master)](https://travis-ci.com/erdnaxe/AuroReservation)
[![Coverage Status](https://coveralls.io/repos/github/erdnaxe/AuroReservation/badge.svg?branch=master)](https://coveralls.io/github/erdnaxe/AuroReservation?branch=master)

<img align="right" width="70" height="70" src="static/favicon/mstile-70x70.png">
Booking Project est un outil permettant de réserver des salles.
Il a été développé pour pouvoir être utilisé pour réserver des salles plus simplement
entre les élèves et des administrations.

## Mettre en place un environnement de développement

Le projet utilise Pipenv qui permet de très simplement mettre en place un environnement pour développer.
Vous aurez ainsi exactement les mêmes modules Python que les autres développeurs.
Ces versions correspondent au plus à celles dans Debian Buster.

Pour mettre cet environnement en place, vérifiez que vous avez Pipenv sur votre machine, puis dans le dossier du projet :

Pour la compilation du frontend, vous pouvez utiliser `yarn` ou `npm`.
`yarn` est légèrement plus récent et rapide que `npm` mais pas toujours disponible dans les dépôts.

```bash
yarn install  # Installation des dépendances du frontend (ou avec npm)
pipenv install  # Installation d'un virtualenv
pipenv shell  # Rentre dans le virtualenv
./manage.py migrate  # Exécute les migrations de la base de données
./manage.py compilemessages  # Compile les traductions
./manage.py createsuperuser  # Crée un super-utilisateur
yarn run build  # Build frontend
./manage.py runserver  # Lancer un serveur de développement
```

Pensez à vérifier la timezone dans `settings.py` (par exemple `Europe/Paris`) et à changer les secrets.

Vous pouvez activer `django_extensions` dans les `INSTALLED_APPS` pour avoir accès à une commande permettant
de tracer le graphe des dépendances des modèles. 

## Guide du petit contributeur

Lorsque vous voulez proposer une fonctionnalité vous pouvez ouvrir un rapport en bug.
Ensuite si vous voulez aider à mettre plus rapidement cette fonctionnalité dans le code vous pouvez ouvrir une requête de fusion en proposant votre code sur une autre branche. Ainsi nous pourrons le tester et discuter dessus.

Les règles de contributions :

  * **Le code est écrit et commenté en anglais** seulement afin de fournir une documentation auto-générée homogène.
  * Chaque application doit être pensées le plus possible **DRY** (don't repeat yourself) et **KISS** (keep it simple stupid).
    Exemple : l'application `users` reprend le code de Django et ajoute juste un profil utilisateur.
  * **Garder les applications indépendantes.**
    On doit pouvoir désactiver une app sans pour autant devoir modifier majoritairement le code.

Je vous conseille de vous référez au guide de contribution de Django.

## Contribuer à la traduction

Ce projet utilise POEditor comme plateforme de traduction collaborative.
Vous pouvez rejoindre l'équipe de traduction en suivant ce lien :
<https://poeditor.com/join/project/A5nqT2DDsz>

## Installation sous Debian Buster

Les dépendances du projet ont été choisis pour être disponibles dans Debian
Buster.

Les paquets nécessaires sont :

  * [python3-django](https://packages.debian.org/experimental/all/python3-django/download) (prendre pour le moment la version de `experimental`)
  * python3-djangorestframework
  * python3-django-reversion
  * python3-django-webpack-loader
  * python3-docutils
  * yarn (vous pouvez le remplacer par npm qui est avec nodejs)
  * nodejs
  * gettext

## Crédits

 - [pa](https://gitlab.crans.org/pa) (structure du projet, traduction anglaise et motivation) ;
 - [lieunoir](https://gitlab.crans.org/lieunoir) (formulaires et motivation) ;
 - [erdnaxe](https://gitlab.crans.org/erdnaxe) (interface utilisateur) ;
 - [elkmaennchen](https://gitlab.crans.org/elkmaennchen) (traduction espagnole).

## Licence

Ce projet est sous [licence GPL](LICENSE) parce que l'on croît au développement ouvert.
La licence GPL implique des droits et des devoirs.
Veuillez vous référer au fichier de licence pour plus d'informations.
