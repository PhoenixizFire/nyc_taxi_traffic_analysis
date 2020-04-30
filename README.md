# Analyse du traffic des taxis à NYC
*Simplonline homework (litterally from home)*

Dans un premier temps, il s'agit de calculer des indicateurs à partir d'une base de données sous format csv et de les représenter graphiquement. Dans un second temps, il est demandé de construire un algorithme de machine learning pour prédire la durée des trajets de taxis.

## Livrables

A minima:

- 2 notebooks (1 sur la description et 1 sur la 
prédiction)

Dans le meilleur des cas, un repo github avec:

- 1 script python permettant de calculer les indicateurs
- 1 notebook avec les analyses graphiques
- 1 notebook avec la pipeline de Machine Learning
- 2-3 tests unitaires (bonus)

## Contexte du projet
### Partie descriptive:
On cherche à étudier les caractéristiques des trajets des taxis new yorkais. Pour cela, nous allons calculer 4 indicateurs :

- la vitesse moyenne de chaque trajet (en km/h)
- le nombre de trajets effectués en fonction du jour de la semaine
- le nombre de trajets effectués en fonction de l’horaire de la journée par tranche de 4h.
- le nombre de km parcourus par jour de la semaine

De plus, chaque indicateur sera illustré par un graphique.

### Partie prédictive:
Enfin, vous mettrez en place un ou plusieurs modèles de régressions afin de prédire la durée des trajets en découpant la base en train / test (70% / 30%).

## Modalités pédagogiques
Travail en groupes (par deux, trois ou quatres).
Vous pouvez travailler via google colab.

## Critères de performance
- Les indicateurs doivent être calculés avec les bonnes unités.
- Les graphiques doivent être commentés
- Le choix des variables explicatives pour le modèle de regression doit être justifié
- La pipeline de ML doit permettre de détecter un éventuel overfitting

## Modalités d'évaluation
- Concision du code
- Clarté des explications