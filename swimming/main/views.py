from django.shortcuts import render, redirect
from workouts.models import Workouts_gym, Workouts_swimming, Workouts_swimming_pro, Registrations
from workouts.forms import RegistrationsForm


def parse(full_text : list, info : set):
    for elem in full_text:
        shit = elem[-1][-2:]
        for el in elem:
            if shit in el:
                elem[-1] = el.split(shit)[0]

    for elem in range(len(info)):
        info[elem]['full_text'] = full_text[elem]

    return info

def base(request):
    return render(request, 'main/base.html')

def about_swimming(request):
    return render(request, 'about_swimming/about_swimming.html')

def about_me(request):
    return render(request, 'about_me/about_me.html')

def registration(request):
    error = {}
    if request.method == 'POST':
        form = RegistrationsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registration/success.html')
        else:
            for field in form.errors:
               error[field]=form.errors[field].as_text()

    form = RegistrationsForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'registration/reg.html', data)

def workout_gym(request):
    text = []
    info =  Workouts_gym.objects.values()
    for elem in info.values():
        sent = str(elem).split("'full_text': '")[1]
        res = sent.split('\\r\\n')
        text.append(res)

    return render(request, 'workouts/workout_gym.html', {'info' : parse(text, info)})

def workout_swimming(request):
    text = []
    info =  Workouts_swimming.objects.values()
    for elem in info.values():
        sent = str(elem).split("'full_text': '")[1]
        res = sent.split('\\r\\n')
        text.append(res)    
    return render(request, 'workouts/workout_swimming.html', {'info' : parse(text, info)})

def workouts_swimming_pro(request):
    text = []
    info =  Workouts_swimming_pro.objects.values()
    for elem in info.values():
        sent = str(elem).split("'full_text': '")[1]
        res = sent.split('\\r\\n')
        text.append(res)    
    return render(request, 'workouts/workout_swimming_pro.html', {'info' : parse(text, info)})