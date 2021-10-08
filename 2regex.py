import re

text = '''Abascus absurdd abaondon allure amazed abbbas anant'''

'''patt = re.compile(r'[aA]b*')   # checks for b for 0 or more than that
match = patt.finditer(text)

for i in match:
    print(i)
'''

pattr = re.compile(r'[aA]b+') # checks for b 1 o more than that

match1 = pattr.finditer(text)

for i in match1:
    print(i)
