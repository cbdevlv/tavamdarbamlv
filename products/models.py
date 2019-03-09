from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.png', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pvn = models.PositiveSmallIntegerField(default=21)

    """
- izmērs
    """
    def __str__(self):
        return self.title
"""
    def get_cat_list(self):           #for now ignore this instance method,
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]"""

#Categries for products
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True ,related_name='children')

    class Meta:
        unique_together = ('slug', 'parent',)    #enforcing that there can not be two
        verbose_name_plural = "categories"       #categories under a parent with same
                                                 #slug

    def __str__(self):                           # __str__ method elaborated later in
        full_path = [self.name]                  # post.  use __unicode__ in place of
                                                 # __str__ if you are using python 2
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])



"""When model is changed do:
python manage.py makemigrations
python manage.py migrate"""
