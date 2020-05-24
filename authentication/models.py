from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Utilisateur(AbstractUser):
    '''
    Model d'Utilisateur pour l'authentication
    '''
    USER_TYPE_CHOICES = (
        (0, 'Admin'),
        (1, 'Locataire'),
        (2, 'Gestionnaire'),
    )
    profile_image = models.ImageField(upload_to='utilisateur_img/', default='utilisateur.png')
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=0)

    def __str__(self):
        return self.username
