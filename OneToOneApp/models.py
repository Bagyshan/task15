from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)
    geography = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Flag(models.Model):
    color = models.CharField(max_length=50)
    form = models.CharField(max_length=50)
    country = models.OneToOneField(
        Country,
        on_delete=models.CASCADE,
        related_query_name='country'
    )


    def __str__(self) -> str:
        return f'{self.color}, {self.form}'