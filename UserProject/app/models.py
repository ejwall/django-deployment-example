from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    # Create relationship with User class
    # inheriting the User class can cause database problems
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    portfolio = models.URLField(blank=True) # doesn't have to be filled out
    picture = models.ImageField(upload_to='profile_pics',blank=True) # automatically goes under MEDIA_ROOT

    def __str__(self):
        return self.user.username
