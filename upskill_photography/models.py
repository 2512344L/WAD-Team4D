from django.contrib.auth.models import User
from django.db import models
import uuid
from django.urls import reverse

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return f'{self.user.username} UserProfile'
        

class Picture(models.Model):
    uploading_user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    picture_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="user_uploads/")
    thumbnail = models.ImageField(upload_to="thumbnails/")
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True, default=None)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    
    def __str__(self):

        return str(self.user.username) + " - " + str(self.title)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

        return str(self.uploading_user.user.username) + " - " + str(self.title)

        
        
class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ForeignKey('Picture', on_delete=models.CASCADE)
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    
    def __str__(self):
        return str(self.id) + " - " + str(self.text)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return str(self.name)
