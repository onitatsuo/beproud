from django.db import models

# Create your models here.

class Master(models.Model):
    id = models.AutoField(primary_key=True)
    fruit_name = models.CharField(max_length=30)
    fruit_price = models.IntegerField()
    fruit_date = models.DateField()

#def get_context(self, request):
#        context = super().get_context(request)
#        context['fruits'] = Master.objects.all()
#        return context


class Add(models.Model):
    fruit_name = models.CharField(max_length=30)
    fruit_price = models.IntegerField()
    fruit_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
