from django.db import models

# Create your models here.
class Item(models.Model):
    address = models.CharField(max_length=20)
    location = models.CharField(max_length=500)
    area = models.DecimalField(max_digits=5,decimal_places=2)
    balcony_num = models.IntegerField()
    bedroom_num = models.IntegerField()
    hall_num = models.IntegerField()
    toilet_num = models.IntegerField()
    facing = models.CharField(max_length=2,choices=(('e','正东'),('w','正西'),('n','正北'),('s','正南'),('ne','东北'),('nw','西北'),('se','东南'),('sw','西南')))
    floor = models.IntegerField()
    floor_height = models.CharField(max_length=1,choices=(('l','低'),('m','中'),('h','高')))
    has_elevator = models.BooleanField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    renting_type = models.CharField(max_length=2,choices=(('整租','整租'),('合租','合租')))
    tags = models.CharField(max_length=500)
    title = models.CharField(max_length=30)
    usage = models.CharField(max_length=2,choices=(('居家','居家'),('办公','办公')))