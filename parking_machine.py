

class Dashboard:
    counter = False
    def payment_option(self):
        print('Select payment option')
        self.option = input('Card or Cash? | ').lower()
        if self.option == 'card':
            Dashboard.duration(self)
        elif self.option == 'cash':
            Dashboard.counter = True
            Dashboard.duration(self)
        else:
            print('Something went wrong')


    def make_payment(self):
        if Dashboard.counter == False:
            print('Please swipe your card to pay')
            swipe = input('Contactless - swiped | ').lower()
            if swipe == 'swiped':
                Dashboard.receipt(self)
            else:
                print('Something went wrong')
        elif Dashboard.counter == True:
            print('Please pay cash into the slot')
            slot = input('Slot - paid| ').lower()
            if slot == 'paid':
                Dashboard.receipt(self)
            else:
                print('Something went wrong')
    

    def receipt(self):
        receipt_option = input('Do you want receipt? | ').lower()
        if receipt_option == 'yes':
            print('£'+str(self.bill)+ ' for '+ str(self.dur) +' -Successful! Get your ticket')
        elif receipt_option == 'no':
            print('£'+str(self.bill)+ ' for '+ str(self.dur) +' -Successful!')
        else:
            print('Something went wrong')

    def duration(self):
        self.time = float(input('How long do you want to stay? | '))
        self.dur = str(self.time) +' Hours'
        
        self.bill = self.time + 0.5
        print('£'+str(self.bill)+ ' for '+ str(self.dur))
        Dashboard.make_payment(self)

pay = Dashboard()
pay.payment_option()