def NairaException:
    try:
        amount=float(input(" You are converting: £"))
    except TypeError:
        print("Wrong input. Try again!")
        NairaException()
    else:
        convert=amount*one_Pnaira
        print()
        print(' To: NGN'+str(round(convert,2))+'\n')
        next=input("""\n
    Do you want to perform another conversion?
    Enter YES to perform another conversion and NO to quit | """)
        if next.lower()=="yes":
            continue
        else:
            break

def PoundException:
    try:
        amount = float(input(" You are converting: N"))
    except TypeError:
        print("Wrong input. Try again!")
        PoundException()
    else:
        convert = amount/one_Npound
        print()
        print(' To: GBP'+str(round(convert,2))+"\n")
        next=input("""
    Do you want to perform another conversion?
    Enter YES to perform another conversion and NO to quit | """)
        if next.lower()=="yes":
            continue
        else:
            break
            
one_Npound = 1236.00
one_Pnaira = 1198.85

print('\nNaira ~ Pound: Enter symbol £.\nPound ~ Naira: Enter symbol N.\n')
while True:
    currency = input(" Enter currency | ")
    if currency == "£":
        print(' £1 = N1236.00')
        PoundException
    elif currency == "N":
        print(' £1 = N1198.85')
        NairaException()
    else:
        print(">>\tError: Invalid currency. Try again!")
        print('\nNaira ~ Pound: Enter symbol £.\nPound ~ Naira: Enter symbol N.\n')
