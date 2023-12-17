from django.db import models

# Create your models here.
class Bus(models.Model):
    busnumber = models.IntegerField()
    busmodel = models.CharField(max_length=50, null=True)
    
    def __str__(self) -> str:
        return f'{self.busnumber}'
    
class Human(models.Model):
    SEX = (
        ('male', 'мужской'),
        ('female', 'женский')
    )
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=20, choices=SEX)
    bus = models.ManyToManyField(
        Bus,
        related_query_name='humans'
    )

    def __str__(self) -> str:
        return f'{self.name}, {self.sex}'
    

