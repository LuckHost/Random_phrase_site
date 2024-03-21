from django.shortcuts import render
from main.models import Allwords, Rusnounsmorfs
import random
import wikipedia
import asyncio

def main_page(request):
    return render(request, 'main/main_page.html')

def add_words(request):
    return render(request, 'main/adding_page.html')

def get_explanations(sentence):
    explanation = {}
    wikipedia.set_lang("ru")
    for i in sentence:
        try:
            wiki_answer = wikipedia.summary(i, sentences=6)
            explanation |= {"word": i}
            explanation |= {"wiki_answer": wiki_answer}
            return explanation
        except:
            pass

def result_output(request):
    if request.method == 'POST':  
        words_base = Allwords.objects
        words_nouns = Rusnounsmorfs.objects
        words_nouns = words_nouns.filter(soul=1)
        
        gender_choise = request.POST.getlist('gender_choise')
        if "male" in gender_choise:
            words_nouns = words_nouns.filter(gender='муж')
        elif "fem" in gender_choise:
            words_nouns = words_nouns.filter(gender='жен')
        elif "neut" in gender_choise:
            words_nouns.filter(gender='ср')
            
        """
        
        First sentence structure:
        noun (main), 
        verb (main, describes what the main noun did to the second one), 
        adjective (describes the object on which the action was performed), 
        noun (on which the action is performed)
        
        Example:
        сопровождающий зашпионил афганского бытовика
        
        """    
        firts_sentence = []
        firts_sentence.append(random.choice(words_nouns.filter(wcase="им")))
        firts_sentence.append(random.choice(words_nouns.filter(wcase="род")))
        firts_sentence.append(random.choice(words_base.filter(type="гл").filter(perfect=1).filter(vozv=0).filter(gender=firts_sentence[0].getGender())))
        firts_sentence.append(random.choice(words_base.filter(type="прч").filter(wcase="вин").filter(soul=1).filter(nakl='страд').filter(plural=firts_sentence[1].getPlural())))
        firts_sentence = [firts_sentence[0], firts_sentence[2], firts_sentence[3], firts_sentence[1]]
        
        explanations = get_explanations(firts_sentence)

    return render(request, 'main/result_output.html', {"data": firts_sentence, "explanations": explanations})