from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        return timezone.now() - timedelta(days=1) <= self.pub_date <= timezone.now()
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    

class Profile(models.Model):
    profile_id = models.AutoField(primary_key=True),
    profile_id_int = models.IntegerField(unique=True, default=0)
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    looking_for = models.CharField(max_length=2000)