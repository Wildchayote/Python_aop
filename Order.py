from random import choice
from datetime import datetime
import copy




class Stack:

    def Aisle(self):
        self.prod ={'CA11': 'Aisle AA-07',   'CA22': 'Aisle AA-11',    'AB75': 'Aisle BE-79 A-03 7683 01',
                    'FO11': 'Aisle AA-01',   'FO22': 'Aisle AA-06',    'SM75': 'Aisle BE-47 A-01 1118 01',
                    'BI11': 'Aisle AA-15',   'BI22': 'Aisle AB-32',    'PE7L': 'Aisle BL-50 A-02 9785 12',
                    'CO11': 'Aisle AA-05',   'CO22': 'Aisle AA-02',    'DP30': 'Aisle BA-04 A-02 0530 02',
                    'JS11': 'Aisle AA-12',   'JS22': 'Aisle AA-08',    'CE35': 'Aisle BA-90 A-03 3248 03',
                    'MA11': 'Aisle AA-09',   'GD11': 'Aisle AA-10',    'FG1L': 'Aisle BB-86 A-16 3005 10',
                    'SA11': 'Aisle AA-13',   'TS11': 'Aisle AA-14',
                    'TB09': 'Aisle AA-16',   'PN11': 'Aisle AA-04'}
        
        self.Item_description ={
                    'CA11': 'Carling (CA11) | 11 gal keg, 63.05kg',         'CA22': 'Carling (CA22) | 22 gal keg, 100kg',
                    'FO11': 'Fosters (FO11) | 11 gal keg, 63.05kg',         'FO22': 'Fosters (FO22) | 22 gal keg, 100kg',
                    'BI11': 'Birra Moretti (BI11) | 11 gal keg, 63.05kg',   'BI22': 'Birra Moretti (BI22) | 22 gal keg, 100kg',
                    'CO11': 'Coors Lite (CO11) | 11 gal keg, 63.05kg',      'CO22': 'Coors Lite (CO22) | 22 gal keg, 100kg',
                    'JS11': 'John Smiths (JS11) | 11 gal keg, 63.05kg',     'JS22': 'John Smiths (JS22) | 22 gal keg, 100kg',
                    'MA11': 'Madri Lager (MA11) | 11 gal, 63.05kg',         'GS11': 'Guiness Draughts (GS11) | 11 gal keg, 63.05kg',
                    'SA11': 'Stella Attoires (SA11) | 10.5 gal, 55.05kg',   'TS11': 'Trophy Special (TS11) | 11 gal keg, 63.05kg',
                    'TB09': 'Theakson Bitters (TB09) | 09 gal keg, 40kg',   'PN11': 'Peroni Special Lager (PN11) | 11 gal keg, 63.05kg',

                    'AB75': 'Absolut Vodka (AB40) | 40% alc, 6x75cl',       'DP30': 'Desperados Tequila Beer (DP04) | 4% alc, 300ml, 24x330ml',
                    'SM75': 'Smirnoff Vodka (SM37) | 38% alc, 6x75cl',      'CE35': 'Corona Extra Cider (CE35) | 4.5% alc, 350ml, 24x350ml',
                    'PE7L': 'Britvic Pepsi Cola Max | 7lt Bib',             'FG1L': 'Famous Grouse Whisky | 40.5% alc, 1.5lt , 6x1.5lt'}

        self.Stage_num = Stage_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.Stage_numb = choice(Stage_num)

        key = []
        quantity = []
        for i in self.stacklist:
            demo = i[0:4]
            quan = i[5:]
            key.append(demo)
            quantity.append(quan)
        self.order_dict = dict(zip(key, quantity))

        value = []
        for i in self.prod:
            if i in key:
                demo0 = (self.prod[i])[0:11]
                value.append(demo0)

        self.order_list0 = []

        for j in self.prod:
            if j in key:
                new_list = list(map(lambda s: j, sorted(value)))
                new_list0 = (new_list[0])[0:8]
                self.order_list0.append(new_list0)

        try:
            self.order_list0 = copy.copy(self.newstacklist)
        except AttributeError:
            self.order_list0 = copy.copy(self.order_list0)
            pass
        else:
            pass

        while True: 
            for i in self.order_list0:
                try:
                    assert i in self.prod
                except AssertionError:
                    print(' >>\t Data not found. Try again!')
                    InventorySys.Queuing(self)
                else:
                    pass
                self.uprod = uprod = self.prod[i]
                self.uprod = uprod[0:8]


                try:
                    knockoff_val = (self.prod[self.knockoff])[0:8] 
                    if knockoff_val == self.uprod:
                        raise Exception
                    else:
                        pass
                        #raise AttributeError
                except AttributeError:
                    pass
                except Exception:
                    if self.uprod == 'Aisle AA' or self.uprod == 'Aisle AB':
                        Stack.verify_keg(self)                            
                    else:
                        Stack.verify_bottle(self)
                   

                if self.uprod == 'Aisle AA' or self.uprod == 'Aisle AB':                    #Kegs
                    self.status = status = input(self.uprod+': ')
                    while True:
                        self.prodd = prodd = copy.copy(self.uprod)
                        if status == 'ready':
                            while True:
                                Stack.verify_keg(self)

                        elif status == 'how much more.c' or status == 'HMM.c':
                            InventorySys.HMM(self)
                            print()
                            self.status=status=input(prodd+': ')

                        elif status == 'aisle summary':
                            Stack.Aisle_summary(self)
                            self.status=status=input(self.prodd+': ')

                        elif status == 'RLP.c':
                            InventorySys.RLP(self)

                        else: 
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                            self.status=status=input(prodd+': ')
                            
                elif self.uprod != 'Aisle AA':                                                               #  Bottles
                    self.status = status = input(self.uprod+': ')
                    while True:

                        self.prodd = prodd = copy.copy(self.uprod)
                        if status == 'ready':
                            while True:
                                Stack.verify_bottle(self)

                        elif status == 'how much more.c' or status == 'HMM.c':
                            InventorySys.HMM(self)
                            print()
                            self.status = status = input(prodd+': ')

                        elif status == 'aisle summary':
                            Stack.Aisle_summary(self)
                            self.status=status=input(self.prodd+': ')

                        elif status == 'RLP.c':
                            InventorySys.RLP(self)

                        else: 
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                            self.status=status=input(prodd+': ')                                                                  
                else: 
                    print(' >>\t Data not found. Try again!')
                    InventorySys.Queuing(self)


    def Kegs(self):
        self.knockoff = knockoff = self.knockoff
        if knockoff in self.order_dict:
            quantity =self.order_dict[knockoff]
            print('Pick '+str(quantity)+' each. ', end = '')
            print(str(self.Item_description[knockoff]))
        
        while True:
            self.say_qty=int(input('Quantity? '))
            if self.say_qty == int(quantity):
                Stack.Keg_repeater(self)

            elif self.say_qty == 'deliver now.c' or self.say_qty == 'DN.c':
                InventorySys.DN(self)      
                                                                     
            elif self.say_qty > int(quantity):
                print_err = ' >>\tYou said {}, I only asked for {}.\n \tTry again, pick {} each.\n \t{}'.format(str(self.say_qty),
                                        str(int(quantity)), str(int(quantity)), str(self.Item_description[self.knockoff]))
                print(print_err)
                print()
            else:
                self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I only asked for '+str(int(quantity))+
                                                 '.\n \t Is this a short product? ')
                if short_prod=='yes':
                    Stack.Keg_repeater(self)
                    InventorySys.Printer(self)
                    break
                elif short_prod == 'no':
                    pass
                elif short_prod == 'how much more.c' or short_prod == 'HMM.c':
                    InventorySys.HMM(self)
                    print()
                else:
                    print(' >>\t I can\'t hear you. Please speak up a bit.\n')
    
    def Bottles(self):
        self.knockoff = knockoff = self.knockoff
        if knockoff in self.order_dict:
            self.quantity = self.order_dict[knockoff]
            print('Pick '+str(self.quantity)+' each. ', end = '')
            print(str(self.Item_description[knockoff]))

        while True:
            self.say_qty = int(input('Quantity? '))
            if self.say_qty == int(self.quantity):
                Stack.Bottle_ID(self) 
            
            elif self.say_qty == 'deliver now.c' or self.say_qty == 'DN.c':
                InventorySys.DN(self)

            elif self.say_qty > int(self.quantity):
                print_err = ' >>\tYou said {}, I only asked for {}.\n \tTry again, pick {} each.\n \t{}'.format(str(self.say_qty),
                                                 str(self.quantity), str(self.quantity), str(self.Item_description[knockoff]))
                print(print_err)
                print()
            else:
                self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I only asked for '+str(self.quantity)+
                                                 '.\n \t Is this a short product? ')
                print()
                if short_prod=='yes':
                    Stack.Bottle_ID(self)
                    InventorySys.Printer(self)
                    break
                elif short_prod=='no':
                    pass
                elif short_prod == 'how much more.c' or short_prod == 'HMM.c':
                    InventorySys.HMM(self)
                    print()
                else:
                    print(' >>\t I can\'t hear you. Please speak up a bit.\n')

    def Keg_repeater(self):
        print()
        print('Items picked: '+str(self.say_qty)+' ['+str(self.knockoff)+'] ' +'\nItems on queue: '+str(self.newstacklist)+'\n')
        self.prodd = copy.copy(self.prod)
        
        if len(self.newstacklist)>0:
            print()
            Stack.Aisle(self)  
        else: 
            InventorySys.Printer(self) 

    def Bottle_ID(self):
        while True:
            self.item_barcode = item_barcode = self.prod
            self.item_barcode = (item_barcode[self.knockoff])[17:21]
            self.item_no = item_no = input('Item number | '+self.item_barcode+ ': ')
            self.confirm_item_no = input(str(item_no)+ ' corect? ')
            print()
            
            if self.confirm_item_no == 'yes' and item_no == self.item_barcode:
                print('Items picked: '+str(self.say_qty)+' ['+str(self.knockoff)+'] '+'\nItems on queue: '+str(self.newstacklist)+'\n')
                self.prodd = copy.copy(self.prod)

                if len(self.newstacklist)>0:
                    print()
                    Stack.Aisle(self)
                else:
                    InventorySys.Printer(self)

            elif self.confirm_item_no == 'yes' and item_no != self.item_barcode:
                print('Invalid '+ item_no+'. Try again!\n')
            else:
                if self.confirm_item_no == 'no':
                    pass
 
    def pop(self):
        order = self.order_list0[0]
        del self.order_list0[0]
        return order
    

    def verify_keg(self):
        for i in self.order_list0:
                
            self.uprod = uprod = self.prod[i]
            self.aisle_num = self.uprod[9:11]
            self.say_num = say_num = input((self.aisle_num)+': ')
            if say_num == self.aisle_num:
                print()
                self.knockoff = Stack.pop(self)
                self.newstacklist = copy.copy(self.order_list0)
                Stack.Kegs(self)
            else:
                print(' >>\t Wrong check digit '+str(self.aisle_num)+'. Try again!')

    def verify_bottle(self):
        for i in self.order_list0:

            self.uprod = uprod = self.prod[i]
            self.seg = uprod[22:]
            self.check_digit = uprod[9:11]
            self.check = uprod[12:16]

            self.say_num = say_num = input(str(self.seg)+' | '+str(self.check)+': '+self.check_digit+': ')
            if say_num == str(self.check_digit):
                print()
                self.knockoff = Stack.pop(self)
                self.newstacklist  = copy.copy(self.order_list0)
                Stack.Bottles(self)
            else:
                print(' >>\t Wrong check digit. Try again! ')


    def Aisle_summary(self):
        j = [eval(i[5:]) for i in self.stacklist]
        items = sum(j)
        print()
        print(str(items)+ ' items in '+ str(len(self.stacklist))+ ' locations.')



class InventorySys(Stack):

    def Command(self):
        self.Command = Command = input('Talkman: say (help.c, RLP.c, DN.c, HMM.c): ')
        if Command == 'help.c':
            InventorySys.help(self)
        elif Command == 'RLP.c':
            print('Repeat last pick not allowed!')
        elif Command == 'how much more.c' or Command == 'HMM.c':
            InventorySys.HMM(self)
        elif Command == 'DN.c':
            InventorySys.DN(self)
        else:
            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            
    def help(self):
        print('''\n
RLP: Repeat last pick
AS: Aisle summary
DN: Deliver now
HMM: How much more
SA: Say again \n
        ''')
    
    def HMM(self):
        print('>>\t'+str(len(self.order_list))+' each in '+str(len(self.order_list))+ ' locations.')
    
    def DN(self):
        deliver = input('Deliver now? ')
        if deliver == 'yes':
            InventorySys.Printer(self)
        elif deliver == 'no':
            pass
        else:
            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            deliver = input('Deliver now? ')
            
    def RLP(self):
        print()
        rlp='''>>\tLast pick was: {}-A-0{}, {}. Pick {} of {} each.\n'''.format(self.prodd, str(self.say_num),
        self.Item_description[self.knockoff], str(self.say_qty), str(self.itemm_value))
        print(rlp)

    def Stage(self):
        while True:
            self.say_Stagenum=say_Stagenum=input('Stage number? ')
            if say_Stagenum==str(self.Stage_numb):
                while True:
                    self.next_assignment=next_assignment=input('Assignment complete! For next assignment, say ready: ')
                    print()
                    if next_assignment=='ready':
                        InventorySys.Queuing(self)
                    elif next_assignment == 'sign off':
                        while True:
                            print('<< <<\tSign off | ', end = '')
                            Setup.Log_timestamp(self)
                            sign_on = input('Sign off complete. To sign on again, say ready: ')
                            if sign_on == 'ready':
                                Setup.Config(self)
                            else:
                                print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                    else:
                        print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                        InventorySys.Command(self)
            else: 
                print(' >>\t Wrong '+str(say_Stagenum)+ ', Try again! Deliver to Stage 0'+str(self.Stage_numb))
                print()
                pass

    def Printer(self):
        print('Picking complete!')
        while True:
            Printer=int(input('Printer? '))
            print()
            if Printer in [2,3]:
                self.Stage_numb=Stage_numb=self.Stage_numb
                select_Printer=input(str(Printer)+'? TIMELESS '+str(Printer)+'? correct? ')
                if select_Printer=='yes' and self.self_collect == 'no':
                    print('Deliver to Stage 0'+str(Stage_numb)+ '\n')
                    InventorySys.Stage(self)
                elif select_Printer=='yes' and self.self_collect == 'yes':
                    self.Stage_numb = 10
                    print('Deliver to Stage 0'+str(self.Stage_numb)+ '\n')
                    InventorySys.Stage(self)
                elif select_Printer=='no':
                    pass
                else: 
                    print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            else:
                while True:
                    select_Printer = input(str(Printer)+'? TIMELESS '+str(Printer)+'? correct? ')
                    if select_Printer=='yes':
                        print(' >>\t TIMELESS '+str(Printer)+' not found. Try again!')
                    elif select_Printer=='no':
                        InventorySys.Printer(self)
                    else: 
                        print(' >>\t I can\'t hear you. Please speak up a bit.\n')

    def Recur(self):
        self.start=start=input('VOICE picking. Directive picking. To receive work, say ready:  ')
        while True:
            if start=='ready':
                self.password=password=input('Password? ')
                while True:
                    if password=='1234':
                        InventorySys.Queuing(self)
                    else:
                        password=input(' >>\t Wrong '+password+'. Try again! Password? ')
            else: 
                start=input(' >>\t I can\'t hear you. Please speak up a bit. To receive work, say ready: ')

    def Queuing(self):
        print()
        
        self.stacklist=input('Load Assignment: ')
        self.self_collect = self_collect = input('Self Collect? ')
        print()
        self.stacklist = stacklist = self.stacklist.split()
              

        try:
            assert self.self_collect in ['yes', 'no']
        except AssertionError:
            print('Invalid [ '+self_collect+ ' ]. Enter yes or no')
            self.self_collect = input('Self Collect? ')
        else:
            pass

        try:
            if len(stacklist)==0:
                raise IndexError
        except IndexError:
            while True:
                self.no_work=no_work=input(' >>\t No work available, continue to say ready: ')
                if no_work=='ready':
                    InventorySys.Queuing(self)
                else:
                    print(' >>\t I can\'t hear you. Please speak up a bit.\n')
        else:
            Stack.Aisle(self)





class Setup:
    def Log_timestamp(self):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S)")
        print(self.value+ ' :\t' +timestampStr)
    
    def Config(self):
        self.match = match = {'Bashir': 'Bashir Sanni', 'Damen': 'Damen Butters', 'Chandler': 'Chandler Morrisons', 
                            'Charlie': 'Charlie Dyer', 'Sean': 'Sean Turner', 'Josh': 'Josh Darley'}
        while True:
            print()
            self.key = key = input('Selecting Operator: ')
            if key in match:
                self.value = match[key]
                print('Current Operator is ' +match[key] +'.\n')
                print('>> >>\tSign on | ', end = '')
                Setup.Log_timestamp(self)
                print()
                InventorySys.Recur(self)
            else:
                print(' >>\t Unknown Operator. Try again!\n')

#setup = Setup()        
#setup.Config()
#setup.Log_timestamp()

aop = InventorySys()
aop.Queuing()
