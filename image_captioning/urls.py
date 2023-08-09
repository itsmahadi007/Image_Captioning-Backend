from django.urls import path

from image_captioning.views.basic_images_caption_views import BasicImageCaptioning
from image_captioning.views.views import test_function_view, post_images_function_view

urlpatterns = [
    path('', test_function_view),
    path('post_image/', post_images_function_view),
    path('basic_image_captioning/', BasicImageCaptioning.as_view()),
]
