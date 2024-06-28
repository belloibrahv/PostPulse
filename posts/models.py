from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_new_add=True)
    poster = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']