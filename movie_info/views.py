from django.shortcuts import render
from django.views.generic import TemplateView

class Test(TemplateView):
    template_name = 'product/test.html'

class Thanks(TemplateView):
    template_name = 'product/thank.html'