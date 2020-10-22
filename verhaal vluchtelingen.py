#moet er voor zorgen dat verschillende antwoorden naar naar de goede vraag gaan die er daarna komen
#zorgen dat er 4 einden zijn in het verhaal
#ga kijken hoe dat moet doen of vraag aan anderen


#---------------------------------------------------------------------------------------------------------------------------------------------------------
def question22():
    antwoord = input ("vraag22")

    if antwoord13.lower == "a":
        print("A")
        question4()

    elif  antwoord13.lower == "b":
        print("B")
        question4()

def question21():
    #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question20():
    #einde
    print("you have arrived in europe and with your family at your side to make the best out of your life")

def question19():
    antwoord = input ("vraag19")

    if antwoord12.lower == "a":
        print("A")
        Squestion12()

    elif  antwoord12.lower == "b":
        print("B")
        question7()

def question18():
    antwoord = input ("vraag18")

    if antwoord11.lower == "a":
        print("A")
        question10()

    elif  antwoord11.lower == "b":
        print("B")
        question8()

def question17():
   #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question16():
   #einde
    print("you died and wil never comeback again")

def question15():
    #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question14():
    antwoord = input ("vraag14")

    if antwoord10.lower == "a":
        print("A")
        question2()

    elif  antwoord10.lower == "b":
        print("B")
        question13()

def question13():
    antwoord = input ("you go southwest and you arrive at lebanon and decide if you want to stay here\nA you stay there and end up at a refugee camp\nB you think of going north")

    if antwoord9.lower == "a":
        print("A")
        question5()

    elif  antwoord9.lower == "b":
        print("B")
        question19()

def question12():
    antwoord = input ("vraag12")

    if antwoord8.lower == "a":
        print("A")
        question6()

    elif  antwoord8.lower == "b":
        print("B")
        question3()

def question11():
    #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question10():
    antwoord = input ("vraag10")

    if antwoord7.lower == "a":
        print("A")
        question9()

    elif  antwoord7.lower == "b":
        print("B")
        question15()

def question9():
    antwoord = input ("vraag9")
    
    if antwoord6.lower == "a":
        print("A")
        question20()

    elif  antwoord6.lower == "b":
        print("B")
        question16()

def question8():
    question10()

def question7():
    #einde
    print("you arrived in europe but without your family at your side")

def question6():
    antwoord = input ("vraag6")

    if antwoord5.lower == "a":
        print("A")
        question4()

    elif  antwoord5.lower == "b":
        print("B")
        question4()

def question5():
    #einde
    print("you have arrived at a refugee camp where you wil now live forever")

def question4():
    antwoord = input ("vraag4")

    if antwoord4.lower == "a":
        print("A")
        question10()

    elif  antwoord4.lower == "b":
        print("B")
        question8()

def question3():
    antwoord = input ("vraag3")

    if antwoord3.lower == "a":
        print("A")
        question17()

    elif  antwoord3.lower == "b":
        print("B")
        question11()

def question2():
    antwoord = input ("vraag2")

    if antwoord2.lower == "a":
        print("A")
        question18()

    elif  antwoord2.lower == "b":
        print("B")
        question21()
    
    elif  antwoord2.lower == "c":
         print("C")
         question22()

def question1():
    antwoord1 = input ("you have to flee from your home in Iran because of the war and you're thinking of where to go\nA you go north west\nB you go to the south west")

    if antwoord1.lower() == "a":
        print("A")
        question14()

    elif  antwoord1.lower == "b":
        print("B")
        question13()
#-------------------------------------------------------------------------------
print("een print voor de test commit naar github")
print("Hi, this little game is based on a true story that happend but you are going to be the person of the story and you have to decide what this persons fate is going to be, good luck!.")
print("the story start in iran and you are fleeing to europe to have better and saver life for yourself and for your family.")
print("what is your name? please think of an name dat is from around that region.")
naam = input()
print("your name is: " + naam)
question1()

