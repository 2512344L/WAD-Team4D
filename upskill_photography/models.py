from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
        

class Picture(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(UserProfile)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='user_uploads/%d' % user.username)
    thumbnail = models.ImageField(upload_to='thumbnails/%d' % user.username)
    category = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return str(user.username) + " - " + str(self.title)
        
        
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ForeignKey(Picture)
    user = models.ForeignKey(UserProfile)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()