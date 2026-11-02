from django.db import models

# Create your models here.
class Item(models.Model):
  def __str__(self):
    return self.Item_name
      
  Item_name = models.CharField(max_length=200)
  Item_description = models.CharField(max_length=500)
  Item_price = models.IntegerField()