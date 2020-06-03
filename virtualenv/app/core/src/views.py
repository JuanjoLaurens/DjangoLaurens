from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage


class HomePageView(TemplateView):

    template_name = "index.html"

   # def get_context_data(self, **kwargs):
      #  context = super().get_context_data(**kwargs)
      #  context['TituloIni'] = "Hola que hace"
      #  context['Titulo2'] = "Otro titutlo "
      #  return context
   

    def get (self,request,*args, **kwargs):
        return render(request, self.template_name, {'TituloIni': 'Juan Laurens Wehousinn'})



def contacto(request):
      formContact = ContactForm()
      #validad formulario

      if request.method == "POST":
        formContact = ContactForm(data=request.POST)
        if formContact.is_valid():
            tipomsj = request.POST.get('tipomsj','')
            nombre = request.POST.get('nombre','')
            apellido = request.POST.get('apellido','')
            correo = request.POST.get('correo','')
            mensaje = request.POST.get('mensaje','')


          # objetos de las variables

            email = EmailMessage(
              "WeHousinn: tienes un nuevo mensaje",
              "De {} {} <{}>\n\nEscribio:\n\n{}".format(nombre, apellido, correo, mensaje),
              "no-contestar@inbox.mailtrap.io",
              ["16rusherlaurens@gmail.com"],
              reply_to=[correo]


             )
            #enviar correo
            try:
              email.send()
              return redirect(reverse('contacto')+"?ok")


            except:
              return redirect(reverse('contacto')+"?fail")  


            



      return render(request, 'contacto.html' ,{'formulario': formContact})
