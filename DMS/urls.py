

from django.urls import path
from DMS import views

urlpatterns = [
    path('',views.showHome),
    path('adddepart',views.addDepart),
    path('delete/<int:departid>',views.Deletedepart),
    path('update/<int:departid>',views.Updatedepart),


]
