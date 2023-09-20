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
            
one_Npound = 1236.00
one_Pnaira = 1198.85


while True:
    currency = input(" Enter currency | ")
    if currency == "£":
        print(' £1 = N1236.00')
        PoundException()
    elif currency == "N":
        print(' £1 = N1198.85')
        NairaException()
    else:
        print(">> Error: Unsupported currency. Try again!")
        #print('\nNaira ~ Pound: Enter symbol £.\nPound ~ Naira: Enter symbol N.\n')

