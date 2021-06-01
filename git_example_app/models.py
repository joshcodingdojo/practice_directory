from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=45)
  last_name = models.CharField(max_length=45)
  age = models.IntegerField()

class Post(models.Model):
  text = models.TextField()
  user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)