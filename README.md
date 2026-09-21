https://medium.com/@sii-lille/data-science-one-hot-encoding-c59e82b3f0e7


L'encodage ordinal est une technique de prétraitement utilisée pour convertir des données catégorielles en valeurs numériques tout en préservant leur ordre intrinsèque. Il est utile pour les modèles d'apprentissage automatique, tels que les réseaux de neurones, qui attendent des variables d'entrée numériques. L'encodage ordinal présente deux avantages principaux :
Encodage des données catégorielles sous des formes numériques que les algorithmes peuvent comprendre.
Conserver l’information ordinale entre les catégories qui est perdue avec l’encodage one-hot .


L'encodage one-hot est une technique de prétraitement courante utilisée lors du traitement de données catégorielles en apprentissage automatique. Elle remplit deux fonctions principales :
A) Convertir les valeurs catégorielles en vecteurs numériques compréhensibles par des algorithmes tels que les réseaux de neurones et la régression. De nombreux modèles nécessitent des données d'entrée numériques.
B) Représenter les valeurs catégorielles de manière à préserver leur unicité. Sans encodage one-hot, les algorithmes risquent de traiter incorrectement différentes catégories comme une seule et même valeur.


Technique de prétraitement — Transformation des données brutes avant la modélisation afin d'améliorer les performances.

Données catégorielles — Données représentant des catégories ou des valeurs discrètes plutôt que des nombres.

Vecteurs numériques — Tableaux de nombres représentant des valeurs catégorielles pour la modélisation.

Réseaux neuronaux — Modèles qui apprennent des schémas complexes à partir de nœuds interconnectés en couches.

Régression — Modèles qui prédisent des résultats continus à partir des relations entre les caractéristiques.

caractéristiques — Variables d'entrée représentant les caractéristiques utilisées par les modèles d'apprentissage automatique pour effectuer des prédictions.

Dimensionnalité — Le nombre de caractéristiques ou de variables dans un ensemble de données.

train_test_split(): diviser les donnes en ensemble d'entrainnement et de test



Ensemble d'entraînement : L'ensemble d'entraînement est un ensemble de données utilisé pour entraîner le modèle. Il s'agit des données sur lesquelles le modèle est entraîné. Ces données sont observées et apprises par le modèle.


Ensemble de test : L’ensemble de données de test est un sous-ensemble de l’ensemble de données d’entraînement utilisé pour fournir une évaluation précise de l’adéquation du modèle final.


Ensemble de validation :   Un ensemble de données de validation est un échantillon de données provenant de l’ensemble d’entraînement de votre modèle, utilisé pour estimer les performances du modèle lors du réglage des hyperparamètres du modèle.