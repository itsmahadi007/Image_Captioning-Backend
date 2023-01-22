import numpy as np
from django.db import models
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D


# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name


class ImageCaptioningModel(models.Model):
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        # Load the InceptionV3 model with pre-trained weights
        base_model = InceptionV3(weights='imagenet', include_top=False)

        # Add a global spatial average pooling layer
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        # Add a fully-connected layer
        x = Dense(1024, activation='relu')(x)
        # Add a logistic layer
        predictions = Dense(200, activation='softmax')(x)

        # This is the model we will train
        model = Model(inputs=base_model.input, outputs=predictions)

        # Freeze the layers of the base_model (We don't want to train these again)
        for layer in base_model.layers:
            layer.trainable = False

        # Compile the model
        model.compile(optimizer='adam', loss='categorical_crossentropy')

        return model

    def train_model(self, X_train, Y_train):
        self.model.fit(X_train, Y_train, epochs=10, batch_size=32)

    def predict_caption(self, image):
        # Preprocess the image
        img = image.img_to_array(image)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)

        # Generate caption
        caption = self.model.predict(img)

        return caption