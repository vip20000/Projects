
from django.shortcuts import render, redirect
from .models import User
from django.conf import settings
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
# Load the new model
model_path = os.path.join(settings.BASE_DIR, 'D:/RealEye/RealEyeUI/realeye/Models/v2/realeyev2.h5')
model = load_model(model_path)
def login(request):
    if request.method == 'POST':
        # Retrieve data from POST request
        username = request.POST.get('username')
        email = request.POST.get('email')
        
        # Save user data to database
        user = User.objects.create(username=username, email=email)
        
        # Redirect to upload page
        return redirect('upload')
    
    # Render login template for GET request
    return render(request, 'login.html')
def upload(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        image_path = os.path.join(settings.MEDIA_ROOT, 'D:/Github Programs/Projects/RealEye/RealEyeUI/realeye/Uploads', image_file.name)
        
        # Save the uploaded image to a temporary directory
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        # Preprocess the image
        img = image.load_img(image_path, target_size=(128, 128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0 # Normalize the image
        
        # Make predictions using the model
        predictions = model.predict(img_array)
        
        # Delete the temporary image file
        os.remove(image_path)
        
        # Store predictions in session
        request.session['predictions'] = predictions.tolist()
        
        # Redirect to result page
        return redirect('result')
    
    # Render upload template for GET request
    return render(request, 'upload.html')
def result(request):
    # Retrieve predictions from session
    predictions = request.session.get('predictions', [])
    print("Predictions from session:", predictions)
    
    # Flatten the list of lists into a single list of floats
    flat_predictions = [item for sublist in predictions for item in sublist]
    print("Flattened predictions:", flat_predictions)
    
    # Determine result based on predictions
    result = "AI-generated" if any(pred >= 0.5 for pred in flat_predictions) else "Real"
    
    # Render results template with result and predictions
    return render(request, 'result.html', {'result': result, 'predictions': flat_predictions})
