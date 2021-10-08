import re
text = '''
1234565677
864540976
9879826394
6835875
3720745986'''

patt = re.compile(r'\b\d{5}[02468]\d{4}\b')

match = patt.finditer(text)

for i in match:
    print(i)
