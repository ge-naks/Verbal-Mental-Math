
import pyttsx3
import random
from playsound import playsound
import speech_recognition as sr
import playsound
import time


t = 10
numCorrect = 0
numIncorrect = 0
r = sr.Recognizer()
engine = pyttsx3.init()
operators = ['plus', 'minus', 'times', 'divided by']
engine.setProperty('rate', 200)
global test
test = -2
answer = -1


def genNumber():
    
    num1Addition = random.randrange(2,100)
    num2Addition = random.randrange(2,100)

    num1Multiplication = random.randrange(2,12)
    num2Multiplication = random.randrange(2,100)

    op =  random.randrange(0,4)
    if op == 0:  
        global test
        test = num1Addition + num2Addition
        engine.say(num1Addition)
        engine.say(operators[op])
        engine.say(num2Addition)
        
    elif op == 2:
        test = num1Multiplication * num2Multiplication
        engine.say(num1Multiplication)
        engine.say(operators[op])
        engine.say(num2Multiplication)
    elif op == 1:
        if num1Addition > num2Addition:
            test = num1Addition - num2Addition
            engine.say(num1Addition)
            engine.say(operators[op])
            engine.say(num2Addition)
            
        else:
            test = num2Addition - num1Addition
            engine.say(num2Addition)
            engine.say(operators[op])
            engine.say(num1Addition)
            
    else:
        if num2Multiplication % num1Multiplication != 0:
            while num2Multiplication % num1Multiplication != 0:
                num1Multiplication = random.randrange(2,12)
                num2Multiplication = random.randrange(2,100)
            test = num2Multiplication / num1Multiplication
            engine.say(num2Multiplication)
            engine.say(operators[op])
            engine.say(num1Multiplication)
            
    engine.runAndWait() 

def listen():
    with sr.Microphone() as source:
        print("speak")
        audio = r.listen(source)
        try:
            global answer 
            answer = r.recognize_google(audio)
        except Exception as e:
            print("error:" + str(e))

def main():
    genNumber()
    listen()
    if int(test) == int(answer):
        print("correct")
        numCorrect = +1
    else:
        print("wrong dummy")
        numIncorrect = +1

def normalizeAudio():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise()

duration = 10

start_time = time.time()
end_time = start_time + duration


def start():
    while time.time() < end_time:
        main()
        elapsed_time = time.time() + start_time
        time.sleep(max(0, duration - elapsed_time))

start()



