from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

class NosotrosPageView(TemplateView):
    template_name ="nosotros.html"


    def get(self,request,*args, **kwargs):
      return render(request, self.template_name, {'TituloEjemplo': 'Ejempo'})
