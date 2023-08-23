

prod = {'CA11':'Aisle AA-07',  'CA22':'Aisle AA-11',
                    'FO11':'Aisle AA-01',   'FO22':'Aisle AA-06',
                    'BM11':'Aisle AA-15',   'BM22':'Aisle AB-32',
                    'CO11':'Aisle AA-05',   'CO22':'Aisle AA-02',
                    'JS11':'Aisle AA-12',   'JS22':'Aisle AA-08', 
                    'MA11':'Aisle AA-09',   'GS11':'Aisle AA-10',
                    'SA11':'Aisle AA-13',   'TS11':'Aisle AA-14',
                    'TB09':'Aisle AA-16',   'PN11':'Aisle AA-04',
                    
                    'AB75': 'Aisle BE-79',
                    'SM75': 'Aisle BE-47',
                    'PE7L': 'Aisle BL-50',
                    'DP30': 'Aisle BA-04',
                    'CE35': 'Aisle BA-90',
                    'FG1L': 'Aisle BB-86'}


#short = ['Aisle AA-16', 'Aisle BE-79','Aisle AA-05', 'Aisle BB-86', 'Aisle BA-90', 'Aisle BA-04', 'Aisle AA-09']
short =[]
for i in prod:
    short0 = (prod[i])[0:11]
    short.append(short0)
print(sorted(short))

#short = ['CA11', 'CA22','CO11', 'FO11','SM75', 'CO22', 'FO22', 'BI11', 'BI22','AB75','PE7L']
long = []
for i in prod:

    if short0 not in short:
        continue
    else:
        new_list = list(map(lambda s: i, sorted(short)))
        new_list = (new_list[0])[0:8]
        #new_list = new_list[0]
        long.append(new_list)
print()
print(long)




"""key = ['CA11','FG1L', 'CA22','CO11', 'FO11', 'CE35', 'FO22', 'BI11', 'BI22','AB75']
value = ['Aisle AA-05','Aisle BE-79','Aisle AA-07','Aisle AA-11', 'Aisle AA-06', 'Aisle BB-86', 'Aisle BA-90','Aisle AA-01']

order = []
for i in prod:
    if i in key:
        new_list = list(map(lambda s: i, value))
        new_list = (new_list[0])[0:8]
        order.append(new_list)
print()
print('Key: ',order)

order_val = []
for i in prod:
    if prod[i] in value:
        new_list = list(map(lambda s: prod[i], key))
        new_list = (new_list[0])[0:]
        order_val.append(new_list)
print('Value: ',order_val)

res = dict(zip(order, order_val))
print('\nOrder Dictionary: ',str(res))"""



