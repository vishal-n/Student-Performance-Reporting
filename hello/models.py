from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	score = models.FloatField()
	semester = models.IntegerField()



