from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Category(models.Model):
    category_id = models.AutoField
    status = models.BooleanField(default=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='shop/images', default="")
    slug = models.SlugField(max_length=300, default=name)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class User(AbstractUser):
    #email = models.EmailField(verbose_name='email',max_length=255,unique=True)
    phone = models.IntegerField(blank=True,null=True)
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name']
    #USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email


