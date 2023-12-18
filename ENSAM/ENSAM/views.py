from PyPDF2 import PdfReader

from django.http import HttpResponseRedirect, HttpResponse
from django.http import FileResponse, Http404
from django.conf import settings
import os
from django.shortcuts import render, redirect
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from django.views.generic import TemplateView
from xhtml2pdf import pisa
from app.models import *


def ent(request):
    return HttpResponseRedirect('https://ent.univh2c.ma/uPortal/f/welcome/normal/render.uP')


def mooc_universite(request):
    return HttpResponseRedirect('https://ent.univh2c.ma/uPortal/f/welcome/normal/render.uP')


def home(request):
    return redirect('/index/')


def lire_pdf(request):
    file_path = os.path.join(settings.STATIC_ROOT, 'assets', 'reglement.pdf')
    return render(request, 'afficher_pdf.html', {'file_path': file_path})


def index(request):
    slide = Slide.objects.all()
    print(slide)
    # type=Article_type.objects.filter(name='Communiqués Officiels')
    # com_off = Article.objects.filter(Article_type_id=type)
    return render(request, 'index.html', {'slide': slide})


def afficher(request, article_id):
    article = Article.objects.filter(id=article_id)
    return render(request, 'afficher.html', {'article': article})
