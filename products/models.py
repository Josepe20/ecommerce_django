from django.db import models
from base.models import BaseModel
from django.utils.text import slugify



class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to='categories')

    def save_category(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return self.category_name



class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.color_name


class StorageVariant(BaseModel):
    storage_num = models.CharField(max_length=100)
    price_extra = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.storage_num


class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    color_variant = models.ManyToManyField(ColorVariant)
    storage_variant = models.ManyToManyField(StorageVariant)


    def save_product(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name

    def get_product_price_by_storage(self, storage):
        return self.price + StorageVariant.objects.get(storage_num=storage).price_extra


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='product')


