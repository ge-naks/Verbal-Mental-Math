
import pyttsx3
import random
import pyaudio
import requests
import json
import time
import wave
import sys



engine = pyttsx3.init()

p = pyaudio.PyAudio()
stream = p.open(
    frames_per_buffer= 3200,
    rate=16000,
    format= pyaudio.paInt16,
    channels= 1,
    input= True,

)


operators = ['plus', 'minus', 'times', 'divided by']
for i in range(0,4):
    num1Addition = random.randrange(2,100)
    num2Addition = random.randrange(2,100)


    num1Multiplication = random.randrange(2,12)
    num2Multiplication = random.randrange(2,100)

    op =  random.randrange(0,4)
    if op == 0:
        engine.say(num1Addition)
        engine.say(operators[op])
        engine.say(num2Addition)
    elif op == 2:
        engine.say(num1Multiplication)
        engine.say(operators[op])
        engine.say(num2Multiplication)
    elif op == 1:
        if num1Addition > num2Addition:
            engine.say(num1Addition)
            engine.say(operators[op])
            engine.say(num2Addition)
        else:
            engine.say(num2Addition)
            engine.say(operators[op])
            engine.say(num1Addition)
    else:
        if num2Multiplication % num1Multiplication != 0:
            while num2Multiplication % num1Multiplication != 0:
                num1Multiplication = random.randrange(2,12)
                num2Multiplication = random.randrange(2,100)
            engine.say(num2Multiplication)
            engine.say(operators[op])
            engine.say(num1Multiplication)

engine.runAndWait()
