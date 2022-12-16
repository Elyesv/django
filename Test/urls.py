from django.urls import path
from . import views

app_name = 'Test'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/<id>', views.show, name='show'),
    path('delete/<id>', views.delete, name='delete'),
    path('create',views.create, name="create"),
    path('update/<id>', views.update, name="update")
    
]
