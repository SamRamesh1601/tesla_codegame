
# Creating Data for Tesla Game Using Python

from playsound import playsound
import datetime
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("")
print(' Welcome to Tesla Code Game')
speak('  Welcome to Tesla Code Game'  )
print("    your Commends are my life ")
print("")
print(' You are Driving Tesla CAR ')
print("")
user_check=True

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(user1)
        speak(".............good morning")
        print("good  Morning  ",user1.upper())
    elif hour>=12 and hour<17:
        speak(user1)
        speak(".............good Afternoon")
        print("good  Afternoon  ",user1.upper())
    elif hour>=17 and hour<20:
        speak(user1)
        speak("............good Evening")
        print("good  Evening  ",user1.upper())
    else:
        speak(user1)
        speak("............good Night....")
        print("Good  Night ",user1.upper())
user=str(input("     Your Name       "))
user1=user.lower()
commend =['start','stop','inspeed','despeed','w','s','a','d']
print("")
print(" Checking User matching...")
i=0
while i<8:
        if user1 == commend[i]:
            print(" Test Failed please change userName this ",i+1,"th  commend ")
            user1=str(input(" Enter Name -> "))
            i+=1
            print("updataing the user_name successfully  ",user1.upper())
            if i==7:
                print(" Process of checking the user_name to enjoy ride ")
                print(" ")
                print("          thank you -            Tesla")
                break
        i+=1
print("")
user_pass=int(input(" Enter Your Passcode   ->>   "))
print("")
it =""
count=0
uturn = True
speed = False
started = False
exit=True
score=0

def lock():
  playsound("carlock.mp3")

def takingoff():
  playsound('takingoff.mp3')

#Tesla Security Configrution

def Tesla_security():
        speak(" Your Security Breached ")
        print(" Your Security Breached so Tesla asking Questions")
        name=str(input(" your name is  ->  "))
        print(" ")
        name_pass=int(input(" password  is  ->  "))
        if user1==name and user_pass==name_pass:
            print(" Waiting for Recognizing.... ")
            print(" Tesla security Updated  ") 
            print(" thank you ",user1.upper())
            speak(" Recognization..... succesfullly.....so Warm welcome you.........")
            check=False
            global score
            score=0
            
        elif user!=name or user_pass!=name_pass:
            print(" Waiting for Recognizing.... ")
            print(" Tesla's security Alert activated")
            speak(" security Alert......... activated")
            speak(" are  you......... abusing Tesla......?")
            speak("calling........ cop...")
            car_alarm()
            print(" your Wrong owner ",user1.upper()," so your Abusing Tesla ")
            print(" So you getout car or call cap ")
            global exit
            exit=False

def start():
  playsound('carstart.mp3')

def play():
  playsound("vili.mp3")

def play1():
  playsound("no.wav")

def car_alarm():
  playsound('caralarm.mp3')
playsound('E:\\PYTHON\\Tesla\\cardoor.mp3')
wishme()
while exit:
 print("")
 print("")
 it = input("> ").lower()
 
# Tesla help Commends


 if it == 'help':
     print("")
     print(" Type Commends To Opearte Tesla")
     print("")
     print('Start - car Started ')
     print('Stop - car Stopped')
     print('Inspeed - car speed increased')
     print('Despeed - car speed decreased')
     print('lock - car Locked')
     print('unlock - car UnLocked')
     print('time  - show time ')
     print('playfm - Tesla FM')
     print('play - Music on tesla')
     print('w - go to Straight road')
     print('a - go to Left Turn ')
     print('d - go to Right Turn ')
     print('s - go to U-Turn ')
     print('Exit - QuitGame')
     print("")
     
 elif it=="time":
   hour2=int(datetime.datetime.now().hour)
   hour3=int(datetime.datetime.now().minute)
   print(" time is ",hour2," Hour ",hour3," Minute")
   speak(hour2)
   speak(hour3)
 elif it=="play":
   print(" Ask for permission ")
   permiss=str(input(" I need permission for playing music ( Y / N )   "))
   while permiss.upper() == "Y":
     print(" Listening.... for you ")
     print(" ")
     print(" 1) love")
     print(" 2) friendship")
     print(" ")
     choice=str(input(" Enter Choose for song.."))
     if choice.lower()=="love":
       print(" Love song...")
       play()
       permiss="N"
     elif choice.lower()=="friendship":
      print(" Friendship for you")
      play1()
      permiss="N"
     break
 elif it==user1:
   print("")
   print(" I love you  ",user1.title())
   print("")
   print(" Thank You for Choosing me ")
   playsound("thankyou.wav")
   print("    may be any call me , I will take care of Travel safely ")
   print("")
 elif it=="playfm":
   print("")
   print(" play frequency Radio 93.5 English")
   print("")
   playsound("fm.mp3")
 elif it =="tesla":
   print("")
   speak(" I am   Listening............... ")
   print(" I am Listening... ")
   print("")
   print(" Alright Start Tesla to Enjoy Ride Thank You  ",user1.upper()," ")
   print("    May be know Commends using KeyWord  [ HELP ] ")
   print("")
   
# Tesla action Commends


 elif it == 'start':
     if started:
         print("")
         print("Tesla is Already Started..")
         print("")
         playsound("bmw.mp3")

     else:
      started = True
      print("")
      print(" Tesla Started to Drive ")
      print("")
      hour1=int(datetime.datetime.now().hour)
      if hour1>=0 and hour1<12:
        print(user1.upper()," The sun's shine was beautiful , fell the Nature ")
      elif hour1>=12 and hour1<17:
        print(user1.upper()," your going to job or work feel heppy to ride ")
      elif hour1>=17 and hour1<20:
        print(user1.upper()," your Job're Finished ,Ok Go to rest i will save you ")
      else:
        print(user1.upper()," It's late night drive slow to safe, I will protect you ")
      print(" ")
      print(" Ready for Travel , increase speed,Movements")
      print("")
      playsound("release.mp3")
      start() 

 elif it=='lock':
   if started:
     print("")
     print(" Tesla started so off Engine to save battery Energy")
     print("")
     print("")
   else:
    print("")
    print(" Tesla Locked..")
    print("")
    lock()
 elif it=="unlock":
   print("")
   print(" Tesla Unlocked..")
   print("")
   print("    Enjoy Ride")
   print("")
   lock()
 elif it == 'stop':
   if not started:
       print("")
       print("   Tesla  is  already  stopped...  ")
       speak("   Tesla  is  already  stopped...  ")
       print("")
       speak("  First Start the Tesla then Enjoy the ride  ") 
       print("  First Start the Tesla then Enjoy the ride  ")
       print("")
   else:
       started = False   
       print("")
       print(" Tesla Stop , Right Now ")
       print("")
       playsound("stop.mp3")
       playsound("apply.mp3")
       if speed:
        speed=False
        print("")
        print( user1.upper(), "  you Alright breath Out")
        print("")
        print(" Are you Emergency call 101 ? ")
        print("")
        emer=input(" call yes or no ?  ")
        if emer=='yes':
           print("")
           print("Calling 101..... ")
           print("")
        else:
           print("")
           print("Thanks for Feedback")     
           print("")
             

# Tesla Exit Commends


 elif it == 'exit':
     print("")
     print("Quit")
     print("")
     break 


# Tesla Speed Commends


 elif it == 'inspeed':
     if started:
       if speed:
         print("")
         print("You are Too speed it ok for you..")
         print("")
         print(" Warnings: go to safe ride")
         print("")
         playsound("racing01.mp3")
       else:
         speed = True
         print("")
         print(" Tesla Speed increased ")
         print("")
         print(" You're speed is 60 km/h")
         print("")
         takingoff()

     else:
      print("")
      print(" Please Start Tesla to enjoy Ride ")
      print("")
      print(" [ Start ] commends to Activate Speed Controls ")
      print(" ")


 elif it == 'despeed':
     if started:
       if not speed:
         print("")
         print("You're nice , maintaing good..")
         print("")
         print(" Thanks for go to safe ride")
         print("")
       else:
         speed = False
         print("")
         print(" Tesla Speed decreased ")
         print("")
         print(" You're speed is 30 km/h")
         print(" ")
     else:
      print("")
      print(" Please Start Tesla to enjoy Ride ")
      print("")
      print(" [ Start ] commends to Activate Speed Controls ")
      print(" ") 


# Tesla Movement Commends 

 elif started:
  if it == 'w':
     print("")
     print(" Tesla Take Straight Road")
     print("") 

  elif it == 'a':
     print("")
     print(" Tesla Take Turn Left")
     print("")   

  elif it == 'd':
     print("")
     print(" Tesla Take Turn Right")
     print("") 

  elif it == 's':
     if not uturn:
       print("")
       speak(" you are so........ funny Sir ")
       print(" you're funny Sir ")
       print("")
       count+=1
       uturn=True
       speak(" your first way is same ")
       print(" your first way is same ")
       print("")
       print(" Tesla Take UTurn")
       print("")
       
     else:
       print("")
       print(" Tesla Take UTurn")
       print("")
       uturn =False  
     while count==3:
        speak(" your So funny for Destination making,,,,  ")
        print(" Alright ",user1," your So funny for Destination making ")
        print(" all best for ",user1)
        break       


 else:
     print("")
     print(user1.upper(),"   I Don't Understand that Commends")
     print("")
     print("This Not a Tesla Comment OR This Comment're Disabled")
     print("")
     print(" Note:  Reason for Disabled Comment  ")
     print("        you're not Start the Tesla  Sir ")
     score+=1
     print(" plese Tell Correct Comment ")
     print(" this your",score,"trys out of 4")
     if score==4:
            print(" ")
            print(" ")
            check=True
            Tesla_security()
            score=0
