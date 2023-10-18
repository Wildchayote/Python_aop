from django.shortcuts import render, redirect
from django.http import HttpResponse
from . forms import AtlasForm
from . models import Nation



def country_form(request):
    if request.method == 'POST':
        form = AtlasForm(request.POST)
        if form.is_valid():
            nation_record = form.save()
            return redirect('get_capital', pk=nation_record.pk)
    else:
        form = AtlasForm()
    return render(request, 'country.html', {'form': form})

def get_capital(request,pk):
    nation_record = Nation.objects.get(pk=pk)
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
    nation = nation_record.nation.lower()
    
    for n in world_atlas:
        if nation in world_atlas:
            capital =  world_atlas[nation].upper()
        else:
            error = f'{[nation]} not found. Check spelling and try again!'
            capital =  error

    nation = nation_record.nation.title()
    nation_capital = Nation(nation=nation, capital = capital)
    nation_capital.save()

    if pk%2 != 0:
        Nation.objects.get(pk=pk).delete()  
    context = {'nation_record': nation_record, 'capital': capital}
    return render(request, 'capital.html', context)
