
one_Npound = 1236.00
one_Pnaira = 1198.85

print('\nNaira ~ Pound: Enter symbol £.\nPound ~ Naira: Enter symbol N.\n')
while True:
    currency = input(" Enter currency | ")
    if currency == "£":
        print(' £1 = N1236.00')
        amount = float(input(" You are converting: N"))
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
    elif currency == "N":
        print(' £1 = N1198.85')
        amount=float(input(" You are converting: £"))
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
    else:
        print(">>\tError: Invalid currency. Try again!")
        print('\nNaira ~ Pound: Enter symbol £.\nPound ~ Naira: Enter symbol N.\n')
