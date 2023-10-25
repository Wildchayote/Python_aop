from random import random, choice
import time, json

print()
marks=0
marks1=0

try:
    questions=int(input("How many questions would you like to try? "))
    print()
except (KeyboardInterrupt, ValueError):
    print("\n\t[error!] Something went wrong!\n")
    try:
        questions=int(input("\t[error!] Try again! Enter an integer > 0:  "))
        print()
    except:
        print()
        try:
            questions=int(input("\t[error!] Enter an integer > 0:   "))
        except:
            print()
            try:
                questions=int(input("\t[error!!] Enter an integer value > 0:   "))
                print()
            except:
                print("\n\t[error!!!] Logging you off dumbass! Relaunch app to start allover.\n")
                exit()

while True:
    with open('C:\\Users\\labod\\Desktop\\dictionary.txt', 'r') as file:
    world_atlas = json.load(file)
    
    print("Fab!", questions,"questions,...Let's go!")
    for i in range(questions):
        keys = list(world_atlas)
        country = choice(keys)
        counter = marks + marks1 

        print("\nQuestion",counter+1,":")
        print("What is the capital of",country.upper(),"?")
        answer=input("Answer: ").upper()
        
        if answer==world_atlas[country]:
            print(">>\tCorrect!")
            marks+=1
            time.sleep(1)
        else:
            print(">>\tWrong!:", end = '')
            print("\tThe capital of",country.title(), "is", world_atlas[country].title())
            marks1+=1
            time.sleep(1)

    print()
    print('*** Loading result...')
    time.sleep(3)
    print("You scored ",marks,'/',questions)
    
    score = marks / questions
    if marks < questions*.5:
        time.sleep(2)
        print("\nYou got",round(score*100,2),"%")
        print("You failed the quiz!...relaunch app to try again!\n".center(500))
        exit()
    else:
        marks>=questions*.5
        time.sleep(2)
        print("\nCongratulation!  You've passed the quiz... you got",round(score*100,2),"%\n")
        exit()
   
