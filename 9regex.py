import re
string = 'orange776'
patt = re.compile(r'.*[0-9]$')
if patt.match(string):
    print('yes')
else:
    print('no')
