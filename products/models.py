from django.db import models
from base.models import Base
from django.template.defaultfilters import slugify

from django.conf import settings



class Category(Base):

    name = models.CharField(max_length=120)
    category_image = models.ImageField(upload_to='category_images')
    slug = models.SlugField(unique=True , editable=False, null=True, blank=True)
    parent = models.ForeignKey('self',blank=True, null=True , related_name='children', on_delete=models.PROTECT)

    class Meta:
        managed = True
        unique_together = ('slug', 'name',) 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.name), slugify(self.id)))
        super(Category, self).save(*args, **kwargs)  

    def __str__(self):                           
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1]) 


class ColorVarient(Base):
    color = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.color

class SizeVarient(Base):
    size = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.size

class Product(Base):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="product_category" )
    price = models.DecimalField(max_digits=8,decimal_places=2)
    slug = models.SlugField( editable=False, null=True , blank=True)
    description = models.TextField()
    color = models.ManyToManyField(ColorVarient  , related_name='product_color' ,blank=True)
    size = models.ManyToManyField(SizeVarient  , related_name='product_size' ,blank=True)

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.name), slugify(self.category)))

        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class ProductImages(Base):
    product = models.ForeignKey(Product, models.CASCADE, related_name="product_img")
    image = models.ImageField(upload_to='product_images')




class Cart(Base):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name='user_cart')
    items= models.ManyToManyField(Product, through='CartItem')

class CartItem(Base):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
