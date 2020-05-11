from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
#def index1(request):
#    return render(request,'index1.html')

#def Subjects(request):
 #   return render(request,'Subjects.html')
class index1(TemplateView):
    template_name = "index1.html"


class Subjects(TemplateView):
    template_name = "Subjects.html"

class List(TemplateView):  
    
    template_name = "List.html" 

class Ide(TemplateView):  
    
    template_name = "Ide.html" 