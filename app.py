import streamlit as st

# Titre de l'application
st.title("Prédiction du nom de la fleur")

# Instructions
st.write("Entrez les dimensions de la fleur pour prédire son nom.")

# Entrées de l'utilisateur pour les dimensions de la fleur
sepal_length = st.number_input("Longueur du sépale (en cm)", min_value=0.0, step=0.1)
sepal_width = st.number_input("Largeur du sépale (en cm)", min_value=0.0, step=0.1)
petal_length = st.number_input("Longueur du pétale (en cm)", min_value=0.0, step=0.1)
petal_width = st.number_input("Largeur du pétale (en cm)", min_value=0.0, step=0.1)

# Choisir un modèle pour prédire le nom de la fleur (exemple avec un modèle pré-entrainé comme un modèle de classification)
# Ici nous utiliserons un modèle fictif, mais en vrai on chargerait un modèle de machine learning (comme un modèle pré-entrainé scikit-learn)
import numpy as np

# Exemple de données d'entraînement (fleurs de l'iris)
# Nom des fleurs
flowers = ["Setosa", "Versicolor", "Virginica"]

# Ici, nous supposons que les entrées correspondent aux caractéristiques de l'iris et nous retournons un nom de fleur basé sur des valeurs de seuil fictives.
def predict_flower(sepal_length, sepal_width, petal_length, petal_width):
    # Logique de prédiction fictive basée sur les seuils
    if sepal_length < 5 and petal_length < 2:
        return "Setosa"
    elif sepal_length < 6.5 and petal_length < 4.5:
        return "Versicolor"
    else:
        return "Virginica"

# Prédire le nom de la fleur
if st.button("Prédire le nom de la fleur"):
    flower_name = predict_flower(sepal_length, sepal_width, petal_length, petal_width)
    st.write(f"Le nom de la fleur est probablement : {flower_name}")

