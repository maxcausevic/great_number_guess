from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1,100)
    number = request.session['number']
    context ={
            "guess" : ""
        } 
    if request.method == "POST":
        guess_from_form = int(request.POST['guess'])
        too_high = "too high!"
        too_low = "too low!"
        correct = (f"{guess_from_form} is the right guess")
    
        if guess_from_form > number:
            context = {
                'guess':too_high
        }
        elif guess_from_form < number:
            context ={
                'guess' : too_low
            }
        else:
            context = {
                'guess' : correct
            }
    return render(request,'index.html', context)

def destroy(request):
    del request.session['number']
    return redirect('/')
