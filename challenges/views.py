from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse




monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for at least 20 minutes everyday",
    "march": "Learn Django for at least 20 minutes everyday",
    "april": "Read for 15 minutes every day",
    "may": "Try a new recipe every week",
    "june": "Go outside and enjoy nature at least once a week",
    "july": "Spend 30 minutes every day improving a new skill",
    "august": "Practice mindfulness or meditation for 10 minutes daily",
    "september": "Declutter one part of your home each week",
    "october": "Complete a creative project by the end of the month",
    "november": "Write a journal entry about your progress each week",
    "december": None
}

# Create your views here.

def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html',{
        "months":months,
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month-1]
    redirect_path = reverse(
        "month-challenge", args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
       
        return render (request,"challenges/challenge.html",{
            "text": challenge_text,
            "month":month.capitalize()
        })
    except:
        raise Http404()
