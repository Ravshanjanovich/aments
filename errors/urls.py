from django.urls import path
from errors.views import error_404


urlpatterns = [
    path('', error_404, name='error_404')
]