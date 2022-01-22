from django.db import models

# Create your models here.
class Administrator(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=200)
    password=models.TextField(max_length=2000)
    def __str__(self):
        return self.username


class AboutModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=250)
    profession=models.CharField(max_length=250)
    DateOfBirth=models.DateField()
    webiste=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    freelancer=models.CharField(max_length=250)
    desc=models.TextField(max_length=3000)
    thumbnail=models.ImageField(upload_to="profile/")
    

