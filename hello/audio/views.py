from django.shortcuts import render, redirect
from .models import Audio
from .forms import AudioForm
from pydub import AudioSegment
import speech_recognition as sp_re
import os
import sys
import webbrowser
import pyttsx3
from django.shortcuts import render, get_object_or_404
import ffmpeg
from django.http import FileResponse,HttpResponse



def make_audio(elem):
    hello = AudioSegment.from_file(elem.audio, format='mp4')
    hello.export("voice.wav", format='wav')


def make_text():
    r = sp_re.Recognizer()
    with sp_re.AudioFile('voice.wav') as source:
        aud = r.record(source,duration=None)
        try:
            zadanie = r.recognize_google(aud, language='ru-RU')
        except sp_re.UnknownValueError:
            zadanie = 'Речь не распознана'
    return zadanie


def home_page(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)

            order.text = 'Hello'
            order.save()

    form = AudioForm

    data = Audio.objects.all()
    for elem in data:
        make_audio(elem)
        elem.text = make_text()
        elem.save()
        print(elem.audio)

    return render(request, 'home_page.html', {'data': data, 'form': form})


def export_doc(request):

    response=HttpResponse(content_type="text/")
    response['Content-Disposition'] = 'attachment; filename=voice.doc'
    lines=[]
    voice=Audio.objects.all()
    for elem in voice:
        lines.append(f'{elem.audio.name}:{elem.text}\n\n\n')


    response.writelines(lines)
    return response

#
# def talk(words):
#     print(words)
#     engine = pyttsx3.init()
#     engine.say(words)
#     engine.runAndWait()
#
#
# talk("Привет Илья")
#
#

#
# def make_somthing(zadanie):
#     if 'скачать документ' in zadanie:
#         talk("Уже скачиваю")
#
# make_somthing(command())
