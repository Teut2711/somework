from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .forms import EmailForm, MasterForm
    
# Create your views here.

from .backend.mailer import emailpy
from .backend.master import nsdl, cdsl


def homepage(request):
    return render(request, 'mainapp/index.html')


def adminn(request):
    return render(request, 'mainapp/adminn.html')

def master(request):
    if request.method == 'POST':
        form = MasterForm(request.POST, request.FILES)
        if form.is_valid():
            if request.POST['hidden'] == 'nsdlbenpos':
                nsdl.main(request.FILES["filepath"])
            else:
                cdsl.main(request.FILES["filepath"])

            
    else:
        form = MasterForm()
    
    return render(request, 'mainapp/master.html', {"form":form})


def report(request):
    return render(request, 'mainapp/report.html')


def query(request):
    return render(request, 'mainapp/query.html')


def email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            emailpy.main(*list(map(lambda x:request.POST.get(x).strip(), 
                                  ['host','emailaddress','password'])), 
                        request.FILES["filepath"])

            
    else:
        form = EmailForm()
    
    return render(request, 'mainapp/email.html', {"form":form})
