import re
text = 'day , date, week, month'
pattern = 'date'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)
