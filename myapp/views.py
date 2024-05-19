from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.


def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our Service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reailable'
    feature2.is_true = True
    feature2.details = 'Most Reailable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'support'
    feature3.is_true = False
    feature3.details = 'Excelent service'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Delivery'
    feature4.is_true = True
    feature4.details = 'Prime Delivery in one day'

    features = [feature1,feature2,feature3,feature4]
    return render(request, 'index.html',{'features': features})


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request,'counter.html',{"amount":amount_of_words})
