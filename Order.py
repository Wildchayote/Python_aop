from random import choice
from datetime import datetime
import copy


class InventorySys:
    
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
    try:
        self.knockoff = copy.copy(self.knockoff_val)
        if counter1!=0:
            raise Exception
        else:
            pass
    except AttributeError:
        self.knockoff = copy.copy(self.newstacklist)
        print('Skip Slot activated')
        print()
    else:
        Stack.Printer(self)
        
    def HMM(self):
        print('>>\t'+str(len(self.stacklist))+' each in '+str(len(self.stacklist))+ ' locations.')
    
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
                            setup.Log_timestamp()
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
            if len(self.stacklist)==0:
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
        
class Stack:
    def Aisle(self):
        self.prod = {'CA11':'Aisle AA', 'CA22':'Aisle AA',
                    'FO11':'Aisle AA',  'FO22':'Aisle AA',
                    'BI11':'Aisle AA',  'BI22':'Aisle AB',
                    'CO11':'Aisle AA',  'CO22':'Aisle AA',
                    'JS11':'Aisle AA',  'JS22':'Aisle AA',
                    'MA11':'Aisle AA',  'GS11':'Aisle AA',
                    'SA11':'Aisle AA',  'TS11':'Aisle AA',
                    'TB09':'Aisle AA',  'PN11':'Aisle AA',
                    
                    'AB75': 'Aisle BE A-03 7683 79 01',
                    'SM75': 'Aisle BD A-01 1118 47 01',
                    'PE7L': 'Aisle BL A-02 9785 50 12',
                    'DP30': 'Aisle BA A-02 0530 04 02',
                    'CE35': 'Aisle BA A-03 3248 90 03',
                    'FG1L': 'Aisle BB A-16 3005 86 10'}
        
        self.Item_description = {'CA11':'Carling (CA11) | 11 gal keg, 63.5kg',      'CA22':'Carling (CA22) | 22 gal keg, 100kg',
                    'FO11':'Fosters (FO11) | 11 gal keg, 63.5kg',       'FO22':'Fosters (FO22) | 22 gal keg, 100kg',
                    'BI11':'Birra Moretti (BI11) | 11 gal keg, 63.5kg', 'BI22':'Birra Moretti (BI22) | 22 gal keg, 100kg',
                    'CO11':'Coors Lite (CO11) | 11 gal keg, 63.5kg',    'CO22':'Coors Lite (CO22) | 22 gal keg, 100kg',
                    'JS11':'John Smiths (JS11) | 11 gal keg, 63.5kg',   'JS22':'John Smiths (JS22) | 22 gal keg, 100kg',
                    'MA11':'Madri Lager (MA11) | 11 gal, 63.5kg',       'GS11':'Guiness Stouts (GS11) | 11 gal keg, 63.5kg',
                    'SA11':'Stella Attoires (SA11) | 11 gal, 63.5kg',   'TS11':'Trophy Special (TS11) | 11 gal keg, 63.5kg',
                    'TB09':'Theakson Bitters (TB09) | 09 gal keg, 40kg',

                    'AB75':'Absolut Vodka (AB40) | 40% alc, 75cl',
                    'SM75':'Smirnoff Vodka (SM37) | 38% alc, 75cl',
                    'PE7L': 'Pepsi Cola | 7ltr Big',
                    'DP30':'Desperados Tequila Beer (DP04) | 4% alc, 300ml, x24',
                    'CE35':'Corona Extra Cider (CE35) | 4.5% alc, 350ml, x24',
                    'FG1L': 'Famous Grouse Vodka | 40.5% alc, 1.5ltr , x6'}
        
        self.prod=prod=self.prod
        self.item_value=[1,2,3,4,5,6,7,8,9,10]
        self.item_value=choice(self.item_value)
        self.itemm_value = copy.copy(self.item_value)
        
        self.num = num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        num=choice(num)
        num=copy.copy(num)

        self.Stage_num = Stage_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.Stage_numb=choice(Stage_num)

        while True:
            for i in self.stacklist:
                try:
                    assert i in self.prod
                except AssertionError:
                    print(' >>\t Data not found. Try again!')
                    InventorySys.Queuing(self)
                else:
                    pass
                
                self.uprod = uprod = prod[i]
                self.uprod = uprod[0:8]
                if self.uprod == 'Aisle AA' or self.uprod == 'Aisle AB':                    #   Kegs
                    self.prod= self.uprod
                    self.status = status = input(self.uprod+': ')
                    while True:
                        self.prodd = prodd = copy.copy(self.uprod)
                        if status == 'ready':
                            while True:
                                self.say_num = say_num = int(input('0'+str(num)+': '))
                                if say_num == num:
                                    print()
                                    self.knockoff = Stack.pop(self)
                                    self.newstacklist = copy.copy(self.stacklist)
                                    Stack.Kegs(self)
                                else:
                                    print(' >>\t Wrong check digit '+str(say_num)+'. Try again!')
                        elif status == 'how much more.c' or status == 'HMM.c':
                            InventorySys.HMM(self)
                            print()
                            self.status=status=input(prodd+': ')
                        elif status == 'talkman':
                            InventorySys.Command(self)
                        else: 
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                            self.status=status=input(prodd+': ')
                            
                elif self.uprod != 'Aisle AA':                                                               #  Bottles
                    self.status = status = input(self.uprod+': ')
                    while True:
                        self.prodd = prodd = copy.copy(self.uprod)
                        if status == 'ready':
                            while True:
                                self.seg = uprod[22:]
                                self.say_num = say_num = input(str(self.seg)+' | '+str(uprod[9:13])+': '+uprod[19:21]+': ')
                                self.seg = uprod[19:21]
                                if say_num == str(self.seg):
                                    print()
                                    self.knockoff = Stack.pop(self)
                                    self.newstacklist  = copy.copy(self.stacklist)
                                    Stack.Bottles(self)
                                else:
                                    print(' >>\t Wrong check digit. Try again! ')
                        elif status == 'how much more.c' or status == 'HMM.c':
                            InventorySys.HMM(self)
                            print()
                            self.status = status = input(prodd+': ') 
                        elif status == 'RLP.c':
                            InventorySys.RLP(self)
                        else: 
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                            self.status=status=input(prodd+': ')                                                                  
                else: 
                    print(' >>\t Data not found. Try again!')
                    InventorySys.Queuing(self)

    def Kegs(self):
        print('Pick '+str(self.itemm_value)+' each. '+str(self.Item_description[self.knockoff]) )
        while True:
            self.itemm_value = copy.copy(self.itemm_value)
            self.say_qty=int(input('Quantity? '))
            if self.say_qty == self.itemm_value:
                Stack.Keg_repeater(self)

            elif self.say_qty == 'deliver now.c' or self.say_qty == 'DN.c':
                InventorySys.DN(self)      
                                                                     
            elif self.say_qty > self.itemm_value:
                print_err = ' >>\tYou said {}, I only asked for {}.\n \tTry again, pick {} each.\n \t{}'.format(str(self.say_qty),
                                        str(self.itemm_value), str(self.itemm_value), str(self.Item_description[self.knockoff]))
                print(print_err)
                print()
            else:
                self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I only asked for '+str(self.itemm_value)+
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
        print('Pick '+str(self.itemm_value)+' each. '+str(self.Item_description[self.knockoff]) )
        while True:
            self.itemm_value = copy.copy(self.itemm_value)
            self.say_qty = int(input('Quantity? '))
            if self.say_qty == self.itemm_value:
                Stack.Bottle_ID(self) 
            
            elif self.say_qty == 'deliver now.c' or self.say_qty == 'DN.c':
                InventorySys.DN(self)

            elif self.say_qty > self.itemm_value:
                print_err = ' >>\tYou said {}, I only asked for {}.\n \tTry again, pick {} each.\n \t{}'.format(str(self.say_qty),
                                                 str(self.itemm_value), str(self.itemm_value), str(self.Item_description[self.knockoff]))
                print(print_err)
                print()
            else:
                self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I only asked for '+str(self.itemm_value)+
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
        print('Order picked: '+str(self.say_qty)+' ['+str(self.knockoff)+'] ' +'\nOrder on queue: '+str(self.newstacklist)+'\n')
        self.prodd = copy.copy(self.prod)
        if len(self.newstacklist)>0:
            print()
            Stack.Aisle(self)
        else: 
            InventorySys.Printer(self) 

    def Bottle_ID(self):
        while True:
            self.item_barcode = item_barcode = copy.deepcopy(self.prod)
            self.item_barcode = (item_barcode[self.knockoff])[14:18]
            self.item_no = item_no = input('Item number | '+self.item_barcode+ ': ')
            self.confirm_item_no = input(str(item_no)+ ' corect? ')
            print()
            
            if self.confirm_item_no == 'yes' and item_no == self.item_barcode:
                print('Order picked: '+str(self.say_qty)+' ['+str(self.knockoff)+'] '+'\nOrder on queue: '+str(self.newstacklist)+'\n')
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
        order = self.stacklist[0]
        del self.stacklist[0]
        return order

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

setup = Setup()        
setup.Config()
setup.Log_timestamp()
aop = InventorySys()
aop.Queuing()
