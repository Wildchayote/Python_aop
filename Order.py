from random import choice
from datetime import datetime
import copy


class InventorySys:
    
    def command(self):
        self.command = command = input('Talkman: say (help.c, RLP.c, DN.c, HMM.c): ')
        if command == 'help.c':
            InventorySys.help(self)
        elif command == 'RLP.c':
            print('Repeat last pick not allowed!')
        elif command == 'how much more.c' or command == 'HMM.c':
            InventorySys.HMM(self)
        elif command == 'DN.c':
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
        print('>>\t'+str(len(self.stacklist))+' each in '+str(len(self.stacklist))+ ' locations.')
    
    def DN(self):
        deliver = input('Deliver now? ')
        if deliver == 'yes':
            InventorySys.printer(self)
        elif deliver == 'no':
            pass
        else:
            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            deliver = input('Deliver now? ')
            
    def RLP(self):
        print()
        rlp='''>>\tLast pick was: {}-A-0{}, {}. Pick {} of {} each.\n'''.format(self.prodd, str(self.say_num), self.desc[self.knockoff], str(self.say_qty), str(self.itemm_value))
        print(rlp)

    def stage(self):
        while True:
            self.say_stagenum=say_stagenum=input('Stage number? ')
            if say_stagenum==str(self.stage_numb):
                while True:
                    self.next_assignment=next_assignment=input('Assignment complete! For next assignment, say ready: ')
                    print()
                    if next_assignment=='ready':
                        InventorySys.Queuing(self)
                    elif next_assignment == 'sign off':
                        while True:
                            print('>> >>\tSign off | ', end = '')
                            setup.log_timestamp()
                            sign_on = input('Sign off complete. To sign on again, say ready: ')
                            if sign_on == 'ready':
                                Setup.config(self)
                            else:
                                print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                    else:
                        print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                        InventorySys.command(self)
            else: 
                print(' >>\t Wrong '+str(say_stagenum)+ ', Try again! Deliver to stage 0'+str(self.stage_numb))
                print()
                pass

    def printer(self):
        print('Picking complete!')
        while True:
            printer=int(input('Printer? '))
            print()
            if printer in [2,3]:
                self.stage_numb=stage_numb=self.stage_numb
                select_printer=input(str(printer)+'? LWC '+str(printer)+'? correct? ')
                if select_printer=='yes' and self.self_collect == 'no':
                    print('Deliver to stage 0'+str(stage_numb)+ '\n')
                    InventorySys.stage(self)
                elif select_printer=='yes' and self.self_collect == 'yes':
                    self.stage_numb = 10
                    print('Deliver to stage 0'+str(self.stage_numb)+ '\n')
                    InventorySys.stage(self)
                elif select_printer=='no':
                    pass
                else: 
                    print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            else:
                while True:
                    select_printer = input(str(printer)+'? LWC '+str(printer)+'? correct? ')
                    if select_printer=='yes':
                        print(' >>\t LWC '+str(printer)+' not found. Try again!')
                    elif select_printer=='no':
                        InventorySys.printer(self)
                    else: 
                        print(' >>\t I can\'t hear you. Please speak up a bit.\n')

    def recur(self):
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
        
class Stack:
    def Aisle(self):
        self.prod = {'BI11':'Aisle AA',     'CO22':'Aisle AA',      'MA11':'Aisle AA',      'AB40':'Aisle BE A-03 7683 79 01',      'SM37':'Aisle BD A-01 1118 47 01',      'PE00': 'Aisle BL A-02 9785 50 12'}
        self.desc = {'PE00': 'Pepsi Cola | 7ltr Big',   'BI11':'Birra Moretti (BI11) | 22 gal keg, 63.5kg',     'CO22':'Coors Lite (CO22) | 22 gal keg, 100kg',     'MA11':'Madri Lager (MA11) | 11 gal, 63.5kg',   'AB40':'Absolut Vodka (AB40) | 40% alc, 75cl',      'SM37':'Smirnoff Vodka (SM37) | 38% alc, 75cl'}
        self.prod=prod=self.prod
        self.item_value=[1,2,3,4,5,6,7,8,9,10]
        self.item_value=choice(self.item_value)
        self.itemm_value = copy.copy(self.item_value)
        
        self.num = num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        num=choice(num)
        num=copy.copy(num)

        self.stage_num = stage_num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        self.stage_numb=choice(stage_num)

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
                if self.uprod == 'Aisle AA':                                                        #   Kegs
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
                            InventorySys.command(self)
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
                                self.say_num = say_num = input(str(self.seg)+' | '+str(uprod[9:13])+': ')
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
        print('Pick '+str(self.itemm_value)+' each. '+str(self.desc[self.knockoff]) )
        while True:
            self.itemm_value = copy.copy(self.itemm_value)
            self.say_qty=int(input('Quantity? '))
            if self.say_qty == self.itemm_value:
                Stack.KegRepeater(self)

            elif self.say_qty == 'deliver now.c' or self.say_qty == 'DN.c':
                InventorySys.DN(self)      
                                                                     
            elif self.say_qty > self.itemm_value:
                print_err = ' >>\tYou said {}, I only asked for {}.\n \tTry again, pick {} each.\n \t{}'.format(str(self.say_qty), str(self.itemm_value), str(self.itemm_value), str(self.desc[self.knockoff]))
                print(print_err)
                print()
            else:
                self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I only asked for '+str(self.itemm_value)+'.\n \t Is this a short product? ')
                if short_prod=='yes':
                    Stack.KegRepeater(self)
                    InventorySys.printer(self)
                    break
                elif short_prod == 'no':
                    pass
                elif short_prod == 'how much more.c' or short_prod == 'HMM.c':
                    InventorySys.HMM(self)
                    print()
                else:
                    print(' >>\t I can\'t hear you. Please speak up a bit.\n')
    
    def Bottles(self):
        print('Pick '+str(self.itemm_value)+' each. '+str(self.desc[self.knockoff]) )
        while True:
            self.itemm_value = copy.copy(self.itemm_value)
            self.say_qty = int(input('Quantity? '))
            if self.say_qty == self.itemm_value:
                Stack.bottleID(self) 
            
            elif self.say_qty == 'deliver now.c' or self.say_qty == 'DN.c':
                InventorySys.DN(self)

            elif self.say_qty > self.itemm_value:
                print_err = ' >>\tYou said {}, I only asked for {}.\n \tTry again, pick {} each.\n \t{}'.format(str(self.say_qty), str(self.itemm_value), str(self.itemm_value), str(self.desc[self.knockoff]))
                print(print_err)
                print()
            else:
                self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I only asked for '+str(self.itemm_value)+'.\n \t Is this a short product? ')
                print()
                if short_prod=='yes':
                    Stack.bottleID(self)
                    InventorySys.printer(self)
                    break
                elif short_prod=='no':
                    pass
                elif short_prod == 'how much more.c' or short_prod == 'HMM.c':
                    InventorySys.HMM(self)
                    print()
                else:
                    print(' >>\t I can\'t hear you. Please speak up a bit.\n')

    def KegRepeater(self):
        print()
        print('Order picked: '+str(self.say_qty)+' ['+str(self.knockoff)+'] ' +'\nOrder on queue: '+str(self.newstacklist)+'\n')
        self.prodd = copy.copy(self.prod)
        if len(self.newstacklist)>0:
            print()
            Stack.Aisle(self)
        else: 
            InventorySys.printer(self) 

    def bottleID(self):
        while True:
            self.item_no = item_no = input('Item number? ')
            self.confirm = input(str(item_no)+ ' corect? ')
            print()
            self.barcode = barcode = copy.deepcopy(self.prod)
            self.barcode = (barcode[self.knockoff])[14:18]
            if self.confirm == 'yes' and item_no == self.barcode:
                print('Order picked: '+str(self.say_qty)+' ['+str(self.knockoff)+'] '+'\nOrder on queue: '+str(self.newstacklist)+'\n')
                self.prodd = copy.copy(self.prod)
                if len(self.newstacklist)>0:
                    print()
                    Stack.Aisle(self)
                else:
                    InventorySys.printer(self)
            elif self.confirm == 'yes' and item_no != self.barcode:
                print('Invalid '+ item_no+'. Try again!\n')
            else:
                if self.confirm == 'no':
                    pass
 
    def pop(self):
        order = self.stacklist[0]
        del self.stacklist[0]
        return order

class Setup:
    def log_timestamp(self):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S)")
        print(self.value+ ' :\t' +timestampStr)
    
    def config(self):
        self.match = match = {'Bashir': 'Bashir Sanni', 'Damen': 'Damen Butters', 'Chandler': 'Chandler Morrisons', 'Charlie': 'Charlie Dyer', 'Sean': 'Sean Turner', 'Josh': 'Josh Darley'}
        while True:
            print()
            self.key = key = input('Selecting Operator: ')
            if key in match:
                self.value = match[key]
                print('Current Operator is ' +match[key] +'.\n')
                print('>> >>\tSign on | ', end = '')
                Setup.log_timestamp(self)
                print()
                InventorySys.recur(self)
            else:
                print(' >>\t Unknown Operator. Try again!\n')

setup = Setup()        
setup.config()
setup.log_timestamp()
aop = InventorySys()
aop.Queuing()