from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(default='default.png', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    """
- izmērs
- tips
    """
    def __str__(self):
        return self.title



"""When model is changed do:
python manage.py makemigrations
python manage.py migrate"""
