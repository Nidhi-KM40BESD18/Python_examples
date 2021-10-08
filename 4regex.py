import re

text = '''
450-987-1234
768-987-9875
457-568-6582
650-546-3243

mr. david
Mr Joseph
Mrs peter
Ms jenny
mr.ronald'''

patt1 = re.compile(r'[mM][r|rs|s]\.?.*\w*')
match = patt1.finditer(text)

for i in match:
    print(i)



