import re
text = '''The Ganges (/ˈɡændʒiːz/ GAN-jeez) or Ganga (/ˈɡʌŋɡə/ GUNG-gə, Hindustani: [ˈɡəŋɡaː]) is a trans-boundary river of Asia which flows through India and Bangladesh. The 2,525 km (1,569 mi) river rises in the western Himalayas in the Indian state of Uttarakhand, and flows south and east through the Gangetic plain of North India into Bangladesh, where it empties into the Bay of Bengal. It is the third largest river on Earth by discharge.[9]

The main stem of the Ganges begins at the town of Devprayag,[1] at confluence of the Alaknanda, which is the source stream in hydrology because of its greater length, and the Bhagirathi, which is considered the source stream in Hindu mythology.[1]'''

p = re.compile(r'\w*h\b')  #letter ending with h

match  = p.finditer(text)

for i in match:
    print(i)
