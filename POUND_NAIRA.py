print('\nNaira ~ Pound: Enter symbol £.\nPound ~ Naira: Enter symbol N.\n')

def NairaException():
    try:
        amount=float(input(" You are converting: £"))
    except ValueError:
        print("\n>> Error: Wrong input. Try again!")
        NairaException()
    else:
        convert=amount*one_Pnaira
        print()
        print(' To: NGN'+str(round(convert,2))+'\n')
        next=input("""\n
    Do you want to perform another conversion?
    Enter YES to perform another conversion and NO to quit | """)
        if next.lower()=="yes":
            pass
        else:
            quit()

def PoundException():
    try:
        amount = float(input(" You are converting: N"))
    except ValueError:
        print("\n>> Error: Wrong input. Try again!")
        PoundException()
    else:
        convert = amount/one_Npound
        print()
        print(' To: GBP'+str(round(convert,2))+"\n")
        next=input("""
    Do you want to perform another conversion?
    Enter YES to perform another conversion and NO to quit | """)
        if next.lower()=="yes":
            pass
        else:
            quit()
            
<<<<<<< HEAD
one_Npound = 1550.00
one_Pnaira = 1450.25
=======
one_Npound = 730.00
one_Pnaira = 770.85
>>>>>>> eb6678bb0bbf23ebb9f421033414c3a45372e388


while True:
    currency = input(" Enter currency | ")
    if currency == "£":
        print(' £1 = N1550.00')
        PoundException()
    elif currency == "N":
        print(' £1 = N1450.25')
        NairaException()
    else:
        print(">> Error: Unsupported currency. Try again!")
        #print('\nNaira ~ Pound: Enter symbol £.\nPound ~ Naira: Enter symbol N.\n')

