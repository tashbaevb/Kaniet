from django.db import models


class Home_about(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()


class Do(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=2000)
    img = models.ImageField(upload_to='')


class New(models.Model):
    img = models.ImageField(upload_to='')
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=5000)


class Mission(models.Model):
    about = models.TextField(max_length=4000)
    missions = models.TextField(max_length=2000)


class Place(models.Model):
    img = models.ImageField(upload_to="")
