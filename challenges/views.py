from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

monthly_challenges = {
    "january": "Eat no fast food",
    "february": "walk atlest 20 min",
    "march": "learn Django 20 min",
    "april": "increse good work",
    "may": "They avoid debt",
    "june": "emergency funds",
    "july": "invest",
    "august": "utilize tax deductions",
    "septermber": "income streams",
    "october": "start saving for their kids college early on",
    "november": "seek advice",
    "december": "reading book"

}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    return HttpResponse(monthly_challenges[months[month]])


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
