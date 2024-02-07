from django.shortcuts import render
from main.models import Words
from .forms import MainpageCheckbox
from django.http import HttpResponseRedirect

# Create your views here.
def main_page(request):
    words = Words.objects.all()
    print = False
    if request.method == "POST":
        form = MainpageCheckbox(request.POST)
        if form.is_valid():
            if request.POST["is_funny"]:
                print = True
            else:
                print = False
    else:
        form = MainpageCheckbox()
    return render(request, 'main/main_page.html', {'data': words, 'form': form, 'print': print})

def add_words(request):
    return render(request, 'main/adding_page.html')