from tkinter import *                              # THIS LIBRARY IS USED TO BUILD THE GRAPHICAL USER INTERFACE
import serial                                      # THIS LIBRARY IS USED TO SET COMMUNICATION BETWEEN ARDUINO AND PYTHON
import time                                        # THIS LIBRARY IS USED TO SET DELAY TIME
import pyttsx3                                     # THIS LIBRARY IS USED TO MAKE OUR PROGRAM TO SPEAK
arduinoData = serial.Serial('com6',9600)           # SETTING UP PORT NUMBER OF ARDUINO
arduinoData.timeout = 1

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')              # SETTING UP TYPE OF VOICE AND OTHER PARAMETERS FOR SPEAKING
engine.setProperty('voice',voices[0].id)
def speak(audio):                                  # FUNCTION TO SPEAK A PARTICULAR LINE
    engine.say(audio)
    engine.runAndWait()

def redon():                                       # THIS FUNCTION WILL BE EXECUTED WHEN WE CLICK ON (RED COLOUR ON) BUTTON
    speak("switching on red colour")               # FIRST IT WILL SPEAK THIS LINE BY USING SPEAK FUNCTION  
    led = ("red on")                               # IN LED KEYWORD WE WILL PUT (RED ON) COMMAND 
    arduinoData.write(led.encode())                # NOW THIS VALUE(RED ON) WILL BE SEND TO ARDUINO AND ARDUINO WILL EXECUTE ALL THE COMMANDS RELATED TO IT
    time.sleep(0.5)                                # THIS SLEEP TIME IS GIVEN SO THAT ARDUINO AND PYTHON WILL WORK PROPERLY WITHOUT ANY ERRORS 
    print(arduinoData.readline().decode('ascii'))  # WHEN THE COMMAND WILL BE EXECUTED THE ARDUINO WILL SEND THE COMMAND THAT IT HAS DONE THE GIVEN TASK
    

def blueon():
    speak("switching on blue colour")
    led = ("blue on")
    arduinoData.write(led.encode())       # ALL THE FUNCTIONS WILL WORK IN THE SAME WAY AS ABOVE
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def greenon():
    speak("switching on green colour")
    led = ("green on")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def redoff():
    speak("switching off red colour")
    led = ("red off")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def blueoff():
    speak("switching off blue colour")
    led = ("blue off")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def greenoff():
    speak("switching off green colour")
    led = ("green off")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def whiteon():
    speak("switching on white colour")
    led = ("white on")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def whiteoff():
    speak("switching off white colour")
    led = ("white off")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def mergentaon():
    speak("switching on mergenta colour")
    led = ("mergenta on")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def mergentaoff():
    speak("switching off mergenta colour")
    led = ("mergenta off")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def cyanon():
    speak("switching on cyan colour")
    led = ("cyan on")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def cyanoff():
    speak("switching off cyan colour")
    led = ("cyan off")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def lemonon():
    speak("switching on lemon green colour")
    led = ("lemon green on")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))

def lemonoff():
    speak("switching off lemon green colour")
    led = ("lemon green off")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))


def allcolouron():
    speak("switching on all colours")
    led = ("all colours")
    arduinoData.write(led.encode())
    time.sleep(0.5)
    print(arduinoData.readline().decode('ascii'))


window = Tk()
window.title("LED BUTTON")                       # GIVING TITLE TO THE GRAPHICAL USER INTERFACE WINDOW 
window.geometry("350x760")                       # SETTING UP DIMENSIONS OF THE GUI
window.configure(bg = 'yellow')                  # SETTING UP BACKGROUND COLOUR OF THE INTERFACE

button1 = Button(window,text = 'RED ON')         # CREATING A BUTTON AND PUTTING UP A TEXT(RED ON) ON THAT BUTTON
button1.config(command = redon)                  # WHEN THE BUTTON WILL BE CLICKED THE IT WILL AUTOMATICALLY EXECUTE REDON FUNCTION 
button1.config(font =('Ink free',20,'bold'))     # SETTING UP FONT STYLE AND SIZE
button1.config(bg='#fc0303')                     # SETTING UP BACKGROUND COLOUR OF BUTTON 
button1.config(fg='#ffffff')                     # SETTING UP BUTTON TEXT COLOUR
button1.config(state=ACTIVE)                     # MAKING THIS BUTTON TO BE IN ACTIVE STATE
button1.config(activebackground='#fc0303')       # BY EXECUTING THIS COMMAND THE COLOUR OF BUTTON WILL BE IN ACTIVE STATE FROM THE STARTING
button1.config(activeforeground = '#ffffff')     # BY EXECUTING THIS COMMAND THE COLOUR OF BUTTON TEXT WILL BE IN ACTIVE STATE FROM THE STARTING

button2 = Button(window,text = 'BLUE ON')
button2.config(command = blueon)
button2.config(font =('Ink free',20,'bold'))
button2.config(bg='#1205ff')
button2.config(fg='#ffffff')       # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button2.config(state=ACTIVE)
button2.config(activebackground='#1205ff')
button2.config(activeforeground = '#ffffff')


button3 = Button(window,text = 'GREEN ON')
button3.config(command = greenon)
button3.config(font =('Ink free',20,'bold'))
button3.config(bg='#09ff05')
button3.config(fg='#ffffff')        # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button3.config(state=ACTIVE)
button3.config(activebackground='#09ff05')
button3.config(activeforeground = '#ffffff')

button4 = Button(window,text = 'CYAN ON')
button4.config(command = cyanon)
button4.config(font =('Ink free',20,'bold'))
button4.config(bg='#00FFFF')
button4.config(fg='#ffffff')         # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button4.config(state=ACTIVE)
button4.config(activebackground='#00FFFF')
button4.config(activeforeground = '#ffffff')

button5 = Button(window,text = 'LEMON GREEN ON')
button5.config(command = lemonon)
button5.config(font =('Ink free',20,'bold'))
button5.config(bg='#adf802')
button5.config(fg='#ffffff')         # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button5.config(state=ACTIVE)
button5.config(activebackground='#adf802')
button5.config(activeforeground = '#ffffff')

button6 = Button(window,text = 'WHITE ON')
button6.config(command = whiteon)
button6.config(font =('Ink free',20,'bold'))
button6.config(bg='#ffffff')
button6.config(fg='#020302')          # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button6.config(state=ACTIVE)          
button6.config(activebackground='#ffffff')
button6.config(activeforeground = '#020302')

button13 = Button(window,text = 'ALL COLOURS ON')
button13.config(command = allcolouron)
button13.config(font =('Ink free',20,'bold'))
button13.config(bg='#ffffff')
button13.config(fg='#020302')          # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button13.config(state=ACTIVE)         
button13.config(activebackground='#ffffff')
button13.config(activeforeground = '#020302')


button7 = Button(window,text = 'RED OFF')
button7.config(command = redoff)
button7.config(font =('Ink free',20,'bold'))
button7.config(bg='#ffffff')
button7.config(fg='#fc0303')           # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1 
button7.config(state=ACTIVE)
button7.config(activebackground='#ffffff')
button7.config(activeforeground = '#fc0303')


button8 = Button(window,text = 'BLUE OFF')
button8.config(command = blueoff)
button8.config(font =('Ink free',20,'bold'))
button8.config(bg='#ffffff')
button8.config(fg='#1205ff')           # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button8.config(state=ACTIVE)
button8.config(activebackground='#ffffff')
button8.config(activeforeground = '#1205ff')


button9 = Button(window,text = 'GREEN OFF')
button9.config(command = greenoff)
button9.config(font =('Ink free',20,'bold'))
button9.config(bg='#ffffff')
button9.config(fg='#09ff05')            # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button9.config(state=ACTIVE)
button9.config(activebackground='#ffffff')
button9.config(activeforeground = '#09ff05')


button10 = Button(window,text = 'CYAN OFF')
button10.config(command = cyanoff)
button10.config(font =('Ink free',20,'bold'))
button10.config(bg='#ffffff')
button10.config(fg='#00FFFF')            # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button10.config(state=ACTIVE) 
button10.config(activebackground='#ffffff')
button10.config(activeforeground = '#00FFFF')


button11 = Button(window,text = 'LEMON GREEN OFF')
button11.config(command = lemonoff)
button11.config(font =('Ink free',20,'bold'))
button11.config(bg='#ffffff')
button11.config(fg='#adf802')             # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button11.config(state=ACTIVE)
button11.config(activebackground='#ffffff')
button11.config(activeforeground = '#adf802')

button12 = Button(window,text = 'WHITE OFF')
button12.config(command = whiteoff)
button12.config(font =('Ink free',20,'bold'))
button12.config(bg='#ffffff')
button12.config(fg='#020302')              # ALL THESE COMMAND WILL WILL WORK IN THE SAME WAY AS THEY ARE WORKING WITH BUTTON 1
button12.config(state=ACTIVE)            
button12.config(activebackground='#ffffff')
button12.config(activeforeground = '#020302')


button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()                              # MAKING ALL THESE BUTTON VISIBLE ON THE GUI WINDOW
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
button12.pack()
button13.pack()
window.mainloop()                           # MAINLOOP() MUST BE CALLED FOR WINDOW TO BE DRAWN AND EVENTS TO BE PROCESSED