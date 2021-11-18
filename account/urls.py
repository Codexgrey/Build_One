from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.user_accounts)
]
