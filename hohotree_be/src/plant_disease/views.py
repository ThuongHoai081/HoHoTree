from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
import tensorflow as tf
import numpy as np
from scipy.stats import entropy
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', '1.keras')
model = tf.keras.models.load_model(MODEL_PATH)

def is_leaf_like(image_array):
    red = image_array[:, :, 0]
    green = image_array[:, :, 1]
    blue = image_array[:, :, 2]
    green_mask = (green > 100) & (green > red) & (green > blue)

    yellow_mask = (red > 100) & (green > 100) & (blue < 100)

    valid_pixels = np.sum(green_mask | yellow_mask)
    total_pixels = image_array.shape[0] * image_array.shape[1]
    valid_ratio = valid_pixels / total_pixels

    return valid_ratio > 0.2


@csrf_exempt
def predict_image(request):
    if request.method == 'POST' and request.FILES.get('file'):
        image_file = request.FILES['file']
    
        try:
            image = Image.open(image_file).convert('RGB').resize((256, 256))
            image_np = np.array(image).astype(np.float32)

            if not is_leaf_like(image_np):
                return JsonResponse({
                    'disease': 'Unknown',
                    'reason': 'Image does not appear to be a leaf'
                })

            image_input = np.expand_dims(image_np, axis=0)

            prediction = model.predict(image_input)
            probs = prediction[0]
            predicted_class = int(np.argmax(probs))
            confidence = float(np.max(probs))
            ent = float(entropy(probs, base=2))

            if ent > 1.2:
                return JsonResponse({
                    'disease': 'Unknown',
                    'confidence': round(confidence, 4),
                    'entropy': round(ent, 4),
                    'reason': 'Uncertain prediction'
                })

            disease_labels = {
                0: "Early Blight",
                1: "Late Blight",
                2: "Healthy",
            }
            disease_name = disease_labels.get(predicted_class, "Unknown")

            print(f"Prediction: {prediction}")
            print(f"Class: {predicted_class} -> {disease_name}, Confidence: {confidence:.4f}, Entropy: {ent:.4f}")

            return JsonResponse({
                'disease': disease_name,
                'confidence': round(confidence, 4),
                'entropy': round(ent, 4)
            })

        except Exception as e:
            return JsonResponse({'error': f'Processing failed: {str(e)}'}, status=500)

    return JsonResponse({'error': 'No image uploaded'}, status=400)
