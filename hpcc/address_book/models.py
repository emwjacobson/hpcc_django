from django.db import models

class Address(models.Model):
    number = models.CharField(max_length=8, blank=False)
    street_name = models.CharField(max_length=64, blank=False)
    apt = models.CharField(max_length=64, blank=True)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100, blank=False)
    state = models.CharField(max_length=32, blank=False)
    
    def __str__(self):
        return F"{self.number} {self.street_name} {self.apt}, {self.city}, {self.state}, {self.zip_code}"

class User(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    phone_number = models.CharField(max_length=16, blank=False)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return F"{self.first_name} {self.last_name}"
    