from django.db import models
from django.contrib.auth.models import User

class detailsuser(models.Model):
    userdetails = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,unique=True)
    money = models.IntegerField(default='0')
    oplatil = models.CharField(max_length=1000)
    temporaryamount = models.IntegerField(verbose_name='Временная сумма:',help_text='Если пользователь не оплатил',default=0)
    def __str__(self):
        return str(self.userdetails)
class blog(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
class Prices(models.Model):
    product = models.CharField(max_length=100)
      # image = models.ImageField()
    useralot = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,unique=True)
    text = models.TextField()
    prise = models.IntegerField()
    slug = models.SlugField(max_length=100,unique=True, null=True)
    docker_choose = models.CharField(max_length=100)
    uuid = models.CharField(max_length=1024)
    userconnect = models.OneToOneField(User,on_delete=models.CASCADE,unique=True,related_name='fix')
   # userconnect = models.ManyToManyField(detailsuser)
    is_active = models.BooleanField(default=False)
    file = models.FileField(upload_to = 'media/',null=True)

    def __str__(self):
        return self.product

