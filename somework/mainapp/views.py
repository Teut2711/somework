from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .forms import UploadFileForm
    
# Create your views here.

from .backend.mailer import mailer

def homepage(request):
    return render(request, 'mainapp/index.html')


def adminn(request):
    return render(request, 'mainapp/adminn.html')


def master(request):
    return render(request, 'mainapp/master.html')


def report(request):
    return render(request, 'mainapp/report.html')


def query(request):
    return render(request, 'mainapp/query.html')


def email(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            mailer.main(*list(map(lambda x:request.POST.get(x).strip(), 
                                  ['host','emailaddress','password'])), 
                        request.FILES["filepath"])

            
    else:
        form = UploadFileForm()
    
    return render(request, 'mainapp/email.html', {"form":form})
