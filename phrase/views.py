
from django.shortcuts import render
from django.http import HttpResponse
from .phrase import generate_text
from django.views.decorators.csrf import csrf_exempt
from django import forms



@csrf_exempt
def phrasemaking(request):
    if request.method == 'POST':        
        prompt = request.POST.get('text', '')          
        generated_text = generate_text(prompt)  
        return render(request, 'phrasemaking.html', {'output': generated_text, 'input_text': prompt})
    else:
        return render(request, 'phrasemaking.html', {'output': '', 'input_text': ''})