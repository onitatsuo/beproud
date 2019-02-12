from django.db import models

# Create your models here.

class Master(models.Model):
    id = models.AutoField(primary_key=True)
    fruit_name = models.CharField(max_length=30)
    fruit_price = models.IntegerField()
    fruit_date = models.DateField()

def get_context(self, request):
        context = super().get_context(request)
        context['fruits'] = Master.objects.all()
        return context

  #  def __str__(self):
  #      return self.fruit_name

  #  def __str__(self):
  #      return self.fruit_price

  #  def __str__(self):
  #      return self.fruit_date
