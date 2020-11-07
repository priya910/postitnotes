from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    author = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.title


