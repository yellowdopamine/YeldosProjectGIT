from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
# Category
# Product
# CartProduct
# Cart
# Order
# Specifications
user = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя категории")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    # class Meta:
    #     abstract = True

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey(User, verbose_name="Покупатель", on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name="Корзина", on_delete=models.CASCADE, related_name="related_products")
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return "Продукт: {}".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name="related_cart")
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Сумма")

    def __str__(self):
        return str(self.id)


class Specification(models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    name = models.CharField(max_length=255, verbose_name="Имя товара для характеристик")

    def __str__(self):
        return "Характеристики для товаров: {}".format(self.name)
