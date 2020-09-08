from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Avaliacao(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comentario = models.TextField(null=True,blank=True)
    nota = models.DecimalField(decimal_places=10,max_digits=10)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username