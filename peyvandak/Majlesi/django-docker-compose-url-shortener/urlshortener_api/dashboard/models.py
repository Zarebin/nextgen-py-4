from django.db import models
from ipaddress import ip_address
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    product_category = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=50)
    shipping_cost = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)



class VisitUrl(models.Model):
    short_url = models.CharField(max_length=15, blank=True)
    #ip_address = models. GenericIPAddressField()
    visit_date = models.DateTimeField(auto_now_add=True)
    response_date = models.DateTimeField(auto_now_add=True)
    #device = models.CharField(max_length=20, blank=True)
    visitor = models.CharField(max_length=20)

    device = models.CharField(max_length=15)
    browser = models.CharField(max_length=15)
    browser_version = models.CharField(max_length=15)
    os = models.CharField(max_length=15)
    os_version = models.CharField(max_length=10)
    ip_address = models. GenericIPAddressField(blank=True, null=True)

    class Meta:
        ordering = ["-visit_date"]



# Create your models here.
class Shortener(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)

    unique_times_followed = models.PositiveIntegerField(default=0)    

    long_url = models.URLField()

    short_url = models.CharField(max_length=15, unique=True, blank=True)

    device = models.CharField(max_length=15, blank=True)
    
    #owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=-1)
    shortner_owner = models.CharField(max_length=20, editable=False, blank=True)

    ip_address = models. GenericIPAddressField(blank=True, null=True)

    class Meta:
        ordering = ["-created_date"]


    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
    

    #def save(self, *args, **kwargs):
    #    if not self.short_url:
    #        self.short_url = create_shortened_url(self)
    #    super().save(*args, **kwargs)
           
