from django.shortcuts import render
from main.models import Words
from .forms import MainpageCheckbox
from django.http import HttpResponseRedirect

# Create your views here.
def main_page(request):
    return render(request, 'main/main_page.html')

def add_words(request):
    return render(request, 'main/adding_page.html')

def result_output(request):
    if request.method == 'POST':
        words_base = Words.objects.all()
        words = request.POST.getlist('checkboxes')
        if "funny" in words:
            words_base = words_base.filter(mood_type='fun')
        else:
            words_base = words_base.filter(mood_type='sad')
            
        if "animal" in words:
            words_base = words_base.filter(alive=True)
        else:
            words_base = words_base.filter(alive=False)
         
    form = MainpageCheckbox()
    return render(request, 'main/result_output.html', {"data": words_base})