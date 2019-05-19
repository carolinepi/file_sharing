from django.conf import settings
from django.db import models
from django.utils import timezone


class UploadModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', blank=False, null=False)
    created_date = models.DateTimeField(default=timezone.now)
    ended_date = models.DateTimeField()
    is_worked = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
