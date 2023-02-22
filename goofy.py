Namn = input("Skriv ditt namn ")
len(Namn)
print(len(Namn))
print(Namn[0:3])
print(Namn.index("a")+ 1) #Jag gjorde om index till platsen i ordet med +1.
if Namn.islower():
    print("alla är små bokstäver")
else:
    print("alla bokstäver är inte små")