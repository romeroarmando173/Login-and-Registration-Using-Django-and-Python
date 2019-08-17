from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length = 60)
    password = models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now= True)
    #quotesUploaded 
    #PosterBoy
class Quote(models.Model):
    author = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    userQuote = models.ForeignKey(User, related_name="UserQuote")
    # uploadedBy = models.ForeignKey(User,related_name="quotesUploaded")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

