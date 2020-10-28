from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Ingredient(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Character(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tea(models.Model):

    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    weight = models.FloatField()
    description = models.TextField()
    ingredient = models.ManyToManyField(Ingredient)
    character = models.ManyToManyField(Character)
    suggestion = models.CharField(max_length=50)
    color = models.CharField(max_length=20, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.name = str.upper(self.name)
        return super().save(*args, **kwargs)