from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from image_captioning.models import Images
from image_captioning.serializers import ImagesSerializerDetails


# Create your views here.

@api_view(["GET"])
def test_function_view(request):
    return Response("Hello World", status=status.HTTP_200_OK)


@api_view(["POST"])
def post_images_function_view(request):
    image = request.FILES["image"]
    image = Images.objects.create(image=image)
    serializer = ImagesSerializerDetails(image, context={"request": request}).data
    return Response(serializer, status=status.HTTP_200_OK)
