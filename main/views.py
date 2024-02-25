from django.shortcuts import render
from main.models import Allwords, Rusnounsmorfs
import random

def main_page(request):
    return render(request, 'main/main_page.html')

def add_words(request):
    return render(request, 'main/adding_page.html')

def result_output(request):
    if request.method == 'POST':
        words_base = Allwords.objects
        words_nouns = Rusnounsmorfs.objects
        
        words = request.POST.getlist('checkboxes')
        if "male" in words:
            words_nouns = words_nouns.filter(gender='муж')
        elif "fem" in words:
            words_nouns = words_nouns.filter(gender='жен')
        elif "neut" in words:
            words_nouns.filter(gender='ср')
               
        if "alive" in words:
            words_nouns = words_nouns.filter(soul=1)
        else:
            words_nouns = words_nouns.filter(soul=0)
            
        output = []
        
        output.append(random.choice(words_nouns.filter(wcase="им")))
        output.append(random.choice(words_nouns.filter(wcase="род")))
        
        output.append(random.choice(words_base.filter(type="гл").filter(perfect=1).filter(vozv=0).filter(gender=output[0].getGender())))
        output.append(random.choice(words_base.filter(type="прл").filter(wcase="вин").filter(soul=1).filter(plural=output[1].getPlural())))
        
        output = [output[0], output[2], output[3], output[1]]
        
        
            
    return render(request, 'main/result_output.html', {"data": output})