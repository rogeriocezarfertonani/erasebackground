from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
import uuid


def upload_image_formater(instance, filename):
    return f"{str(uuid.uuid4())}-backgroundremoved{filename}"


class EraseBackgroundModel(models.Model):
    image = models.ImageField(
        upload_to= upload_image_formater, blank=True, null=True)

    # class Meta:
    #     verbose_name = 'ImageUploadModel'
    #     verbose_name_plural = 'ImageUploadModels'
