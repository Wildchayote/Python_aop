from random import random, choice
import time
import pandas as pd
import openpyxl



class Atlas:
    name_list =[]
    result_list1 =[]
    result_list2 =[]
    counter = 0
    def exception_dial(self):
        print()
        self.marks =0
        self.marks1 =0

        try:
            questions=int(input("How many questions would you like to try? "))
            print()
        except (KeyboardInterrupt, ValueError):
            print("\n\t[error!] Something went wrong!\n")
            Atlas.exception_dial(self)
        else:
            pass
        
        while True:
            
            world_atlas = {"nigeria": "ABUJA", "togo": "LOME", "uk": "LONDON","scotland": "EDINBURG","wales": "CARDIFF","germany": "BERLIN",
                            "benin": "PORT NOVO","ghana": "ACCRA","cote d'ivoire": "YAMOUSSOUKRO","mali": "BAMAKO","niger": "NIAMEY","chad": 
                            "N'JAMENA","burkina faso": "OAGADOUGOU","senegal": "DAKAR","liberia": "MONROVIA","sierra leone": "FREETOWN","gabon": 
                            "LIBREVILLE","guinea": "CONAKRY","cape verde": "PRAIA","western sahara": "AL-AIUN","mauritania": "NOUAKCHOTT","morocco":
                            "RABAT","algeria": "ALGIERS","libya": "TRIPOLI","tunisia": "TUNIS","egypt": "CAIRO","sudan": "KHARTOUM","south sudan": 
                            "JUBA", "eritrea": "ASMARA","djibouti": "DJIBOUTI","somalia": "MOGADISHU","ethiopia": "ADISABABA","rwanda": "KIGALI",
                            "uganda": "KAMPALA","burundi": "BUJUMBURA","tanzania": "DODOMA","dr congo": "KINSHASA","congo": "BRAZAVILLE","car": 
                            "BANGUI","gambia": "BANJUL","guinea bissau": "BISSAU","cameroon": "YAOUNDE","angola": "LUANDA","zambia": "LUSAKA",
                            "namibia": "WINDHOEK","seychelles": "VICTORIA","mozambique": "MAPUTO","kenya": "NAIROBI","malawi": "LILONGWE","zimbabwe":
                            "HARARE","mauritius": "PORT-LOUIS","comoros": "MORONI","lesotho": "MASERU","swaziland": "MBABANE","south africa": 
                            "CAPETOWN","madagascar": "ANTANANARIVO","botswana": "GABORONE","equatorial guinea": "MALABO","sao tome de principe": 
                            "SAO TOME","france": "PARIS","spain": "MADRID","italy": "ROME","portugal": "LISBON","belgium": "BRUSSELS","poland": 
                            "WARSAW","netherlands": "AMSTERDAM","estonia": "TALLINN","latvia": "RIGA","lithuania": "VILNIUS","luxemborg": "LUXEMBORG",
                            "denmark": "COPENHAGEN","norway": "OSLO","finland": "HELSINKI","sweden": "STOCKHOLM","ukraine": "KIEV","malta": "VALLETTA",
                            "albania": "TIRANA","slovakia": "BRATISLAVA","slovenia": "LJUBLJANA","czech republic": "PRAGUE","switzerland": "BERN",
                            "vatican city": "HOLY SEE","bulgaria": "SOFIA","romania": "BUCHAREST","hungary": "BUDAPEST","cyprus": "NICOSIA",
                            "greece": "ATHENS","austria": "VIENNA","croatia": "ZAGREB","macedonia": "SKOPJE","serbia": "BELGRADE","monaco": "MONACO",
                            "iceland": "REKJAVIK","armenia": "YEREVAN","azerbaijan": "BAKU","moldova": "CHISINAU","belarus": "MINSK","ireland": 
                            "DUBLIN","andorra": "ANDORRA LA VELLA","bosnia": "SARAJEVO","montenegro": "PODGORICA","san marino": "SAN MARINO",
                            "liechtenstein": "LIECHTENSTEIN","brazil": "BRASILIA","paraguay": "ASUNCION","uruguay": "MONTEVIDEO","columbia": "BOGOTA",
                            "peru": "LIMA","ecuador": "QUITTO","argentina": "BUENOS AIRES","bolivia": "SUCRE","venezuela": "CARACAS","suriname": 
                            "PARAMARIBO","guyana": "GEORGETOWN","chile": "SANTIAGO DE CHILE","trinidad and tobago": "PORT OF SPAIN","panama": 
                            "PANAMA CITY","honduras": "TEGUCIGALPA","el savaldor": "SAN SAVALDOR","nicaragua": "MANAGUA","mexico": "MEXICO CITY",
                            "guatemala": "GUATEMALA CITY","cuba": "HAVANA","bahamas": "NASSAU","st kitts and nevis": "BASSETERRE","haiti": 
                            "PORT-AU-PRINCE","jamaica": "KINGSTON","grenada": "ST GEORGE'S","costa rica": "SAN JOSE","dominican republic": 
                            "SANTO DOMINIGO","greenland": "NUUK","usa": "WASHINGTON DC","canada": "TORONTO","belize": "BELMOPAN","barbados": 
                            "BRIDGETOWN","st lucia": "CASTRIES","antigua and barbuda": "ST JOHN'S","dominica": "ROSEAU","russia": "MOSCOW","china":
                            "BEIJIN","mongolia": "ULAAN BAATAR","uzbekistan": "TASHKENT","turkmenistan": "ASHGABAT","kazakhstan": "ASTANA","krygyzstan":
                            "BISHIKEK","tajikistan": "DUSHANBE","syria": "DAMASCUS","pakistan": "ISLAMABAD","turkey": "ANKARA","afghanistan": "KABUL",
                            "iran": "TEHRAN","iraq": "BAGHDAD","israel": "TEL AVIV","palestine": "JERUSALEM","lebanon": "BEIRUT","jordan": "AMMAN",
                            "india": "NEW DELHI","sri lanka": "COLOMBO","maldives": "MALE","south korea": "SEOUL","north korea": "PYONGYANG",
                            "japan": "TOKYO","bangladesh": "DHAKA","nepal": "KATHMANDU","bhutan": "THIMHPU","thailand": "BANGKOK","laos": "HANNOI",
                            "vietnam": "LAOS","cambodia": "PHNOM PHEN","brunei": "BANDAR SERI BEGAWAN","malaysia": "KUALA LUMPUR","indonesia": "JAKARTA",
                            "singapore": "SINGAPORE","taiwan": "TAI PEI","philippines": "MANILA","new guinea": "PORT MORESBY","australia": "CANBERRA",
                            "new zealand": "WELLINGTON","oman": "MUSCAT","saudi arabia": "RIYAHD","kuwait": "KUWAIT","yemen": "SANA'A","qatar": "DOHA",
                            "bahrain":"BAHRAIN","uae": "ABU DHABI","myanmar": "NAYPYIDAW","east timor": "DILI","fiji": "SUVA","solomon island":
                            "HONIARA","micronesia": "PALIKIR","tuvalu": "FUNAFUTI","vanuatu": "PORT VILA","kiribati": "TARAWA","marshall islands": 
                            "MAJURO","nauru": "YAREN","palau": "NGERULMUD"}
            
            print("Fab!", questions,"questions,...Let's go!")
            for i in range(questions):
                keys = list(world_atlas)
                country = choice(keys)
                counter = self.marks + self.marks1 

                print("\nQuestion",counter+1,":")
                print("What is the capital of",country.upper(),"|")
                answer=input("Answer: ").upper()
                
                if answer==world_atlas[country]:
                    print(">>\tCorrect!")
                    self.marks+=1
                    time.sleep(1)
                else:
                    print(">>\tWrong!:", end = '')
                    print("\tThe capital of",country.title(), "is", world_atlas[country].title())
                    self.marks1+=1
                    time.sleep(1)

            print()
            print('*** Loading result...')
            time.sleep(2)
            print("You scored ",self.marks,'/',questions)
            
            score = self.marks / questions
            if self.marks < questions*.5:
                time.sleep(2)
                print("\nYou scored",round(score*100,2),"%")
                print("You failed the quiz!...relaunch app to try again!\n")
                print('Launch: '+str(Atlas.counter)+ ' | '+self.name+'\'s turn!')
                Round_exce.Data_job(self)
                Atlas.exception_dial(self)
            else:
                self.marks>=questions*.5
                time.sleep(2)
                self.result = round(score*100,2)
                print("\nCongratulation!  You've passed the quiz... you scored",self.result,"%\n")
                if self.name == 'Bashir':
                    print('Launch: '+str(Atlas.counter)+ ' | Deola\'s turn!')
                elif self.name == 'Deola':
                    print('Launch: '+str(Atlas.counter)+ ' | Bashir\'s turn!')
                Round_exce.Data_job(self)
                Atlas.exception_dial(self)
            
    def save(self):
        self.res = dict(zip(Atlas.name_list, self.ress))
        print(self.res)
        Atlas.Log(self)
        exit()
        
    def Kounter(self):        
        Atlas.name_list.append(self.name)
        self.ress = [Atlas.result_list1, Atlas.result_list2]
        Atlas.counter+=1
        if Atlas.counter == self.attempts*2:
            Atlas.save(self)
        else:
            pass
        
    def Log(self):
        start_row = 0
        with pd.ExcelWriter("testing.xlsx", engine="openpyxl") as writer:
            df = pd.DataFrame(self.res)
            df.to_excel(writer, sheet_name = 'Result_Sheet', startrow=start_row, index=True)
            writer.save()

class Round_exce(Atlas):
    
    def Data_job(self):
        self.name = input('Username: ')
        try:
            assert self.name in ['Bashir', 'Deola']
        except AssertionError:
            print("Error: Name not registered. Try again!")
            Round_exce.Data_job(self)
        else:
            if self.name == "Bashir":
                try:
                    self.result
                except AttributeError:
                    Atlas.exception_dial(self)
                else:
                    Atlas.result_list1.append(int(self.result))
                    Atlas.Kounter(self)
            else:
                try:
                    self.result
                except AttributeError:
                    Atlas.exception_dial(self)
                else:
                    Atlas.result_list2.append(int(self.result))
                    Atlas.Kounter(self)

    def rounds(self):
        try:
            self.attempts=int(input("How many rounds would you like to go? "))
            print()
        except (KeyboardInterrupt, ValueError):
            print("\n\t[error!] Something went wrong!\n")
            Round_exce.rounds(self)
        else:
            pass

raund = Round_exce()
print()
raund.rounds()
raund.Data_job()
raund.exception_dial()
