from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ObjectDoesNotExist

class Word(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = "word"
        verbose_name_plural = "words"
    def __unicode__(self):
        return self.name

class Question(models.Model):
    #user_id
    sentence = models.CharField(max_length=500)
    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"
    def __unicode__(self):
        return self.sentence

class Answer(models.Model):
    #user_id
    sentence = models.CharField(max_length=500)
    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"
    def __unicode__(self):
        return self.sentence

class Q_and_W_rel(models.Model):
    #user_id
    question = models.PositiveIntegerField(primary_key=True)
    #ID of word
    word = models.PositiveIntegerField()
    def clean(self):
        if Word.objects.filter(id=word).count() <= 0:
            raise ObjectDoesNotExist(_('Given id of the Word is not in the DB'))


class A_and_W_rel(models.Model):
    answer = models.PositiveIntegerField(primary_key=True)
    word = models.PositiveIntegerField()
    def clean(self):
        if Word.objects.filter(id=word).count() <= 0:
            raise ObjectDoesNotExist(_('Given id of the Word is not in the DB'))

class Q_A_and_W_rel(models.Model):
    question = models.PositiveIntegerField(primary_key=True)
    answer = models.PositiveIntegerField()
    kelime = models.PositiveIntegerField()

class Q_quality(models.Model):
    question = models.PositiveIntegerField(primary_key=True)
    #user_id     models.ForeignKey(Question, primary_key=True, on_delete=models.CASCADE)
    quality =  models.BooleanField()

class A_quality(models.Model):
    answer = models.PositiveIntegerField(primary_key=True)
    #user_id     models.ForeignKey(Question, primary_key=True, on_delete=models.CASCADE)
    quality =  models.BooleanField()

class Q_and_A_compatibility(models.Model):
    question = models.PositiveIntegerField(primary_key=True)
    answer = models.PositiveIntegerField()
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
