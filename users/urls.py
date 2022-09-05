from django.urls import path
from . import views

urlpatterns = [
    path('login/', view=views.login_api),
    path('user/', view=views.get_user_data)
]
