from django.db import models

class table_user(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)

    class Meta:
        db_table='table_user'

class table_gadgets(models.Model):
    g_name=models.CharField(max_length=50)
    g_price=models.IntegerField()
    g_warranty=models.CharField(max_length=50)
    photo=models.CharField(max_length=500)
    g_category=models.CharField(max_length=50)

    class Meta:
        db_table='table_gadgets'
# Create your models here.
