from django.db import models

# Create your models here.
class TranslationModel(models.Model):
    model_name = models.CharField(max_length=255)
    model_url = models.CharField(max_length=255, blank=True, default='')
    source_lang = models.CharField(max_length=255)
    destination_lang = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, default='')
    score = models.FloatField(default=0)

    def __str__(self):
        return self.model_name