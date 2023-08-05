import re

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class CustomUser(AbstractUser):
    # Add any additional fields you need for your user model here
    # For example:
    # bio = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    completed_profile = models.BooleanField(default=False)

    # team =

    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    def has_team(self, competition):
        return self.teams_joined.filter(competition=competition).exists()

    def __str__(self):
        return self.first_name


def validate_phone_number(value):
    pattern = re.compile(r'^09\d{9}$')  # Regular expression for the format 09xxxxxxxxx
    if not pattern.match(value):
        raise ValidationError('Please enter a valid phone number in the format 09xxxxxxxxx.')


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default_profile.jpg',
                                blank=True, null=True)
    phone_number = models.CharField(max_length=12, validators=[validate_phone_number])

    # Add more fields as needed

    def __str__(self):
        return self.user.username
