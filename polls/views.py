# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
import pyrebase
# Create your views here.

config = {
    "apiKey": "AIzaSyCznj3GqolK7pLJAOAkaCDfLdv9QQQ8tMo",
    "authDomain": "polls-ca153.firebaseapp.com",
    "databaseURL": "https://polls-ca153.firebaseio.com",
    "projectId": "polls-ca153",
    "storageBucket": "polls-ca153.appspot.com",
    "messagingSenderId": "104492789662"
  }
firebase=pyrebase.initialize_app(config)
db=firebase.database()
auth=firebase.auth()
storage=firebase.storage()


def vote(request):
    return render(request,"vote.html")

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
