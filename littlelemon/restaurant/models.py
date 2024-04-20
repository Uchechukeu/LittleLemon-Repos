from django.db import models

# Create your models here.
class menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    inventory = models.IntegerField()
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    
    #def get_item(self):
    #    return f'{self.title} : {str(self.price)}'

class booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    
