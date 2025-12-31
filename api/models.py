from django.db import models



class Cat(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    breed = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Country(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Mission(models.Model):
    cat = models.ForeignKey(Cat, null=True, on_delete=models.CASCADE, related_name='missions')
    is_completed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Target(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    notes = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    mission = models.ForeignKey('Mission', on_delete=models.CASCADE, related_name='targets')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

