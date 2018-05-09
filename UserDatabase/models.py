# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.datetime_safe import datetime
from django.db import models


# Create your models here.



class student_details(models.Model):
    student_name = models.CharField(max_length=50, default='')
    date_of_birth = models.CharField(max_length=50, default='')
    goal = models.CharField(max_length=50, default='')
    phone1 = models.CharField(max_length=15, default='')
    current_education = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    school = models.CharField(max_length=50, default='')
    school_duration = models.CharField(max_length=50, default='')
    school_board = models.CharField(max_length=50, default='')
    school_achievements = models.CharField(max_length=150, default='')
    collage1 = models.CharField(max_length=50, default='')
    collage_course1 = models.CharField(max_length=50, default='')
    collage_achievements1 = models.CharField(max_length=150, default='')
    collage_duration1 = models.CharField(max_length=50, default='')
    collage2 = models.CharField(max_length=50, default='')
    collage_course2 = models.CharField(max_length=50, default='')
    collage_achievements2 = models.CharField(max_length=150, default='')
    collage_duration2 = models.CharField(max_length=50, default='')
    docfile = models.FileField(upload_to='guide')

    def __unicode__(self):
        return self.email


class guide_details(models.Model):
    guide_name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    work_details = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    aboutguide = models.CharField(max_length=210, default='')
    company1 = models.CharField(max_length=50, default='')
    companyduration1 = models.CharField(max_length=50, default='')
    positionInCompany1 = models.CharField(max_length=50, default='')
    company2 = models.CharField(max_length=50, default='')
    companyduration2 = models.CharField(max_length=50, default='')
    positionInCompany2 = models.CharField(max_length=50, default='')
    company3 = models.CharField(max_length=50, default='')
    companyduration3 = models.CharField(max_length=50, default='')
    positionInCompany3 = models.CharField(max_length=50, default='')
    docfile = models.FileField(upload_to='sponsor')
    certificate = models.FileField(upload_to='guide', null=True, blank=True)
    def __unicode__(self):
        return self.guide_name


class spons_details(models.Model):
    sponsor_name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=50, default='')
    aboutsponsor = models.CharField(max_length=210, default='')
    email = models.EmailField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    company1 = models.CharField(max_length=50, default='')
    positionInCompany1 = models.CharField(max_length=50, default='')
    docfile = models.FileField(upload_to='doc')


class student_inbox(models.Model):
    student_mail = models.EmailField(max_length=50, default='')
    sender_mail_1 = models.EmailField(max_length=50, default='')
    sender_message_1 = models.CharField(max_length=100, default='')
    sender_mail_2 = models.EmailField(max_length=50, default='')
    sender_message_2 = models.CharField(max_length=100, default='')
    sender_mail_3 = models.EmailField(max_length=50, default='')
    sender_message_3 = models.CharField(max_length=100, default='')
    sender_mail_4 = models.EmailField(max_length=50, default='')
    sender_message_4 = models.CharField(max_length=100, default='')
    sender_mail_5 = models.EmailField(max_length=50, default='')
    sender_message_5 = models.CharField(max_length=100, default='')


class guide_inbox(models.Model):
    guide_mail = models.EmailField(max_length=50, default='')
    sender_mail_1 = models.EmailField(max_length=50, default='')
    sender_message_1 = models.CharField(max_length=100, default='')
    sender_mail_2 = models.EmailField(max_length=50, default='')
    sender_message_2 = models.CharField(max_length=100, default='')
    sender_mail_3 = models.EmailField(max_length=50, default='')
    sender_message_3 = models.CharField(max_length=100, default='')
    sender_mail_4 = models.EmailField(max_length=50, default='')
    sender_message_4 = models.CharField(max_length=100, default='')
    sender_mail_5 = models.EmailField(max_length=50, default='')
    sender_message_5 = models.CharField(max_length=100, default='')


class sponsor_inbox(models.Model):
    sponsor_mail = models.EmailField(max_length=50, default='')
    sender_mail_1 = models.EmailField(max_length=50, default='')
    sender_message_1 = models.CharField(max_length=100, default='')
    sender_mail_2 = models.EmailField(max_length=50, default='')
    sender_message_2 = models.CharField(max_length=100, default='')
    sender_mail_3 = models.EmailField(max_length=50, default='')
    sender_message_3 = models.CharField(max_length=100, default='')
    sender_mail_4 = models.EmailField(max_length=50, default='')
    sender_message_4 = models.CharField(max_length=100, default='')
    sender_mail_5 = models.EmailField(max_length=50, default='')
    sender_message_5 = models.CharField(max_length=100, default='')


GOAL_CHOICES = (
    ('CSE', 'CSE'),
    ('ECE', 'ECE'),
    ('MEC', 'MEC'),
    ('CIVIL', 'CIVIL'),
    ('DOCTOR', 'DOCTOR'),
)


class notify_me(models.Model):
    goaltype = models.CharField(max_length=20, choices=GOAL_CHOICES, default='IAS')
    notification = models.CharField(max_length=50, default='null')
    notify = models.TextField(max_length=500)
    created_on = models.DateTimeField(default=datetime.now, blank=True)


class scholorship(models.Model):
    apply_scholorship = models.URLField(max_length=200)
    goaltype = models.CharField(max_length=20, choices=GOAL_CHOICES, default='ias')
    scholorship_details = models.TextField(max_length=500)
