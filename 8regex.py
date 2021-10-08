import re

text = '''arrived on the Indian subcontinent from Africa no later than 55,000 years ago.[24] Their long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity.[25] Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE.[26] By 1200 BCE, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest'''

patt = re.compile(r'[0-9].')
match = patt.finditer(text)

for i in match:
    print(i)


ip = "210.08.094.196"
string = re.sub('\.[0]+', '.', ip)
print(string)
