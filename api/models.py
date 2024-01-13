from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='card/')
    image1 = models.ImageField(upload_to='card/')
    image2 = models.ImageField(upload_to='card/')
    image3 = models.ImageField(upload_to='card/')
    full_info = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name