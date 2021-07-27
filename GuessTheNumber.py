import random
import sys
scor=0
h=1
lost=False
def checkAnswer(r,userAnswer,score):
    ar=int(userAnswer)
    global lost
    global scor
    if(ar>=1 or ar<=100):
        if(ar==r):
            print("\nBravo you have found the answer\n")
            lost=False
            scor+=10
            
        elif(ar!=r):
            print("\nWrong! You lost a point\n")            
            lost=True
            scor-=1
    scorStr=str(scor)
    print("Your score is "+scorStr)

def giveHint(r,userAnswer):
    
    ua=int(userAnswer)
    ra=int(r)
    a=abs(ua-ra)
    global h
    
    if(a>=1 and a<10 and h==1):
        print("You are close")
        h+=1

    elif(h==2):
        if(r%2==0):
            print("It is an even number")
        else:
            print("It is an odd number")
        h+=1
        
    elif(h==3):
        if(r%3==0):
            print("It can be divided by 3")
        if(r%5==0):
            print("It can be divided by 5")
        if(r%10==0):
            print("It can be divided by 10")
        if(r%7==0):
            print("It can be divided byy 7")
        h+=1

def checkVal(anss):
    ans=int(anss)
    if(ans<=0):
        raise Exception("It was between 1 and 100 !!! (1<=number<=100")
    else:
        return False


ch=""
choice=""
    
while(1):
    if(lost==False):
        randomNumber=random.randint(1,100)
        print("Welcome to Guess The Number\nI have a number in my mind. It is between 1 and 100.\nCan you guess it?")
    userA=input("\nEnter your value: ")
    if (checkVal(userA)==False):
        checkAnswer(randomNumber,userA,scor)
    
    if(lost==True):
        giveHint(randomNumber, userA)
    ch=input("Would you like to continue?\n").lower()
    if(ch=="no" or ch=="exit"):
        sys.exit()
    