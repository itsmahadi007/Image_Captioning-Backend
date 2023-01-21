from django.urls import path, include

from image_captioning.views import post_images_function_view, test_function_view

urlpatterns = [
    path('', test_function_view),
    path('post_image/', post_images_function_view),
]
