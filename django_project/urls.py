
from django.urls import path
from portfolio_app import views as portfolio_views

urlpatterns = [
    path('api/contact/', portfolio_views.contact_form, name='contact_api'),
]
