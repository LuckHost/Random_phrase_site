from django.shortcuts import render
from main.models import Words

# Create your views here.
def main_page(request):
    words = Words.objects.all()
    return render(request, 'main/main_page.html', {'data': words})

def add_words(request):
    return render(request, 'main/adding_page.html')