from django.shortcuts import render
from .models import Contact
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def index(request):
    return  render(request,'home.html')

def contact(request):
    return  render(request,'contact.html')

def about(request):
    return  render(request,'about.html')

def products(request):
    return  render(request,'products.html')

def save(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name =='':
            data = {'state':'false','message':'Please enter  Name','id':'name'}
            return JsonResponse(data)
        if name.isnumeric():
            data = {'state':'false','message':'Please enter valid Name','id':'name'}
            return JsonResponse(data)
        else:
            email = request.POST.get('email')
            if email =='':
                data = {'state':'false','message':'Please enter valid email','id':'email'}
                return JsonResponse(data)
            else:
                phone = request.POST.get('phone')
                if not phone.isnumeric():
                    data = {'state':'false','message':'Please enter valid phone number'}
                    return JsonResponse(data)
                else:
                    subject = request.POST.get('subject')
                    if subject =='':
                        data = {'state':'false','message':'Please enter Subject'}
                        return JsonResponse(data)
                    else:
                        message = request.POST.get('message')
                        if message =='':
                            data = {'state':'false','message':'Please enter message'}
                            return JsonResponse(data)
                        else:
                            obj = Contact(name=name,email=email,phone=phone,subject=subject,message=message)
                            obj.save()
                            data = {'state':'true','message':'Form Submitted Successfully...'}
                            return JsonResponse(data)

    
