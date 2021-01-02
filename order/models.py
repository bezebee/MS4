from django.db import models


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    sketch_name = models.CharField(max_length=254)
    sketch_sku = models.CharField(max_length=254)
    description = models.TextField()
    special_requests = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


