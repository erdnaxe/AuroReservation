# Booking Project

## Mettre en place un environnement de développement

Le projet utilise Pipenv qui permet de très simplement mettre en place un environnement pour développer.
Vous aurez ainsi exactement les mêmes modules Python que les autres développeurs.

Pour mettre cet environnement en place, vérifiez que vous avez Pipenv sur votre machine, puis dans le dossier du projet :

```bash
pipenv install  # Installation d'un virtualenv
pipenv shell  # Rentre dans le virtualenv
./manage.py migrate  # Exécute les migrations de la base de données
./manage.py compilemessages  # Compile les traductions
./manage.py createsuperuser  # Crée un super-utilisateur
./manage.py runserver  # Lancer un serveur de développement
```

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