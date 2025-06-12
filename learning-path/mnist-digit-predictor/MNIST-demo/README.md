# 🧠 MNIST Digit Predictor

A simple web-based digit recognition tool built using **TensorFlow** and **Django**.  
This is a learning project to understand how deep learning models can be served using web frameworks.

---

## 🛠️ Technologies Used

- **Python**
- **Django**
- **TensorFlow / Keras**
- **Bootstrap 4** (for basic styling)
- **Pillow** (for image processing)
- **NumPy**

---

## 🎯 Project Description

This project allows users to:

- Upload an image of a **handwritten digit** (0-9)
- The backend pre-trained model (trained on the MNIST dataset) predicts the digit
- The result is displayed on the web page after submission

---

## 🖼️ How It Works

1. User uploads a `.png` or `.jpg` image of a digit.
2. The image is:
   - Converted to grayscale
   - Resized to 28x28 pixels
   - Normalized and reshaped for model input
3. TensorFlow model returns the predicted digit.
4. The prediction is displayed on the web page.

---


