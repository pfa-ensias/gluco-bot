import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import io
import os
import numpy as np
from tensorflow.keras.models import load_model

# Charger le modèle de classification d'images
model_path = 'best_model_101class.hdf5'
model = load_model(model_path, compile=False)

class_N = {}
N_class = {}
with open('classes.txt', 'r') as txt:
    classes = [i.strip() for i in txt.readlines()]
    class_N = dict(zip(classes, range(len(classes))))
    N_class = dict(zip(range(len(classes)), classes))
    class_N = {i: j for j, i in N_class.items()}

# Charger les données nutritionnelles
nutrition_data = pd.read_csv('nutrition101.csv')

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (200, 200))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def predict(image_path):
    img = preprocess_image(image_path)
    predictions = model.predict(img)
    class_index = np.argmax(predictions)
    class_label = N_class[class_index]
    return class_label

def main():
    st.title("Food safety")

    # Ajouter un formulaire pour charger une image
    uploaded_file = st.file_uploader("Choose an image of a dish.", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        # Lire les données de l'image
        image_data = uploaded_file.read()
        image = Image.open(io.BytesIO(image_data))

        # Afficher l'image
        st.image(image, caption='Image du plat', use_column_width=True)

        # Enregistrer l'image temporairement
        temp_image_path = f"temp_image{uploaded_file.name}"
        with open(temp_image_path, "wb") as temp_image_file:
            temp_image_file.write(image_data)

        # Prédire la classe du plat
        predicted_class = predict(temp_image_path)
        st.write("Food name:", predicted_class)

        # Rechercher les informations nutritionnelles du plat
        nutrition_info = nutrition_data[nutrition_data['name'] == predicted_class]

        if not nutrition_info.empty:
            # Afficher les informations nutritionnelles
            st.subheader("Nutritional information")
            selected_columns = ['protein', 'calcium', 'fat', 'carbohydrates', 'vitamins', 'sugar']
            st.dataframe(nutrition_info[selected_columns], width=800)

            # Vérifier la compatibilité avec le diabète
            if nutrition_info['sugar'].values[0] > 10:
                st.error("Unsafe for someone with diabetes")
            else:
                st.success("Safe for someone with diabetes")
        else:
            st.error("Nutritional information not available for this class.")

        # Supprimer l'image temporaire
        os.remove(temp_image_path)

if __name__ == '__main__':
    main()
