from fastapi import FastAPI
from pydantic import BaseModel
import tensorflow as tf
import numpy as np

# Load the .h5 model
model = tf.keras.models.load_model("my_model.h5")

# FastAPI app
app = FastAPI()

# Request schema
class InputData(BaseModel):
    data: list[float]  # Example: [1.0, 0.0]

# Prediction endpoint
@app.post("/predict")
def predict(input: InputData):
    # Convert input to NumPy array
    input_array = np.array([input.data])
    prediction = model.predict(input_array)
    # Return as float
    return {"prediction": float(prediction[0][0])}

@app.get("/")
def read_root():
    return {"message": "TensorFlow FastAPI is running!"}

