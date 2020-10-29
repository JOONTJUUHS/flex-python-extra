import re

phone = input("voer je mobile nummer in")

patern = "^06-?\d{8}$"

matches = re.findall(patern, input)

print(matches)

 if(len(matches) > 0):
        break


print("Bedankt nummer in juiste formaat:", matches[0])
