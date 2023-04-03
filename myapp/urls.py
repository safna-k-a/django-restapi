from django.urls import include, path
from myapp import views

urlpatterns = [
    path('',views.Home,name="Home"),
    path('emplist',views.emplist,name="emplist"),
    path('add_items/',views.add_items,name="add_items"),
    path('delete_items/<int:pk>',views.delete_items),
    path('update_items/<int:pk>',views.update_items),
    path('my', views.my_api_view, name='my_api_view')
]