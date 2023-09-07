from django.db import models

# Create your models here.
class Occupation_details(models.Model):
    profession = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    salary = models.IntegerField()

    def __str__(self) -> str:
        return self.profession

class Person(models.Model):
    occupation = models.ForeignKey(Occupation_details, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name


