from django.shortcuts import render
from main.models import Words
from .forms import MainpageCheckbox

# Create your views here.
def main_page(request):
    words = Words.objects.all()
    if request.method == "POST":
        form = MainpageCheckbox(request.POST)
        if form.is_valid():
            pass
    
    else:
        form = MainpageCheckbox()
    return render(request, 'main/main_page.html', {'data': words})

def add_words(request):
    return render(request, 'main/adding_page.html')