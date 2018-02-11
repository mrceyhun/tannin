from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class Word(models.Model):
    kelime = models.CharField(max_length=100)
    class Meta:
        verbose_name = "word"
        verbose_name_plural = "words"
    def __unicode__(self):
        return self.name

class Question(models.Model):
    #user_id
    question = models.CharField(max_length=500)
    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"
    def __unicode__(self):
        return self.question

class Answer(models.Model):
    #user_id
    answer = models.CharField(max_length=500)
    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"
    def __unicode__(self):
        return self.answer

#d.phonenumber_set.objects.all()
class Q_and_W_rel(models.Model):
    #user_id
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)
    kelime = models.OneToOneField(Word, on_delete=models.CASCADE)

class A_and_W_rel(models.Model):
    answer = models.OneToOneField(Answer, primary_key=True, on_delete=models.CASCADE)
    kelime = models.OneToOneField(Word, on_delete=models.CASCADE)

class Q_A_and_W_rel(models.Model):
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)
    answer = models.OneToOneField(Answer,  on_delete=models.CASCADE)
    kelime = models.OneToOneField(Word, on_delete=models.CASCADE)

class Q_quality(models.Model):
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)
    #user_id     models.ForeignKey(Question, primary_key=True, on_delete=models.CASCADE)
    quality =  models.BooleanField()

class A_quality(models.Model):
    answer = models.OneToOneField(Answer, primary_key=True, on_delete=models.CASCADE)
    #user_id     models.ForeignKey(Question, primary_key=True, on_delete=models.CASCADE)
    quality =  models.BooleanField()

class Q_and_A_compatibility(models.Model):
    question = models.OneToOneField(Question, primary_key=True, on_delete=models.CASCADE)
    answer = models.OneToOneField(Answer,  on_delete=models.CASCADE)
    #user_id     models.ForeignKey(Question, primary_key=True, on_delete=models.CASCADE)
    compatibility =  models.BooleanField()

"""
class User_control(models.Model):
    Id
    one_of(Q|A|Q&A)
    user_id
    user_puan

class Control_q_and_a(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500)
    class Meta:
        verbose_name = "control question and answer"
        verbose_name_plural = "control questions and answers"
    def __unicode__(self):
        return "Q: %s \nA: %s"%(self.question, self.answer)
"""
