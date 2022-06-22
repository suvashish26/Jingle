import speech_recognition as sr # this helps jingle listen to me
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer() #listens ur voice
engine = pyttsx3.init()
voices = engine.getProperty('voices') # getting all the possible voices
engine.setProperty('voice', voices[1].id)

# here we are calling the talk function and it will say whatever the parameter we are passing
def talk(text):
    engine.say(text)
    engine.runAndWait()
     
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening right now...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice) #we will pass the audio to the google and google will give the text
            command = command.lower()
            if 'jingle' in  command: #if user says jingle then only it recognizes
                commmand = command.replace('jingle', '') # alexa will be removed
                print(command) # returns the porameter we've passed to the function
            #using microphone as source and call speech recongnizer to listen to this source
    except:
        pass
    return command  # it returns the command from us 
def run_jingle():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        t= datetime.datetime.now().strftime('%I:%M %p')
        print(t)
        talk('The time right now is' + t)  
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'what is' in command:
        topic = command.replace('what is', '')
        info_second = wikipedia.summary(topic, 1)
        print(info_second)
        talk(info_second)
    elif 'name' and "hello" in command:
        talk("Namaste, I am jingle, your new assistant")
    elif 'beautiful' in command:
        talk("Awww, thats really cute")
    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())
    elif "not funny" in command:
        talk(' sorry to dissapoint you')
    elif "that was a good one" in command:
        talk(" Its nice you liked it hehe")
    else:
        talk("Sorry I could not hear you")

while True: # running in loop
    run_jingle()
