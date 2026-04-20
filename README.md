# RL Eagle-1 — Pilote automatique d’atterrissage lunaire

## Contexte

Ce projet consiste à développer un système autonome capable de piloter un module lunaire simulé ("Eagle-1") afin de réussir un atterrissage en douceur.

L’objectif est de concevoir un agent intelligent capable de prendre des décisions en temps réel pour contrôler la trajectoire, la vitesse et l’orientation du module tout en optimisant la stabilité et la consommation de carburant.

Ce travail s’inscrit dans un cadre d’apprentissage du Reinforcement Learning (RL).

---

## Objectif

Développer un agent capable de :

* analyser l’état du module (position, vitesse, orientation)
* choisir les actions appropriées (propulseurs)
* maximiser une récompense cumulative
* réussir un atterrissage contrôlé sur la zone cible

---

## Méthodologie

### 1. Baseline avec DQN

* Algorithme : DQN (Deep Q-Network)
* Paramètres par défaut
* Objectif : établir une référence

**Résultats :**

* Reward moyenne : **-147**
* Écart-type : **± 53**

Conclusion : performances insuffisantes, l’agent ne maîtrise pas l’atterrissage.

---

### 2. Optimisation avec PPO

* Algorithme : PPO (Proximal Policy Optimization)
* Ajustement des hyperparamètres
* Analyse via TensorBoard
* Entraînement : **1 000 000 timesteps**

---

## Résultats finaux

* Reward moyenne : **263**
* Écart-type : **± 45**
* Évaluation sur **100 épisodes**

L’objectif (> 200) est atteint.
L’agent réalise des atterrissages stables et contrôlés.

---

## Démonstration visuelle (Étape 3)

L’agent peut être visualisé en train de jouer une partie complète grâce à une vidéo générée automatiquement.

### Lancer la démonstration

1. Démarrer l’API :

```bash
uvicorn api:app --reload
```

2. Lancer l’interface :

```bash
streamlit run app.py
```

3. Dans l’interface Streamlit :

* Aller dans "Visualisation"
* Cliquer sur "Générer la vidéo"

Une vidéo de l’atterrissage est affichée.

---

## Génération de la vidéo

```bash
python record.py
```

Les vidéos sont enregistrées dans :

```
/videos/
```

---

## Dashboard

Disponible dans l’interface Streamlit :

* Reward moyen
* Reward max / min
* Écart-type (stabilité)
* Distribution des performances

---

## API

Lancer l’API :

```bash
uvicorn api:app --reload
```

Documentation :

http://127.0.0.1:8000/docs

### Endpoints :

* `/play` : simulation simple
* `/play_video` : génération de vidéo
* `/metrics` : statistiques
* `/health` : état de l’API

---

## Interface graphique

```bash
streamlit run app.py
```

Fonctionnalités :

* Simulation de l’agent
* Visualisation vidéo
* Dashboard de performance

---

## Entraînement

```bash
python train.py
```

---

## Évaluation

```bash
python evaluate.py
```

---

## TensorBoard

```bash
tensorboard --logdir=logs
```

Puis ouvrir :

http://localhost:6006

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Structure du projet

```
rl-eagle1/
│
├── train.py
├── evaluate.py
├── record.py
├── api.py
├── app.py
├── requirements.txt
├── README.md
├── eagle1_step1.ipynb
├── model/
└── logs/
```

---

## Résumé

* Agent RL entraîné (PPO)
* Performance > 200
* API fonctionnelle
* Interface graphique
* Visualisation réelle
* Dashboard

---

## Auteur

Projet réalisé par Selma dans le cadre d’une formation en Intelligence Artificielle.
