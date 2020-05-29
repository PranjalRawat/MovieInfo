from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib import auth
# Create your models here.
class AddProduct(models.Model):
    user         = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=callable)
    movie_name   = models.CharField(max_length=140)
    description  = models.TextField()
    director     = models.CharField(max_length=140)
    image        = models.ImageField(upload_to='product_images/')
    actors       = models.CharField(max_length=240)
    genre        = models.CharField(max_length=140)
    country      = models.CharField(max_length=140)
    updated      = models.DateTimeField(auto_now=True)
    timestamp    = models.DateTimeField(auto_now_add=True)
    language     = models.CharField(max_length=140)
    release_date = models.DateField()

    HOLLYWOOD = 'hollywood'
    BOLLYWOOD = 'bollywood'
    TOLLYWOOD = 'tollywood'
    ANIMATED  = 'animated'

    Movies_Category = [
        (HOLLYWOOD, 'Hollywood'),
        (BOLLYWOOD, 'Bollywood'),
        (TOLLYWOOD, 'Tollywood'),
        (ANIMATED, 'Animated'),
    ]
    category = models.CharField(
        max_length=12,
        choices=Movies_Category,
        default=HOLLYWOOD,
    )

    def __str__(self):
         return str(self.movie_name)

    def get_absolute_url(self):
        return reverse("product:detail" ,kwargs={"pk":self.pk})


class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return str(self.username)