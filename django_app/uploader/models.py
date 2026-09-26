from django.db import models


def upload_to(instance, filename):
    return f"uploads/{filename}"


class UploadedFile(models.Model):
    file = models.FileField(upload_to=upload_to)
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.file.name
