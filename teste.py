#!/usr/bin/env python3

import speech_recognition as sr
# get audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Diga algo :")
    audio = r.listen(source)

try:
    print("Você disse : " + r.recognize_google(audio, language='pt-BR'))
except sr.UnknownValueError:
    print("Não consegui te entender ")
except sr.RequestError as e:
    print("vc esta offline; {0}".format(e))

    print('Olá Git')
