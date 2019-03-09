from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TotalScore(models.Model):
    username=models.CharField(max_length=50,default="sumanth")
    sixthquestionanswer=models.IntegerField(default=0)
    sixthquestionmarks=models.IntegerField(default=0)
    seventhquestionanswer=models.IntegerField(default=0)
    seventhquestionmarks=models.IntegerField(default=0)
    eigthquestionanswer=models.CharField(max_length=300,default="n/a")
    eigthquestionmarks=models.IntegerField(default=0)
    ninthquestionanswer=models.CharField(max_length=300,default="n/a")
    ninthquestionmarks=models.IntegerField(default=0)
    totalmarks=models.IntegerField(default=0)
    percentage=models.IntegerField(default=0)

class UserProfileInfo(models.Model):
    CHOICES = [('Admin', 'Admin'),
    ('User', 'User')]
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    role = models.CharField(max_length = 8, choices = CHOICES)

    def __str__(self):
        return self.user.username
