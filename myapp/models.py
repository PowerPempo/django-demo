from django.db import models

# Create your models here.
class email(models.Model):
    email = models.EmailField(unique=True)


    def __str__(self):
        return self.email
    



class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name
