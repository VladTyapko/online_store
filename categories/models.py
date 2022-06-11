from django.urls import reverse
from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    img = models.ImageField(upload_to='course_images')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "categories:products", kwargs={"slug": self.slug, "pk": self.id}
        )

    def get_image(self):
        return self.img.url if self.img else settings.STATIC_URL + 'images/default.png'



class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('id',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'


    def __str__(self):
        return self.name

    def get_image(self):
        return self.image.url if self.image else settings.STATIC_URL + 'images/default.png'
