from django.db import models



class Szerzo(models.Model):
 
    nev = models.CharField(max_length=100)
    birth = models.DateField(auto_now_add=True)

 
    class Meta:
        verbose_name = ("Szerző")
        verbose_name_plural = ("Szerzők")
 
    def __str__(self):
        return self.nev



class Konyv(models.Model):

    nev = models.CharField(max_length=100)
    szerzo = models.ForeignKey(Szerzo,on_delete=models.CASCADE)
    jo_e = models.BooleanField(default=True)
    db = models.IntegerField()
    ar = models.FloatField(blank=True,null=True)

    class Meta:
        verbose_name = "Könyv"
        verbose_name_plural = "Könyvek"

    def __str__(self):
        return self.nev


    


 