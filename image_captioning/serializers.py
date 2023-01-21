from rest_framework import serializers

from image_captioning.models import Images


class ImagesSerializerDetails(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['created_at'] = instance.created_at.strftime("%B %d, %Y")
        representation['updated_at'] = instance.updated_at.strftime("%B %d, %Y")

        if len(instance.image.name) != 0:
            x = instance.image.name.split("/")
            type = x[-1].split(".")
            image = {
                "url": representation.pop("image"),
                "size": instance.image.size,
                "name": x[-1],
                "type": type[-1],
            }
            representation["image"] = image

        return representation
