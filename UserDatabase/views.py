# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from UserDatabase.models import student_details, guide_details, spons_details, student_inbox, guide_inbox, \
    sponsor_inbox


def SaveStudentData(request):
    if User.objects.filter(email=request.POST["email"]).exists():
        return render(request, 'alert/duplicate_email.html')
    if User.objects.filter(username=request.POST["uname"]).exists():
        return render(request, 'alert/duplicate_user.html')
    try:
        user = User.objects.create_user(username=request.POST["uname"], email=request.POST["email"],
                                        password=request.POST["psw"])
        user.first_name = 'student'
        user.save()
        us = student_details(student_name=request.POST["uname"], location=request.POST["address"],
                             current_education=request.POST["edulist"], phone1=request.POST["phone"],
                             date_of_birth=request.POST["bday"], email=request.POST["email"],
                             password=request.POST["psw"], goal=request.POST["goal"], docfile=request.FILES['docfile'])
        us.save()
        p = student_inbox(student_mail=request.POST["email"])
        p.save()
    except:
        return render(request, 'alert/duplicate_user.html')
    return render(request, 'alert/relogin.html')


def SaveGuideData(request):
    if User.objects.filter(email=request.POST["email"]).exists():
        return render(request, 'alert/duplicate_email.html')
    if User.objects.filter(username=request.POST["uname"]).exists():
        return render(request, 'alert/duplicate_user.html')

    user = User.objects.create_user(username=request.POST["uname"], email=request.POST["email"],
                                    password=request.POST["psw"])
    user.first_name = 'guide'
    user.is_active = False
    user.save()
    us = guide_details(guide_name=request.POST["uname"], email=request.POST["email"], password=request.POST["psw"],
                       docfile=request.FILES['docfile'],certificate=request.FILES['certificate1'])
    us.save()
    p = guide_inbox(guide_mail=request.POST["email"])
    p.save()

    return render(request, 'alert/relogin.html')


def SaveSponsorData(request):
    if User.objects.filter(email=request.POST["email"]).exists():
        return render(request, 'alert/duplicate_email.html')
    if User.objects.filter(username=request.POST["uname"]).exists():
        return render(request, 'alert/duplicate_user.html')
    try:
        user = User.objects.create_user(username=request.POST["uname"], email=request.POST["email"],
                                        password=request.POST["psw"])
        user.first_name = 'sponsor'
        user.save()
        us = spons_details(sponsor_name=request.POST["uname"],
                           address=request.POST["address"], email=request.POST["email"], password=request.POST["psw"],
                           docfile=request.FILES['docfile'])
        us.save()
        p = sponsor_inbox(sponsor_mail=request.POST["email"])
        p.save()
    except:
        return render(request, 'alert/duplicate_user.html')
    return render(request, 'alert/relogin.html')


def EditGuideAbout(request, id):
    if request.user.is_authenticated():
        print(request.POST["AboutMe"])
        t = guide_details.objects.get(id=id)
        t.aboutguide = request.POST["AboutMe"]
        t.save()
        students = student_details.objects.all()
        gmessages = guide_inbox.objects.all()
        return render(request, 'guidepages/guide_homepage.html', {'f': t, 'students': students, 'gmessages': gmessages})
    return render(request, 'alert/session_timeout.html')


def EditGuideCompany1(request, id):
    if request.user.is_authenticated():
        t = guide_details.objects.get(id=id)
        t.company1 = request.POST["CompanyName"]
        t.companyduration1 = request.POST["Duration"]
        t.positionInCompany1 = request.POST["PositionInCompany"]
        t.save()
        students = student_details.objects.all()
        gmessages = guide_inbox.objects.all()
        return render(request, 'guidepages/guide_homepage.html', {'f': t, 'students': students, 'gmessages': gmessages})
    return render(request, 'alert/session_timeout.html')


def EditGuideCompany2(request, id):
    if request.user.is_authenticated():
        t = guide_details.objects.get(id=id)
        t.company2 = request.POST["CompanyName"]
        t.companyduration2 = request.POST["Duration"]
        t.positionInCompany2 = request.POST["PositionInCompany"]
        t.save()
        students = student_details.objects.all()
        gmessages = guide_inbox.objects.all()
        return render(request, 'guidepages/guide_homepage.html', {'f': t, 'students': students, 'gmessages': gmessages})
    return render(request, 'alert/session_timeout.html')


def EditGuideCompany3(request, id):
    if request.user.is_authenticated():
        t = guide_details.objects.get(id=id)
        t.company3 = request.POST["CompanyName"]
        t.companyduration3 = request.POST["Duration"]
        t.positionInCompany3 = request.POST["PositionInCompany"]
        t.save()
        students = student_details.objects.all()
        gmessages = guide_inbox.objects.all()
        return render(request, 'guidepages/guide_homepage.html', {'f': t, 'students': students, 'gmessages': gmessages})
    return render(request, 'alert/session_timeout.html')


def EditSponsAbout(request, id):
    if request.user.is_authenticated():
        print(request.POST["AboutMe"])
        t = spons_details.objects.get(id=id)
        t.aboutsponsor = request.POST["AboutMe"]
        t.save()
        students = student_details.objects.all()
        return render(request, 'sponsorpages/sponsor_homepage.html', {'f': t, 'students': students})
    return render(request, 'alert/session_timeout.html')


def EditSponsCompany1(request, id):
    if request.user.is_authenticated():
        print(request.POST["CompanyName"])
        print(request.POST["Duration"])
        print(request.POST["PositionInCompany"])
        t = spons_details.objects.get(id=id)
        t.company1 = request.POST["CompanyName"]
        t.positionInCompany1 = request.POST["PositionInCompany"]
        t.save()
        students = student_details.objects.all()
        return render(request, 'sponsorpages/sponsor_homepage.html', {'f': t, 'students': students})
    return render(request, 'alert/session_timeout.html')


def MessageToGuide(request, id, id2):
    if request.user.is_authenticated():
        print(request.POST["message"])
        v = guide_details.objects.get(id=id)
        print(v.email)
        p = guide_inbox.objects.get(guide_mail=v.email)
        k = student_details.objects.get(id=id2)
        if p.sender_mail_1 is '':
            print('111')
            p.sender_mail_1 = k.email
            p.sender_message_1 = request.POST["message"]
            p.save()
        elif p.sender_mail_2 is '':
            print('2222')
            p.sender_mail_2 = k.email
            p.sender_message_2 = request.POST["message"]
            p.save()
        elif p.sender_mail_3 is '':
            p.sender_mail_3 = k.email
            p.sender_message_3 = request.POST["message"]
            p.save()
        elif p.sender_mail_4 is '':
            p.sender_mail_4 = k.email
            p.sender_message_4 = request.POST["message"]
            p.save()
        elif p.sender_mail_5 is '':
            p.sender_mail_5 = k.email
            p.sender_message_5 = request.POST["message"]
            p.save()
        elif p.sender_mail_1 is not '':
            print('111')
            p.sender_mail_1 = k.email
            p.sender_message_1 = request.POST["message"]
            p.save()
        elif p.sender_mail_2 is not '':
            print('2222')
            p.sender_mail_2 = k.email
            p.sender_message_2 = request.POST["message"]
            p.save()
        elif p.sender_mail_3 is not '':
            p.sender_mail_3 = k.email
            p.sender_message_3 = request.POST["message"]
            p.save()
        elif p.sender_mail_4 is not '':
            p.sender_mail_4 = k.email
            p.sender_message_4 = request.POST["message"]
            p.save()
        elif p.sender_mail_5 is not '':
            p.sender_mail_5 = k.email
            p.sender_message_5 = request.POST["message"]
            p.save()
        print('4444')
        flag = 1
        return render(request, 'guidepages/guideprofileview.html', {'v': v, 'k': k, 'flag': flag})
    return render(request, 'alert/session_timeout.html')


def MessageToStudent(request, id, id2):
    if request.user.is_authenticated():
        print(request.POST["message"])
        v = student_details.objects.get(id=id)
        print(v.email)
        p = student_inbox.objects.get(student_mail=v.email)
        k = guide_details.objects.get(id=id2)
        if p.sender_mail_1 is '':
            print('111')
            p.sender_mail_1 = k.email
            p.sender_message_1 = request.POST["message"]
            p.save()
        elif p.sender_mail_2 is '':
            print('2222')
            p.sender_mail_2 = k.email
            p.sender_message_2 = request.POST["message"]
            p.save()
        elif p.sender_mail_3 is '':
            p.sender_mail_3 = k.email
            p.sender_message_3 = request.POST["message"]
            p.save()
        elif p.sender_mail_4 is '':
            p.sender_mail_4 = k.email
            p.sender_message_4 = request.POST["message"]
            p.save()
        elif p.sender_mail_5 is '':
            p.sender_mail_5 = k.email
            p.sender_message_5 = request.POST["message"]
            p.save()
        elif p.sender_mail_1 is not '':
            print('111')
            p.sender_mail_1 = k.email
            p.sender_message_1 = request.POST["message"]
            p.save()
        elif p.sender_mail_2 is not '':
            print('2222')
            p.sender_mail_2 = k.email
            p.sender_message_2 = request.POST["message"]
            p.save()
        elif p.sender_mail_3 is not '':
            p.sender_mail_3 = k.email
            p.sender_message_3 = request.POST["message"]
            p.save()
        elif p.sender_mail_4 is not '':
            p.sender_mail_4 = k.email
            p.sender_message_4 = request.POST["message"]
            p.save()
        elif p.sender_mail_5 is not '':
            p.sender_mail_5 = k.email
            p.sender_message_5 = request.POST["message"]
            p.save()
        print('4444')

        flag = 1
        return render(request, 'studentpages/student_profile_view.html', {'v': v, 'f': k, 'flag': flag})
    return render(request, 'alert/session_timeout.html')
