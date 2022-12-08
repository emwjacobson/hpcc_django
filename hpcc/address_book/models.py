from django.db import models

class Address(models.Model):
    number = models.CharField(max_length=8)
    street_name = models.CharField(max_length=64)
    apt = models.CharField(max_length=64, blank=True)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=32)
    
    def __str__(self):
        return F"{self.number} {self.street_name} {self.apt}, {self.city}, {self.state}, {self.zip_code}"

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return F"{self.first_name} {self.last_name}"
    