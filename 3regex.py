import re

text = '''India's holy Ganges River is devastatingly polluted, yet provides drinking water for over 400 million people — here's what it looks like. ... Untreated sewage flows directly into the river where people cook, bathe, and perform burial rites for the recently-deceased'''


patt = re.compile(r'\b\w*i\w*\b') #seaching i in word
match = patt.finditer(text)

for i in match:
    print(i)
