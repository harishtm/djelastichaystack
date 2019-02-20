from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True, db_index=True, default='')
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField(db_index=True)
    brand = models.CharField(max_length=255, db_index=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images/')
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title