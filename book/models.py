from django.db import models

class Ingredient(models.Model):

    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=128)
    source = models.CharField(max_length=256)
    sourceName = models.CharField(max_length=64, default='Y_lab')
    steps = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, through='Measurement')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Measurement(models.Model):

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    qty = models.CharField(max_length=64)
    unit = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.qty} {self.unit} {self.ingredient}"

