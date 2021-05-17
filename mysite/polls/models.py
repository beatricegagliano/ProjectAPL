from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Utente(models.Model):
     nome = models.CharField(max_length=200)
     cognome = models.CharField(max_length=200)
     data_nascita = models.DateField ('data nascita')
     NumTessera = models.IntegerField(default=0)
     CodPersonale = models.IntegerField(default=0)



def findUtente(num_tess, cod_pers):
    if (num_tess == Utente.NumTessera) & (cod_pers == Utente.CodPersonale):
      return 'utente trovato'
    else:
        return 'utente non trovato'

x = findUtente(1, 888)
print(x)