import cv2
import pytesseract
import os
from difflib import SequenceMatcher
from PIL import Image
import re
import streamlit as st
import numpy as np

# Set the Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply adaptive thresholding
def thresholding(image):
    return cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

# Preprocessing the image to improve the OCR accuracy
def preprocessing(image):
    gray = get_grayscale(image)
    return thresholding(gray)

# apply regular expressions to get the words making up the ingredients
def cleaning(text):
    text = re.sub('[*|\n|\|(|)|.]', ' ', text)
    text = re.sub('[}|{|\|/|,|:]', ' ', text)
    text = re.sub(' +', ' ', text)
    ingredients = text.split()
    return ingredients

def main():
    st.set_page_config(page_title="Ingredient Safety for a diabetic", layout="centered")
    st.title("Ingredient Safety for a diabetic")
    st.write("Upload an image and check if it contains unsafe ingredients.")

    uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        preprocessed_image = preprocessing(img)
        cv2.imwrite("new.png", preprocessed_image)
        text = pytesseract.image_to_string(Image.open(os.path.abspath('new.png')))
        ingredients = cleaning(text)
        ingredients = [x.lower() for x in ingredients]

        sugars = ['sugar', 'glucose', 'fructose', 'dextrose', 'sucrose', 'syrup', 'hydrogenated', 'lard', 'molasses', 'maltose', 'lactose', 'honey']

        weary_ingredients = 0

        for i in range(len(sugars)):
            for j in range(len(ingredients)):
                if SequenceMatcher(None, sugars[i], ingredients[j]).ratio() >= 0.7:
                    weary_ingredients += 1

        st.image(image, caption='Uploaded Image', use_column_width=True)

        if weary_ingredients > 0:
            st.error("This product contains unsafe ingredients for you.")
        else:
            st.success("This product is safe for you.")

if __name__ == '__main__':
    main()
