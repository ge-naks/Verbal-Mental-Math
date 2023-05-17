
import pyttsx3
import random
from playsound import playsound
import speech_recognition as sr
import playsound
import tkinter

engine = pyttsx3.init()
operators = ['plus', 'minus', 'times', 'divided by']

num1Addition = random.randrange(2,100)
num2Addition = random.randrange(2,100)


num1Multiplication = random.randrange(2,12)
num2Multiplication = random.randrange(2,100)

op =  random.randrange(0,4)
if op == 0:
    realans = num1Addition + num2Addition
    engine.say(num1Addition)
    engine.say(operators[op])
    engine.say(num2Addition)
elif op == 2:
    realans = num1Multiplication * num2Multiplication
    engine.say(num1Multiplication)
    engine.say(operators[op])
    engine.say(num2Multiplication)
elif op == 1:
    if num1Addition > num2Addition:
        realans = num1Addition - num2Addition
        engine.say(num1Addition)
        engine.say(operators[op])
        engine.say(num2Addition)
    else:
        realans =  num2Addition - num1Addition
        engine.say(num2Addition)
        engine.say(operators[op])
        engine.say(num1Addition)
else:
    if num2Multiplication % num1Multiplication != 0:
        while num2Multiplication % num1Multiplication != 0:
            num1Multiplication = random.randrange(2,12)
            num2Multiplication = random.randrange(2,100)
        realans =  num2Multiplication / num1Multiplication
        engine.say(num2Multiplication)
        engine.say(operators[op])
        engine.say(num1Multiplication)

engine.runAndWait() 

r = sr.Recognizer()


API_KEY = "AIzaSyAh_qQGUQ_eT7gGyHdGJwXB8MBSNCEJzRA"

def main():
    with sr.Microphone() as source:
        print("speak")
        audio = r.listen(source)
        try:
            answer = r.recognize_google(audio)
            
        except Exception as e:
            print("error:" + str(e))

    print(answer)
    if int(answer) == realans:
        print("correct")
        playsound.playsound('right.wav')
        engine.runAndWait() 
    else:
        print("wrong dummy")
        playsound.playsound('wrong.wav')
        engine.runAndWait() 
main()


