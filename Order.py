from random import choice
from datetime import datetime
import copy
import math



class InventorySys:
       
    def help(self):
        print('''\n
    COMMAND LIST:
RLP.c: Repeat last pick
AS.c: Aisle summary
DN.c: Deliver now
HMM.c: How much more
SS.c: Skip slot \n
        ''')

    def self_collect(self):
        try:
            assert self.self_collect in ['yes', 'no']
        except AssertionError:
            print(' >>\tInvalid input [ '+self.self_collect+ ' ]. Enter yes or no')
            self.self_collect = input('Self Collect? ')
            InventorySys.self_collect(self)
        else:
            try:
                if len(self.stacklist)==0:
                    raise Exception
            except Exception:
                self.no_work=no_work=input(' >>\tNo work available, continue to say ready: ')
                while True:
                    if no_work=='ready':
                        InventorySys.Queuing(self)
                    elif no_work == 'SA.c':
                       self.no_work=no_work=input(' >>\tNo work available, continue to say ready: ') 
                    else:
                        print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            else:
                Stack.Aisle(self)

    def RLP_recur(self):
        aisle_data = self.prod[self.knockoff]
        aisle_data0 = aisle_data[0:11]
        if aisle_data[0:8] == 'Aisle AA':
                rlp='''>>\tLast pick was: {}, {}.\n\tPick {} of {} each.\n'''.format(aisle_data0,
                self.Item_description, str(self.say_qty), str(self.order_dict[self.knockoff]))
                print(rlp)
        else:
            aisle_data1 = aisle_data[0:8]
            aisle_data2 = aisle_data[22:24]
            aisle_data3 = aisle_data[12:16]
            rlp='''>>\tLast pick was: {}-{} | slot {}.\n\t{}.\n\tPick {} of {} each.\n'''.format(aisle_data1, aisle_data2, aisle_data3,
            self.Item_description, str(self.say_qty), str(self.order_dict[self.knockoff]))
            print(rlp)

    def HMM(self):
        self.ListOf_AllQuantity = [self.order_dict[item] for item in self.order_list0]            # ListOfAllQuantity in the order list
        self.SumOfQuantity = sum(self.ListOf_AllQuantity)

        print()
        if self.SumOfQuantity>1 and len(self.order_list0) > 1:
            print('>>\t'+str(self.SumOfQuantity)+ ' items in '+ str(len(self.order_list0))+ ' locations.')
        elif self.SumOfQuantity>1 and len(self.order_list0) ==1:
            print('>>\t'+str(self.SumOfQuantity)+ ' items in '+ str(len(self.order_list0))+ ' location.')
        else:
            print('>>\t'+str(self.SumOfQuantity)+ ' item in '+ str(len(self.order_list0))+ ' location.')
    
    def DN(self):
        print()
        deliver = input('Deliver now? | ')
        if deliver == 'yes':
            InventorySys.Printer(self)
        elif deliver == 'no':
            pass
        elif deliver == 'SA.c':
            pass
        else:
            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            deliver = input('Deliver now? ')

    def RLP(self):
        try:
            self.last_pick
        except AttributeError:
            InventorySys.RLP_recur(self)
        else:
            InventorySys.RLP_recur(self)
        
    def Stage(self):
        while True:
            self.say_Stagenum=say_Stagenum=input('Stage number? | ')
            if say_Stagenum==str(self.Stage_numb):
                while True:
                    self.next_assignment=next_assignment=input('Assignment complete! For next assignment, say ready: ')
                    print()
                    if next_assignment=='ready':
                        self.tally != None
                        del self.newstacklist
                        del self.knockoff
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
                    elif next_assignment == 'SA.c':
                        pass
                    else:
                        print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                        InventorySys.help(self)
            elif say_Stagenum == 'SA.c':
                pass
            else: 
                print(' >>\t Wrong '+str(say_Stagenum)+ ', Try again! Deliver to Stage 0'+str(self.Stage_numb))
                print()
                pass

    def Printer(self):
        print('Picking complete!')
        while True:
            Printer = input('Printer? | ')
            print()
            try:
                assert Printer in ['2','3']
            except AssertionError:
                if Printer == 'RLP.c':
                    InventorySys.RLP(self)
                elif Printer == 'SA.c':
                    pass
                else:
                    while True:
                        select_Printer = input(Printer+'? TIMELESS '+Printer+'? correct? | ')
                        if select_Printer == 'yes':
                            print(' >>\t TIMELESS '+Printer+' not found. Try again!')
                        elif select_Printer == 'SA.c':
                            pass
                        elif select_Printer == 'no':
                            InventorySys.Printer(self)
                        else: 
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            else:
                self.Stage_numb = Stage_numb = self.Stage_numb
                select_Printer = input(Printer+'? TIMELESS '+Printer+'? correct? | ')
                if select_Printer == 'yes' and self.self_collect == 'no':
                    print('Deliver to Stage 0'+str(Stage_numb)+ '\n')
                    InventorySys.Stage(self)
                elif select_Printer == 'yes' and self.self_collect == 'yes':
                    self.Stage_numb = 10
                    print('Deliver to Stage 0'+str(self.Stage_numb)+ '\n')
                    InventorySys.Stage(self)
                elif select_Printer == 'no':
                    pass
                elif select_Printer == 'SA.c':
                    pass
                else: 
                    print(' >>\t I can\'t hear you. Please speak up a bit.\n')

    def Recur(self):
        self.start = start = input('VOICE picking. Directive picking. To receive work, say ready:  ')
        while True:
            if start == 'ready':
                self.password = password = input('Password? ')
                while True:
                    if password == '1234':
                        InventorySys.Queuing(self)
                    else:
                        password = input(' >>\t Wrong '+password+'. Try again! Password? ')
                        if password == 'SA.c':
                           pass
                        else:
                            pass
            elif start == 'SA.c':
                pass
            else: 
                start = input(' >>\t I can\'t hear you. Please speak up a bit. To receive work, say ready: ')
                if start == 'SA.c':
                    pass
                else:
                    pass

    def Queuing(self):
        print()
        
        self.stacklist=input('Load Assignment: | ')
        self.self_collect =  input('Self Collect? | ')
        print()
        self.stacklist = self.stacklist.split()
        
        self.key = key = []
        self.quanti = quanti = []
        for item in self.stacklist:
            demo = item[0:4]
            quan = item[5:]

            try:
                quan = math.floor(float(quan))
            except ValueError:
                print(' >>\tQuantity must be whole number > zero. Try again!')
                InventorySys.Queuing(self)

            key.append(demo)
            quanti.append(quan)
        self.order_dict = dict(zip(key, quanti))

        for item in quanti:
            try:
                if item>0:
                    pass
                else:
                    raise Exception
            except Exception:
                print(' >>\tQuantity must be > zero. Try again!')
                InventorySys.Queuing(self)
        InventorySys.self_collect(self)


class Stack:
    def Aisle(self):
        self.prod ={
                    'CA11': 'Aisle AA-07 Carling (CA11) | 11 gal keg',         'CA22': 'Aisle AA-11 Carling (CA22) | 22 gal keg',    
                    'FO11': 'Aisle AA-01 Fosters (FO11) | 11 gal keg',         'FO22': 'Aisle AA-06 Fosters (FO22) | 22 gal keg',      
                    'CO11': 'Aisle AA-05 Coors Lite (CO11) | 11 gal keg',      'CO22': 'Aisle AA-02 Coors Lite (CO22) | 22 gal keg',    
                    'JS11': 'Aisle AA-12 John Smiths (JS11) | 11 gal keg',     'JS22': 'Aisle AA-08 John Smiths (JS22) | 22 gal keg',    
                    'MA11': 'Aisle AA-09 Madri Lager (MA11) | 11 gal',         'GD11': 'Aisle AA-10 Guiness Draughts (GS11) | 11 gal keg',
                    'SA11': 'Aisle AA-13 Stella Attoires (SA11) | 10.5 gal',   'TS11': 'Aisle AA-14 Trophy Special (TS11) | 11 gal keg',
                    'TB09': 'Aisle AA-16 Theakson Bitters (TB09) | 09 gal keg','PN11': 'Aisle AA-04 Peroni 4.6 (PN11) | 11 gal keg',
                    'BI11': 'Aisle AA-15 Birra Moretti (BI11) | 11 gal keg',

                    'AB75': 'Aisle BE-79-A-03 7683 01 Absolut Vodka (AB40) | 40% alc', 
                    'SM75': 'Aisle BE-47-A-01 1118 01 Smirnoff Vodka (SM37) | 38% alc', 
                    'PE7L': 'Aisle BL-50-A-02 9785 12 Britvic Pepsi Cola Max | 7lt Bib', 
                    'CE35': 'Aisle BA-90-A-03 3248 03 Corona Extra NBA (CE35) | 4.5% alc',
                    'DP30': 'Aisle BA-04-A-02 0530 02 Desperados Tequila Beer (DP04) | 4% alc',
                    'FG1L': 'Aisle BB-86-A-16 3005 10 Famous Grouse Whisky | 40.5% alc'
                    }

        self.Stage_num = Stage_num = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15',
                                      '16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
        self.Stage_numb = choice(Stage_num)

        for item in self.key:
            try:
                assert item in self.prod
            except AssertionError:
                print('>>\t',item ,'not found. Try again!')
                InventorySys.Queuing(self)
            else:
                pass

        self.value = value = []
        for item in self.prod:
            if item in self.key:
                demo0 = (self.prod[item])[0:11]
                value.append(demo0)

        self.order_list0 = []
        for jtem in self.prod:
            if jtem in self.key:
                new_list = list(map(lambda s: jtem, sorted(value)))
                new_list0 = (new_list[0])[0:8]
                self.order_list0.append(new_list0)

        try:
            self.order_list0 = copy.copy(self.newstacklist)
        except AttributeError:
            self.order_list0 = copy.copy(self.order_list0)
        else:
            pass
           
        try:
            self.counter2 != 0
        except AttributeError:
            pass
        else:
            try:
                try:
                    if self.skips != 'yes':
                        raise Exception
                    else:
                        pass
                except AttributeError:
                    pass

                self.newstacklist
            except AttributeError:
                self.order_list0 = copy.copy(self.order_list1)
            except Exception:
                try:
                    counter1 == 0
                except UnboundLocalError:
                    self.order_list0 = copy.copy(self.order_list0)
                else:
                    self.order_list0 = copy.copy(self.newstacklist)
            else:
                counter1 = 0
                self.order_list0 = copy.copy(self.newstacklist)
            print('Order list in RT: ',self.order_list0)
            print()


        while True:
            for item in self.order_list0:
                self.uprod = uprod = self.prod[item]
                self.uprod = uprod[0:8]

                try:
                    self.knockoff_val = (self.prod[self.knockoff])[0:8]
                    if self.knockoff_val == self.uprod:
                        raise Exception
                    else:
                        pass
                except AttributeError:
                    self.tally = None
                except Exception:
                    if self.uprod == 'Aisle AA':
                        Stack.verify_keg(self)                            
                    else:
                        Stack.verify_bottle(self)
                
                if self.uprod == 'Aisle AA':                            #Kegs
                    self.status = input(self.uprod+': ')

                    while True:
                        self.prodd = prodd = copy.copy(self.uprod)
                        if self.status == 'ready':
                            while True:
                                Stack.verify_keg(self)
                        elif self.status == 'HMM.c':
                            InventorySys.HMM(self)
                            print()
                            self.status = input(prodd+': ')
                        elif self.status == 'AS.c':
                            Stack.Aisle_summary(self)
                            self.status = input(self.prodd+': ')

                        elif self.status == 'SA.c':
                            self.status = input(self.uprod+': ')

                        elif self.status == 'RLP.c' and self.tally == None:
                            print('\n>>\tRepeat last pick not allowed!')
                            self.status = input(prodd+': ')
                        elif self.status == 'RLP.c' and self.tally != None:
                            InventorySys.RLP(self)
                            self.status = input(prodd+': ')

                        elif self.status == 'DN.c' and self.tally !=None:
                            InventorySys.DN(self)
                            self.status = input(prodd+': ')
                        elif self.status == 'DN.c' and self.tally == None:
                            print('>>\tDeliver now not allowed!\n')
                            self.status = input(prodd+': ')

                        elif self.status == 'SS.c':
                            Stack.skip_slot(self)
                            Stack.Aisle(self)
                        else:
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                            self.status = input(prodd+': ')
                            
                elif self.uprod != 'Aisle AA':                          #Bottles
                    self.status = input(self.uprod+': ')
                    while True:
                        self.prodd = prodd = copy.copy(self.uprod)
                        if self.status == 'ready':
                            while True:
                                Stack.verify_bottle(self)
                        elif self.status == 'HMM.c':
                            InventorySys.HMM(self)
                            print()
                            self.status = input(prodd+': ')
                        elif self.status == 'AS.c':
                            Stack.Aisle_summary(self)
                            self.status = input(self.prodd+': ')
                        elif self.status == 'SA.c':
                            self.status = input(self.uprod+': ')
                        elif self.status == 'RLP.c' and self.tally == None:
                            print('Repeat last pick not allowed!')
                            self.status = input(prodd+': ')
                        elif self.status == 'RLP.c' and self.tally != None:
                            InventorySys.RLP(self)
                            self.status = input(prodd+': ')
                        
                        elif self.status == 'DN.c' and self.tally != None:
                            InventorySys.DN(self)
                            self.status = input(prodd+': ')
                        elif self.status == 'DN.c' and self.tally == None:
                            print('>>\tDeliver now not allowed!\n')
                            self.status = input(prodd+': ')

                        elif self.status == 'SS.c':
                            Stack.skip_slot(self)
                            Stack.Aisle(self)

                        else: 
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
                            self.status = input(prodd+': ')                                                                 
                else: 
                    print(' >>\t Please see your supervisor!')
                    InventorySys.Queuing(self)                 
    
    def Dial0_kegs(self):
        self.say_num = say_num = input((self.aisle_num)+': ')
        if say_num == self.aisle_num:
            print()
            self.knockoff = Stack.pop(self)
            self.newstacklist = copy.copy(self.order_list0)
            Stack.Kegs(self)
        
        elif say_num == 'HMM.c':
            InventorySys.HMM(self)
            print()
        
        elif say_num == 'SA.c':
            pass

        elif say_num == 'AS.c':
            Stack.Aisle_summary(self)

        elif say_num == 'RLP.c' and self.tally == None:
            print('Repeat last pick not allowed!')

        elif say_num == 'RLP.c' and self.tally != None:
            InventorySys.RLP(self)
        
        elif say_num == 'DN.c' and self.tally != None:
            InventorySys.DN(self)

        elif say_num == 'DN.c' and self.tally == None:
            print('>>\tDeliver now not allowed!\n')

        elif say_num == 'SS.c':
            Stack.skip_slot(self)
            Stack.Aisle(self)
        else:
            print(' >>\t Wrong check digit '+str(self.aisle_num)+'. Try again!')

        
    def Dial0_bottles(self):
        self.say_num = say_num = input(str(self.seg)+' | '+str(self.check)+': '+self.check_digit+': ')
        if say_num == str(self.check_digit):
            print()
            self.knockoff = Stack.pop(self)
            self.newstacklist  = copy.copy(self.order_list0)
            Stack.Bottles(self)
        
        elif say_num == 'HMM.c':
            InventorySys.HMM(self)
            print()
        
        elif say_num == 'SA.c':
            pass

        elif say_num == 'AS.c':
            Stack.Aisle_summary(self)

        elif say_num == 'RLP.c' and self.tally == None:
            print('Repeat last pick not allowed!')

        elif say_num == 'RLP.c' and self.tally != None:
            InventorySys.RLP(self)
        
        elif say_num == 'DN.c' and self.tally != None:
            InventorySys.DN(self)

        elif say_num == 'DN.c' and self.tally == None:
            print('>>\tDeliver now not allowed!\n')

        elif say_num == 'SS.c':
            Stack.skip_slot(self)
            Stack.Aisle(self)
        else:
            print(' >>\t Wrong check digit '+str(self.aisle_num)+'. Try again!')


    def Kegs(self):
        self.knockoff = knockoff = self.knockoff
        if knockoff in self.order_dict:
            self.quantity = self.order_dict[knockoff]
            self.Item_description = (self.prod[knockoff])[12:]
            print('Pick '+str(self.quantity)+' each. ', end = '')
            print(self.Item_description)
        
        while True:
            self.say_qty = input('Quantity? | ')

            try:
                if self.say_qty == 'SA.c':
                    print('Pick '+str(self.quantity)+' each. ', end = '')
                    print(self.Item_description)
                else:
                    raise ValueError
            except ValueError:
                try:
                        int(self.say_qty) == self.quantity
                except ValueError:
                        print('>>\t Error: Wrong input! Try again\n')
                else:
                    if int(self.say_qty) == int(self.quantity):
                        Stack.Keg_repeater(self)                                                    
                    elif int(self.say_qty) > int(self.quantity):
                        self.print_err = ' >>\tYou said {}, I only asked for {}.\n\tTry again, pick {} each.\n\t{}'.format(str(self.say_qty),
                                                str(self.quantity), str(self.quantity), self.Item_description)
                        print(self.print_err)
                        print()
                    else:
                        self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I asked for '+str(self.quantity)+
                                                        '.\n\t Is this a short product? | ')
                        if short_prod=='yes':
                            Stack.Keg_repeater(self)
                            InventorySys.Printer(self)
                            break
                        elif short_prod == 'no':
                            pass
                        elif short_prod == 'HMM.c':
                            InventorySys.HMM(self)
                            print()
                        elif short_prod == 'SA.c':
                            self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I asked for '+str(self.quantity)+
                                                        '.\n\t Is this a short product? | ')
                        else:
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')

    def Bottles(self):
        self.knockoff = knockoff = self.knockoff
        if self.knockoff in self.order_dict:
            self.quantity = self.order_dict[knockoff]
            self.Item_description = (self.prod[self.knockoff])[25:]
            print('Pick '+str(self.quantity)+' each. ', end = '')
            print(self.Item_description)

        while True:
            self.say_qty = input('Quantity? | ')

            try:
                if self.say_qty == 'SA.c':
                    print('Pick '+str(self.quantity)+' each. ', end = '')
                    print(self.Item_description)
                else:
                    raise ValueError
            except ValueError:
                try:
                    int(self.say_qty) == self.quantity
                except ValueError:
                    print('>>\t Error: Wrong input! Try again\n')
                else:
                    if int(self.say_qty) == self.quantity:
                        Stack.Bottle_ID(self) 
                    elif int(self.say_qty) > self.quantity:
                        self.print_err = ' >>\tYou said {}, I only asked for {}.\n\tTry again, pick {} each.\n\t{}'.format(str(self.say_qty),
                                                str(self.quantity), str(self.quantity), self.Item_description)
                        print(self.print_err)
                        print()
                    else:
                        self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I asked for '+str(self.quantity)+
                                                        '.\n\t Is this a short product? | ')
                        print()
                        if short_prod=='yes':
                            Stack.Bottle_ID(self)
                            InventorySys.Printer(self)
                            break
                        elif short_prod=='no':
                            pass
                        elif short_prod == 'HMM.c':
                            InventorySys.HMM(self)
                            print()
                        elif short_prod == 'SA.c':
                            self.short_prod=short_prod=input(' >>\tYou said '+str(self.say_qty)+', I asked for '+str(self.quantity)+
                                                        '.\n\t Is this a short product? | ')
                        else:
                            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            
            

    def Keg_repeater(self):
        print()
        print('Items picked: | '+str(self.say_qty)+' ['+str(self.knockoff)+'] ' +'\nItems on queue: | '+str(self.newstacklist)+'\n')
        self.prodd = copy.copy(self.prod)
        
        if len(self.newstacklist)>0:
            print()
            Stack.Aisle(self)  
        else:
            self.last_pick = None
            InventorySys.Printer(self) 

    def Bottle_ID(self):
        while True:
            self.item_barcode = item_barcode = self.prod
            self.item_barcode = (item_barcode[self.knockoff])[17:21]
            self.item_no = item_no = input('Item number | '+self.item_barcode+ ': | ')
            self.confirm_item_no = input(str(item_no)+ ' corect? | ')
            print()
            
            if self.confirm_item_no == 'yes' and item_no == self.item_barcode:
                print('Items picked: | '+str(self.say_qty)+' ['+str(self.knockoff)+'] '+'\nItems on queue: | '+str(self.newstacklist)+'\n')
                self.prodd = copy.copy(self.prod)

                if len(self.newstacklist)>0:
                    print()
                    Stack.Aisle(self)
                else:
                    self.last_pick = None
                    InventorySys.Printer(self)

            elif self.confirm_item_no == 'yes' and item_no != self.item_barcode:
                print('>>\tInvalid '+ item_no+'. Try again!\n')
            elif self.item_no == 'SA.c':
                self.item_no = item_no = input('Item number | '+self.item_barcode+ ': | ')
            else:
                if self.confirm_item_no == 'no':
                    pass
    
    def verify_keg(self):
        for item in self.order_list0:
            self.uprod =uprod = self.prod[item]
            self.aisle_num = uprod[9:11]
            self.uprod = uprod[0:8]
            while True:
                Stack.Dial0_kegs(self)

    def verify_bottle(self):
        for item in self.order_list0:
            self.uprod = uprod = self.prod[item]
            self.seg = uprod[22:24]
            self.check_digit = uprod[9:11]
            self.check = uprod[12:16]
            self.uprod = uprod[0:8]
            while True:
                Stack.Dial0_bottles(self)

    def Aisle_summary(self):
        try:
            aisle = self.knockoff_val
            if aisle == self.knockoff_val:
                raise AttributeError
            else:
                pass
        except AttributeError:
            self.uprod = uprod = self.uprod
            aisle = uprod

        counter = 0
        new_value = []
        for item in self.value:
            if item.startswith(aisle):
                new_value.append(item)
                counter += 1                                                # counter of inventories on the same aisle.

        final = []
        for item in self.prod:
            k = self.prod[item]
            k = k[0:11]
            if k in new_value:                                             
                final.append(item)

        ListOfQuantities = [self.order_dict[item] for item in final]        # A List of quantities to pick
        items = sum(ListOfQuantities)                                       # Sum of all elements in ListOfQuantities
        final.clear()

        print()
        if items>1 and counter>1:
            print('>>\t'+str(items)+ ' items in '+ str(counter)+ ' locations.')
        elif items>1 and counter==1:
            print('>>\t'+str(items)+ ' items in '+ str(counter)+ ' location.')
        else:
            print('>>\t'+str(items)+ ' item in '+ str(counter)+ ' location.')

    def skip_slot(self):
        self.counter2 = 1
        self.skips = input('Skip slot? | ')
        try:
            assert self.skips in ['yes', 'no']
            if self.skips == 'yes':
                pass
            elif self.skips == 'SA.c':
                Stack.skip_slot(self)
            else:
                Stack.Aisle(self)
        except AssertionError:
            print(' >>\t I can\'t hear you. Please speak up a bit.\n')
            Stack.skip_slot(self)
        

        try:
            self.newstacklist
        except AttributeError:
            self.skip = copy.copy(self.order_list0)
            self.skip0 = self.skip[0]
            del self.skip[0]
            self.skip.append(self.skip0)
            self.order_list1 = copy.copy(self.skip)
        else:
            print()
            self.skip1 = copy.copy(self.newstacklist)
            self.skip2 = self.skip1[0]
            del self.skip1[0]
            self.skip1.append(self.skip2)
            self.newstacklist = copy.copy(self.skip1)


    def pop(self):
        order = self.order_list0[0]
        del self.order_list0[0]
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
            self.key = key = input('Selecting Operator: | ')
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
