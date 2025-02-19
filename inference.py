import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
import os

# Load the trained model
model = load_model('effB3_CNN_DR_classifier.h5')

# Define function for image preprocessing and prediction
def predict_image(img_path):
    try:
        # Check if the image file exists before processing
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Image file {img_path} not found")

        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        # Make prediction
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        return predicted_class

    except Exception as e:
        raise RuntimeError(f"Error during prediction: {str(e)}")
