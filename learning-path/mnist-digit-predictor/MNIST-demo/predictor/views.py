from django.shortcuts import render, HttpResponse
import tensorflow
import os
from tensorflow.keras.models import load_model

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'predictor', 'models', 'model.h5')
model = load_model(model_path)


def prediction_page(request):

        return render(request, 'prediction_page.html')



def make_prediction(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        
        if not image:
            return HttpResponse("No image uploaded", status=400)

        from PIL import Image
        import numpy as np

        img = Image.open(image)
        img = img.resize((28, 28))
        img = img.convert('L')              
        img_array = np.array(img)
        img_array = img_array / 255.0
        processed_image = img_array.reshape(1, 28, 28, 1)

        prediction = model.predict(processed_image)
        predicted_digit = int(np.argmax(prediction))

        return render(request, 'prediction_page.html', {'prediction': predicted_digit})

    # GET request — just show the form, no prediction yet
    return render(request, 'prediction_page.html')
