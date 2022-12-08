from django.db import models

# User
#   First Name
#   Last Name
#   Address
#   Phone Number


# Address
#   Number
#   Street Name
#   Apt Number (Optional)
#   Zip code
#   City
#   State

class Address(models.Model):
    number = models.CharField(max_length=8)
    street_name = models.CharField(max_length=64)
    apt = models.CharField(max_length=64, default='')
    zip_code = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=32)

class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=16)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    