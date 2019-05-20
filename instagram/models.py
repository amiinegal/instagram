from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    bio = models.TextField(max_length = 30, blank = True)
    profile_pic = models.ImageField(upload_to = 'images/', null =True, blank = True)
    followers = models.ManyToManyField('Profile', related_name = 'followers_profile', blank =True)
    following = models.ManyToManyField('Profile', related_name='following_profile', blank =True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    comment = models.TextField(max_length = 30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Image(models.Model):
    image_path = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    caption = models.TextField(blank = True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.ForeignKey(Likes)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.name

Comment.image = models.ForeignKey(Image)
Likes.image = models.ForeignKey(Image)

class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()