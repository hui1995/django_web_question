from django.db import models

# Create your models here.

class Question(models.Model):
    title =models.CharField(max_length=256)
    Recommendation=models.TextField()
    qid=models.IntegerField()





class AnswerRecord(models.Model):
    userId=models.IntegerField()
    isFinish=models.IntegerField(default=0)

class Answer(models.Model):
    titleId=models.IntegerField()
    rid=models.IntegerField()
    result=models.IntegerField()


class Kit_Interested_Countries(models.Model):
    rid=models.IntegerField()

    name=models.CharField(max_length=256,null=True)
    gender=models.CharField(max_length=256,null=True)
    suburb=models.CharField(max_length=256,null=True)
    country=models.CharField(max_length=256,null=True)
    province=models.CharField(max_length=256,null=True)
    email=models.CharField(max_length=256,null=True)


