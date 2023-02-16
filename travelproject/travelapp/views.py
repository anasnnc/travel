from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,'index.html',{'result':obj,'res':obj1})

# def about(request):
#     return render(request,'about.html')
#
# def contact(request):
#     return render(request,'contact.html')
#
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})