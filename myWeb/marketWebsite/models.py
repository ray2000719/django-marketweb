from django.db import models

typeChoice = (('蔬菜',"蔬菜"), ('水果',"水果"), ('肉類',"肉類"), ('蛋類',"蛋類"))

# Create your models here.
class production(models.Model):
    
    pimg = models.ImageField(null=True, blank=True, upload_to="images/")
    pname = models.CharField(max_length=200)
    ptype = models.CharField(max_length=200, choices=typeChoice)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pname