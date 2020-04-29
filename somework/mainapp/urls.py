from django.urls import include, path
from . import views
urlpatterns = [
    path('', views.homepage, name="mainapp-homepage"),
    path('adminn/', views.adminn, name="mainapp-adminn"),
    path('master/', views.master, name="mainapp-master"),
    path('report/', views.report, name="mainapp-report"),
    path('query/', views.query, name="mainapp-query"),
    path('email/', views.email, name="mainapp-email"),
]
