from django.db import models


class Service(models.Model):
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=4000)


class Contact(models.Model):
    number = models.CharField(max_length=100)
    address = models.TextField(max_length=200)
    instagram = models.TextField(max_length=200)
    facebook = models.TextField(max_length=200)


class New(models.Model):
    img = models.ImageField(upload_to='')
    title = models.TextField(max_length=400)
    text = models.TextField(max_length=5000)
