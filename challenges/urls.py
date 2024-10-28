from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.monthly_challenge_by_number,
         name="monthly-challenge-by-number"),
    path("<str:month>", views.monthly_challenge, name="monthly-challenge")

]
