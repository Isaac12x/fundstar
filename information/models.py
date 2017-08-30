from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    email = models.CharField(max_length=140)

    def __unicode__(self):
        return self.name


class SocialProfile(models.Model):
    angel_profile = models.CharField(max_length=200)
    crunchbase_profile = models.CharField(max_length=200)
    twitter_profile = models.CharField(max_length=200)
    linkedin_profile = models.CharField(max_length=140)

    def __unicode__(self):
        return self.angel_profile


class Ranking(models.Model):
    pass


class Score(models.Model):
    pass


class Reviews(models.Model):
    who = (
        ('A', 'Angel'),
        ('E', 'Entrepreneur'),
        ('SE', 'Successful founder'),
    )
    role = models.CharField(max_length=20, choices=who)
    name = models.CharField(max_length=120)
    review = models.CharField(max_length=800)
    given_score = models.ForeignKey(Score, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class SerialEntrepreneur(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    social = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    # industry_experience = models
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.person.name


class Angel(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    social = models.ForeignKey(SocialProfile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    accredited = models.BooleanField(default=False)
    reviews = models.ForeignKey(Reviews, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name


class ReferredAngel(models.Model):
    referrer = models.ForeignKey(SerialEntrepreneur, on_delete=models.CASCADE)
    referred = models.ForeignKey(Angel, on_delete=models.CASCADE)
    why = models.ForeignKey(Reviews, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name
