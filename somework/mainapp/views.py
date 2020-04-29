from django.shortcuts import render

# Create your views here.


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
    if request.method == "POST":
        print(request.FILES["filename"], request.FILES)
    
    return render(request, 'mainapp/email.html')
