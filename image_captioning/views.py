from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from image_captioning.models import Images, ImageCaptioningModel
from image_captioning.serializers import ImagesSerializerDetails

from tensorflow.keras.preprocessing.image import img_to_array, load_img
import numpy as np


# Create your views here.

@api_view(["GET"])
def test_function_view(request):
    return Response("Hello World", status=status.HTTP_200_OK)


@api_view(["POST"])
def post_images_function_view(request):
    try:
        image = request.FILES["image"]
        image = Images.objects.create(image=image)
        serializer = ImagesSerializerDetails(image, context={"request": request}).data
        return Response(serializer, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ImageCaptioning(APIView):
    @staticmethod
    def post(request):
        image = request.FILES.get('image')
        model = ImageCaptioningModel()
        image = load_img(image, target_size=(299, 299))
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        caption = model.predict_caption(image)
        return Response(caption, status=status.HTTP_200_OK)
