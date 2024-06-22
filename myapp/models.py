from django.db import models

# Create your models here.

class email_model(models.Model):
    email_model_input = models.EmailField(max_length=150)
    
