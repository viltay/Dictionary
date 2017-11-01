from django.db import models

# Create your models here.
class Dictionary(models.Model):
    original_word = models.CharField(max_length=30)
    translate_word = models.CharField(max_length=30)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.original_word