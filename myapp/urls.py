from django.urls import path
from . import views

urlpatterns = [ 

    path('main' ,views.main , name='main'),
    path('', views.main , name='main'),
    path('portfolio',views.portfolio, name='portfolio'),
    path('developers',views.save_email, name='developers'),
    path('success' , views.success , name='success')
    
]    