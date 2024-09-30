from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# sending the dynamic data to view 
def index(request):
    context={
        'name':'vivek',
        'age':22,
        'nationality':'indian',
    }
    return render(request,'index.html',context)

def counter(request):
    text=request.GET['text']
    amount_of_word=len(text.split())
    print(amount_of_word)
    return render(request,'counter.html',{'amount':amount_of_word})