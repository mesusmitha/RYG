from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
url(r'^savestudentdata/$', views.SaveStudentData),
url(r'^saveguidedata/$', views.SaveGuideData),
url(r'^savesponsordata/$', views.SaveSponsorData),
url(r'^EditGuideAbout/(?P<id>\d+)/$', views.EditGuideAbout),
url(r'^EditGuideCompany1/(?P<id>\d+)/$', views.EditGuideCompany1),
url(r'^EditGuideCompany2/(?P<id>\d+)/$', views.EditGuideCompany2),
url(r'^EditGuideCompany3/(?P<id>\d+)/$', views.EditGuideCompany3),
url(r'^EditSponsAbout/(?P<id>\d+)/$', views.EditSponsAbout),
url(r'^EditSponsCompany1/(?P<id>\d+)/$', views.EditSponsCompany1),
url(r'^messagetoguide/(?P<id>\d+)/(?P<id2>\d+)$', views.MessageToGuide),
url(r'^messagetostudent/(?P<id>\d+)/(?P<id2>\d+)$', views.MessageToStudent),


]