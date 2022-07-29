from django.shortcuts import render
import pandas as pd

# Create your views here.
def index(request):
    return render(request,'index.html')


def result(request):    
    f = pd.read_csv("trending_score.csv",encoding= 'unicode_escape')

    geeks_object = f.to_html()
    params={'geek': geeks_object}

    return render(request, 'result.html',params)

def home(request):
    return render(request,'home.html')


def final_product(request):
    f = pd.read_csv("product.csv",encoding= 'unicode_escape')

    geeks_object = f.to_html()
    params={'geek': geeks_object}

    return render(request, 'final_product.html',params)