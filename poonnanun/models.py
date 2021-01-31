from django.db import models

class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()

