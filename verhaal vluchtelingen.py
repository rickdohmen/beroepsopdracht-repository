#moet er voor zorgen dat verschillende antwoorden naar naar de goede vraag gaan die er daarna komen
#zorgen dat er 4 einden zijn in het verhaal
#ga kijken hoe dat moet doen of vraag aan anderen

print("een print voor de test commit naar github")
print("Hi, this little game is based on a true story that happend but you are going to be the person of the story and you have to decide what this persons fate is going to be, good luck!.")
print("the story starts in iran and you are fleeing to europe to have better and saver life for yourself and for your family.")
print("what is your name? please think of an name dat is from around that region.")
naam = input()
print("your name is: " + naam)
print("now let's start the game shall we")
#---------------------------------------------------------------------------------------------------------------------------------------------------------
def question1():
    antwoord1 = input ("you have to flee from your home in Iran because of the war and you're thinking of where to go\nA you go north west\nB you go to the south west ")

    if antwoord1.lower() == "a":
        print("A")
        question14()

    elif  antwoord1.lower() == "b":
        print("B")
        question13()
        
def question2():
    antwoord2 = input ("while walking to the north west and arriving at a coast on the border of Turkey you had to decide\nA im going with a plane to europe \nB you are going with a boat to greece \nC you are going to walk through Turkey and spmeday arrive in europe")

    if antwoord2.lower() == "a":
        print("A")
        question18()

    elif  antwoord2.lower() == "b":
        print("B")
        question21()
    
    elif  antwoord2.lower() == "c":
         print("C")
         question22()


def question3():
    antwoord3 = input ("vraag3")

    if antwoord3.lower() == "a":
        print("A")
        question17()

    elif  antwoord3.lower() == "b":
        print("B")
        question11()

def question4():
    antwoord4 = input ("vraag4")

    if antwoord4.lower() == "a":
        print("A")
        question10()

    elif  antwoord4.lower() == "b":
        print("B")
        question8()

def question5():
    #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question6():
    antwoord5 = input ("vraag6")

    if antwoord5.lower() == "a":
        print("A")
        question4()

    elif  antwoord5.lower() == "b":
        print("B")
        question4()

def question7():
    #einde
    print("you arrived in europe but without your family at your side")

def question8():
    print("you managed to get on the plane now on your way to europe")
    question10()

def question9():
    antwoord6 = input ("the police are running after you until you get to place where there is nowhere to go \nA you try to explain what happend to youand where you are from \nByou put your hands i your pockets and try to intimedate them making them think you have a weapon")
    
    if antwoord6.lower() == "a":
        print("A")
        question20()

    elif  antwoord6.lower() == "b":
        print("B")
        question16()

def question10():
    antwoord7 = input ("you arrive at the airport somewhere in europe but in the airport you see the police and try to run becuase you think they are searching for you  \nA you run as fast you can right past them \nB you make rucus and try to get away")

    if antwoord7.lower() == "a":
        print("A")
        question9()

    elif  antwoord7.lower() == "b":
        print("B")
        question15()

def question11():
    #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question12():
    antwoord8 = input ("vraag12")

    if antwoord8.lower() == "a":
        print("A")
        question6()

    elif  antwoord8.lower() == "b":
        print("B")
        question3()

def question13():
    antwoord9 = input ("you go southwest and you arrive at lebanon and decide if you want to stay here\nA you stay there and end up at a refugee camp\nB you think of going north ")

    if antwoord9.lower() == "a":
        print("A")
        question5()

    elif  antwoord9.lower() == "b":
        print("B")
        question19()

def question14():
    antwoord10 = input ("after giving it a good thought you decided to go north west towards Turkey or Azerbaijan \nNow is the question isit sace to go northe west or is it smart to towards lebanon or not \nA you started walking to the north westand go to turkey and eventually to europe \nB you've changed your mind and decided to go southwest to lebanon")

    if antwoord10.lower() == "a":
        print("A")
        question2()

    elif  antwoord10.lower() == "b":
        print("B")
        question13()

def question15():
    #einde
    print("you get shot by the cop and you will die by the fatal wound")

def question16():
   #einde
    print("you get shot by the cop and you will die by the fatal wound")

def question17():
   #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question18():
    antwoord11 = input ("you went to the closesed airport that you could find and decided \nA that you take the plane with last bit of money that you have \nB you try to get on the plane unnoticed")

    if antwoord11.lower() == "a":
        print("A")
        question10()

    elif  antwoord11.lower() == "b":
        print("B")
        question8()

def question19():
    antwoord12 = input ("vraag19")

    if antwoord12.lower() == "a":
        print("A")
        Squestion12()

    elif  antwoord12.lower() == "b":
        print("B")
        question7()

def question20():
    #einde
    print("you explained everything to the cops and they brought you to the police bureau too make sure if everything is true \nAfter 30 min the cops come back and welcome you in the Netherlands and ask if you have family and you say yes \nAfter you said yes they gave you a addres to go so that you can take your family here \nOne year has gone past and your family arrived here")
    print("you have arrived in europe and with your family at your side to make the best out of your life")

def question21():
    #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question22():
    antwoord13 = input ("vraag22")

    if antwoord13.lower() == "a":
        print("A")
        question4()

    elif  antwoord13.lower() == "b":
        print("B")
        question4()
#-------------------------------------------------------------------------------

question1()
