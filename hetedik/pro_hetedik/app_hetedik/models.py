from django.db import models


# Django ORM: Object relational mapping



# Create your models here.

class Mufajka(models.Model):

    ajdi = models.IntegerField()
    nev = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Műfaj"
        verbose_name_plural = "MŰfajOk"

    def __str__(self):
        return self.nev



class Darab(models.Model):

    # VARCHAR(100)
    cim = models.CharField(max_length=100)
    mufaj = models.ForeignKey(Mufajka, on_delete=models.CASCADE)
    # bemutato = models.DateField(auto_now_add=True) # a LÉTREHOZÁS pillanatában a dátum
    # utolso = models.DateField(auto_now=True) # a legutóbbi SZERKESZTÉS dátuma
    bemutato = models.DateField() # a LÉTREHOZÁS pillanatában a dátum
    utolso = models.DateField() # a legutóbbi SZERKESZTÉS dátuma
    hanyszor = models.IntegerField(default=1) # alapértelmezett érték: 1
    nezoszam = models.IntegerField(blank=True, null=True) # nem kötelező mező!

            
    

    class Meta:
        verbose_name = "Darab"
        verbose_name_plural = "DarabOK"

    def __str__(self):
        return self.cim + f' {self.bemutato} - {self.utolso}'


