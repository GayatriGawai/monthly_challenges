from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), # handles /challenges/
    # <str:month> suggests that entered value should be considered and converted into a string
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge, name="month-challenge")
]
