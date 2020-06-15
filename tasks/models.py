from django.db import models

# Create your models here.
# text = tekst zadatka za ToDo
# complete = boolenan vrijednost (true,false) po defaultu stavimo da nije uradjen zadatak (false)

class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text