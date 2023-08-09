import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Load the pre-trained model from the local directory
model_path = "./datasets/basics/inception_v3_model"
model = hub.KerasLayer(model_path)

# Load the ImageNet labels from the local file
with open("./datasets/basics/ImageNetLabels.txt", 'r') as f:
    labels = f.read().splitlines()


def preprocess_image(image):
    # Convert image to tensor
    image_tensor = tf.image.decode_image(image.read())

    # Resize the image to (299, 299) for Inception V3
    image_resized = tf.image.resize(image_tensor, [299, 299])

    # Normalize pixel values to [-1, 1]
    image_normalized = (image_resized - 127.5) / 127.5

    # Expand dimensions for batch size
    return tf.expand_dims(image_normalized, 0)


class BasicImageCaptioning(APIView):
    @staticmethod
    def post(request):
        image = request.FILES.get('image')

        # Preprocess the image for the model
        processed_image = preprocess_image(image)

        # Get predictions
        predictions = model(processed_image)

        # Retrieve the top predicted class label
        class_label = np.argmax(predictions, axis=-1)[0]
        caption = labels[class_label]

        return Response({'caption': caption}, status=status.HTTP_200_OK)

    # Create your views here.
