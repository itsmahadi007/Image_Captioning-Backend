from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from image_captioning.models import Images
from image_captioning.serializers import ImagesSerializerDetails


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
