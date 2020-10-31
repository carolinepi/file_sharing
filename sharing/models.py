from django.conf import settings
from django.db import models
from datetime import date


class UploadModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='aaaa')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', blank=False, null=False)
    created_date = models.DateField(default=date.today())
    ended_date = models.DateField()
    is_worked = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        self.file.delete()

    def __str__(self):
        return self.title
