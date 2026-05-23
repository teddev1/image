from django.db import models

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.image.name


from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
