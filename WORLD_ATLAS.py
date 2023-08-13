import time

def escape():
    print("[!] Okay bye",user,"(:\n")
    exit()
print()
user=input("[prompt:]  Enter username: ")
print()
# This program that returns the captital of a nation when you supply thr nation
world_atlas = {"nigeria": "ABUJA", "togo": "LOME", "uk": "LONDON","scotland": "EDINBURG","wales": "CARDIFF","germany": "BERLIN",
                "benin": "PORT-NOVO","ghana": "ACCRA","cote d'ivoire": "YAMOUSSOUKRO","mali": "BAMAKO","niger": "NIAMEY","chad": 
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
                "greece": "ATHENS","austria": "VIENNA","croatia": "ZAGREB","macedonia": "SKOPJE","serbia": "BELGRADE","monaco": "monaco",
                "iceland": "REKJAVIK","armenia": "YEREVAN","azerbaijan": "BAKU","moldova": "CHISINAU","belarus": "MINSK","ireland": 
                "DUBLIN","andorra": "ANDORRA LA VELLA","bosnia": "SARAJEVO","montenegro": "PODGORICA","san marino": "SAN MARINO",
                "liechteinstein": "LIECHTENSTEIN","brazil": "BRASILIA","paraguay": "ASUNCION","uruguay": "MONTEVIDEO","columbia": "BOGOTA",
                "peru": "LIMA","ecuador": "QUITTO","argentina": "BUENOS AIRES","bolivia": "SUCRE","venezuela": "CARACAS","suriname": 
                "PARAMARIBO","guyana": "GEORGETOWN","chile": "SANTIAGO DE CHILE","trinidad and tobago": "PORT OF SPAIN","panama": 
                "PANAMA CITY","honduras": "TEGUCIGALPA","el savaldor": "SAN SAVALDOR","nicaragua": "MANAGUA","mexico": "MEXICO CITY",
                "guatemala": "GUATEMALA CITY","cuba": "HAVANA","bahamas": "NASSAU","st kitts and nevis": "BASSETERRE","haiti": 
                "PORT-AU-PRINCE","jamaica": "KINGSTON","grenada": "ST GEORGE'S","costa rica": "SAN JOSE","dominican republic": 
                "SANTO DOMINIGO","greenland": "NUUK","usa": "WASHINGTON DC","canada": "TORONTO","belize": "BELMOPAN","barbados": 
                "BRIDGETOWN","st lucia": "CASTRIES","antigua and barbuda": "ST JOHN'S","dominica": "ROSEAU","russia": "MOSCOW","china": 
                "BEIJIN","mongolia": "ULAAN BAATAR","uzbekistan": "TASHKENT","turkmenistan": "ASHGABAT","kazakhstan": "ASTANA","krygyzstan":
                "BISHIKEK","tajikistan": "DUSHANBE","syria": "DAMASCUS","pakistan": "ISLAMABAD","turkey": "ANKARA","afghanistan": "KABUL",
                "iran": "TEHRAN","iraq": "BAGHDAD","israel": "TEL-AVIV","palestine": "JERUSALEM","lebanon": "BEIRUT","jordan": "AMMAN",
                "india": "NEW DELHI","sri lanka": "COLOMBO","maldives": "MALE","south korea": "SEOUL","north korea": "PYONGYANG",
                "japan": "TOKYO","bangladesh": "DHAKA","nepal": "KATHMANDU","bhutan": "THIMHPU","thailand": "BANGKOK","laos": "HANNOI",
                "vietnam": "LAOS","cambodia": "PHNOM PHEN","brunei": "BANDAR SERI BEGAWAN","malaysia": "KUALA LUMPUR","indonesia": "JAKARTA",
                "singapore": "SINGAPORE","taiwan": "TAI PEI","philippines": "MANILA","new guinea": "PORT MORESBY","australia": "CANBERRA",
                "new zealand": "WELLINGTON","oman": "MUSCAT","saudi arabia": "RIYAHD","kuwait": "KUWAIT","yemen": "SANA'A","qatar": "DOHA",
                "bahrain":"BAHRAIN","uae": "ABU DHABI","myanmar": "NAYPYIDAW","east timor": "DILI","fiji": "SUVA","solomon island":
                "HONIARA","micronesia": "PALIKIR","tuvalu": "FUNAFUTI","vanuatu": "PORT VILA","kiribati": "TARAWA","marshall islands": 
                "MAJURO","nauru": "YAREN","palau": "NGERULMUD"}

while True:
    nation=input("[prompt:]  Enter name of country: ").lower()
    for i in range(3):
        if nation in world_atlas:
            print("[output:] ",nation.upper(),"|",world_atlas[nation])
            print()

            if i==2:
                esc=input("""Would you like to exit app?...
Enter yes to exit and otherwise to stay:
""").lower()
                print()
                if esc=="yes":
                    escape()
                else:
                    pass
                    #nation=input("Enter name of country: ").lower()
            else:
                nation=input("Enter name of country: ").lower()
        else:
            print("[error:] "+nation.title()+" not found! Enter correct spelling\n")
            esc=input("""Would you like to exit app?...
Enter yes to exit and otherwise to stay:
""").lower()
            print()
            if esc=="yes":
                escape()
            else:
                nation=input("Enter name of country: ").lower()
    


