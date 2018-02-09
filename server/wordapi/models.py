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
    question = models.CharField(max_length=500)
    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"

    def __unicode__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=500)
    class Meta:
        verbose_name = "answer"
        verbose_name_plural = "answers"

    def __unicode__(self):
        return self.answer