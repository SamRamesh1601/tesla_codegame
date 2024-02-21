# Required package installation command:
# pip install pyttsx3 playsound

from playsound import playsound
import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return True

print("Welcome to Tesla Code Game")
speak("Welcome to Tesla Code Game")
print("Your Commands are my life")
print("")
print('You are Driving a Tesla CAR')
print("")

user_check = True

def wishme(user):
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak(user)
        speak("Good morning")
        print("Good morning", user.upper())
    elif 12 <= hour < 17:
        speak(user)
        speak("Good Afternoon")
        print("Good Afternoon", user.upper())
    elif 17 <= hour < 20:
        speak(user)
        speak("Good Evening")
        print("Good Evening", user.upper())
    else:
        speak(user)
        speak("Good Night")
        print("Good Night", user.upper())

user = input("Your Name: ").lower()
wishme(user)
print("")

commend = ['start', 'stop', 'inspeed', 'despeed', 'w', 's', 'a', 'd', 'help', 'tesla', 'time', 'play', 'playfm']
print("Checking User matching...")
print("")

while True:
    if user in commend:
        print("Please change userName this Tesla commend")
        speak("Please change userName this Tesla commend")
        user = input("Enter Name: ")
        print("Updated the user_name successfully", user.upper())
        if user == 'tesla':
            print("Process of checking the user_name to enjoy ride")
            print("Thank you - Tesla")
            break
    else:
        break

print("")
user_pass = int(input("Enter Your Passcode: "))
print("")

it = ""
count = 0
uturn = True
speed = False
started = False
exit = True
score = 0

def lock():
    playsound("carlock.mp3")

def takingoff():
    playsound('takingoff.mp3')

def start():
    playsound('carstart.mp3')

def play():
    playsound("vili.mp3")

def play1():
    playsound("no.wav")

def car_alarm():
    playsound('caralarm.mp3')

playsound('E:\\PYTHON\\Tesla\\cardoor.mp3')
wishme(user)

while exit:
    print("")
    print("")
    it = input("> ").lower()

    if it == 'help':
        print("Type Commands To Operate Tesla")
        print("Start - car Started")
        print("Stop - car Stopped")
        print("Inspeed - car speed increased")
        print("Despeed - car speed decreased")
        print("lock - car Locked")
        print("unlock - car Unlocked")
        print("time  - show time")
        print("playfm - Tesla FM")
        print("play - Music on Tesla")
        print("w - go to Straight road")
        print("a - go to Left Turn")
        print("d - go to Right Turn")
        print("s - go to U-Turn")
        print("Exit - Quit Game")
        print("")

    elif it == "time":
        now = datetime.datetime.now()
        print(f"Time is {now.hour % 12} Hour : {now.minute} minute : {now.second} seconds")
        speak(f"{now.hour % 12} Hour {now.minute} minute {now.second} seconds")

    elif it == "play":
        print("Ask for permission")
        permiss = input("Do you give permission for playing music? (Y/N): ")
        if permiss.upper() == "Y":
            print("Listening for you")
            print("1) Love")
            print("2) Friendship")
            choice = input("Choose a song: ")
            if choice.lower() == "love":
                print("Love song...")
                play()
            elif choice.lower() == "friendship":
                print("Friendship song...")
                play1()

    elif it == "playfm":
        print("Play frequency Radio 93.5 English")
        playsound("fm.mp3")

    elif it == "tesla":
        print("Alright Start Tesla to Enjoy Ride Thank You", user.upper())
        print("May be know Commends using KeyWord [HELP]")

    elif it == 'start':
        if started:
            print("Tesla is Already Started")
            playsound("bmw.mp3")
        else:
            started = True
            print("Tesla Started to Drive")
            print("Ready for Travel, increase speed, Movements")
            playsound("release.mp3")
            start()

    elif it == 'lock':
        if started:
            print("Tesla started so off Engine to save battery Energy")
        else:
            print("Tesla Locked")
        lock()

    elif it == "unlock":
        print("Tesla Unlocked")
        lock()

    elif it == 'stop':
        if not started:
            print("Tesla is already stopped")
            print("First Start the Tesla then Enjoy the ride")
        else:
            started = False
            print("Tesla Stop, Right Now")
            playsound("stop.mp3")
            playsound("apply.mp3")
            if speed:
                speed = False
                print("Are you Emergency call 101?")

    elif it == 'exit':
        print("Quit")
        break

    elif started:
        if it == 'inspeed':
            if speed:
                print("You are Too speed it ok for you")
                print("Warnings: go to safe ride")
                playsound("racing01.mp3")
            else:
                speed = True
                print("Tesla Speed increased")
                print("You're speed is 60 km/h")
                takingoff()

        elif it == 'despeed':
            if not speed:
                print("You're nice, maintaing good")
                print("Thanks for go to safe ride")
            else:
                speed = False
                print("Tesla Speed decreased")
                print("You're speed is 30 km/h")

    else:
        print("I Don't Understand that Commend")
        print("This Not a Tesla Comment OR This Comment're Disabled")
        print("Note: Reason for Disabled Comment")
        print("      You're not Start the Tesla Sir")
        score += 1
        print("Please Tell Correct Comment")
        print("This your", score, "tries out of 4")
        if score == 4:
            print(" ")
            print(" ")
            Tesla_security()
            score = 0
