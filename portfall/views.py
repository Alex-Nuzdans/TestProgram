from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):
    P=Project.objects.all()
    return render(request,'portfall/home.html',{'P':P})
