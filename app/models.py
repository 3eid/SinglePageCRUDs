from django.db import models

# Create your models here.

class Branch(models.Model):
    customer_no = models.IntegerField(default=0)
    arabic_name = models.CharField(max_length=150, null=True,blank=True)
    arabic_description = models.CharField(max_length=200, null=True,blank=True)
    english_name = models.CharField(max_length=150, null=True,blank=True)
    english_description = models.CharField(max_length=200, null=True,blank=True)
    note = models.TextField( null=True,blank=True)
    address = models.TextField( null=True,blank=True)
    
    def __str__(self):
        return str(self.english_name)