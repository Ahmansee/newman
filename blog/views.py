from django.shortcuts import render, redirect
from .models import Contact
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def info(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
           
            
    else:
        form = UserCreationForm()   
        '''
        fullname = request.POST.get('fname')
        emailads = request.POST.get('ename')
        message  = request.POST.get('mname')
        

        contactmail = Contact(name=fullname, email=emailads, sms=message)
        contactmail.save()
        '''
    return render(request, 'blog/contact.html',{'form':form})


def catagory(request):
    return render(request, 'blog/catagory.html')

def singleblog(request):
    return render(request, 'blog/single-blog.html')