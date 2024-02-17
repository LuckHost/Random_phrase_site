from django.shortcuts import render
from main.models import Rusnounsmorfs
from .forms import MainpageCheckbox

def main_page(request):
    return render(request, 'main/main_page.html')

def add_words(request):
    return render(request, 'main/adding_page.html')

def result_output(request):
    if request.method == 'POST':
        words_base = Rusnounsmorfs.objects.all()
        words = request.POST.getlist('checkboxes')
        if "male" in words:
            words_base = words_base.filter(gender='муж')
        else:
            words_base = words_base.filter(gender='жен')
            
        if "alive" in words:
            words_base = words_base.filter(soul=1)
        else:
            words_base = words_base.filter(soul=0)
            
        output = []
        for i in range(43, 43 + 10):
            output.append(words_base[i])
         
    form = MainpageCheckbox()
    return render(request, 'main/result_output.html', {"data": output})