from django.db import models

class About(models.Model):
    title_web = models.CharField(max_length= 30)
    name = models.CharField(max_length= 20)
    l_name = models.CharField(max_length= 20)
    ability = models.CharField(max_length= 50)
    discription = models.TextField()
    image = models.ImageField(upload_to= 'me')
    def __str__(self) -> str:
        return self.title_web

class library(models.Model):
    library_name = models.CharField(max_length=50)
    library_detail = models.TextField()
    def __str__(self) -> str:
        return self.library_name

class Experience(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length= 50)
    explanation_title = models.CharField(max_length= 50, null= True)
    discription = models.TextField()
    def __str__(self):
        return self.title

class Education(models.Model):
    year = models.IntegerField()
    title = models.CharField(max_length= 50)
    explanation_title = models.CharField(max_length= 50)
    discription = models.TextField()
    site_link = models.CharField(max_length= 30)
    def __str__(self):
        return self.title

class Contact_me (models.Model):
    number = models.CharField(max_length= 13)
    email = models.EmailField()
    telegram =  models.CharField(max_length= 50)
    instagram =  models.CharField(max_length= 50)
    whatsapp =  models.CharField(max_length= 50)

class Recieve_massage(models.Model):
    name = models.CharField(max_length= 50)
    email = models.EmailField()
    massage = models.TextField()