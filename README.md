# RoadDamageAI

Détection automatique de dommages routiers avec un modèle YOLOv8n entraîné sur
RDD2022.

## État du projet

Ce modèle n'est **pas la version finale**. Ce n'est pas non plus le premier
modèle entraîné : les premiers essais utilisaient des datasets plus petits et
moins de classes (par exemple les nids-de-poule uniquement). Il s'agit du modèle
**le plus abouti à ce jour**, avec le plus grand nombre de classes et un dataset
beaucoup plus volumineux (RDD2022). Il sera amélioré par la suite et intégré
dans une application Flutter.

## Classes détectées

- fissure longitudinale
- fissure transversale
- fissure en faïençage (alligator)
- autre dommage
- nid-de-poule

## Dataset

RDD2022 : _A multi-national image dataset for automatic Road Damage Detection_
(https://arxiv.org/abs/2209.08538). Le dataset n'est pas inclus dans ce dépôt en
raison de sa taille.

## Tester le modèle

```powershell
pip install ultralytics
python test.py
```

Le script charge `models/best.pt` et analyse les images placées dans
`exemples/`. Les résultats annotés sont enregistrés par Ultralytics dans
`runs/detect/predict/`.

## Résultats

Les courbes d'entraînement et la matrice de confusion sont disponibles dans
`results/`.
