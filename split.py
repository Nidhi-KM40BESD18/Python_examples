import re

text = "Ten 10, Twenty 20, Thirty 30"
result = re.split("\D+", text)
for i in result:
    print(i)
