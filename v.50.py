import random
for i in range (10):
    r = random.randint(30,50)
    print(r)
print()

for i in range (5):
    r = random.uniform(1, 10)
    print(r)
print()

for i in range(7):
    r = random.gauss(50, 25)
    print(r)
print()

a = 1
while a < 100:
    if a > 50:
        break
    print(a)
    a += 1
print()

a = str(input("Skriv en string "))
b = int(input("Skriv en integer "))
try:
    print(a + b)
except:print("Vi försökte slå samman en int och en str och därför blev det error.")
print()

try:
    print(0/0)
except ZeroDivisionError:
    print("0/0 går inte") #Utan try/except så skulle proggrammet krasha.
print()

#Här visar jag programmet var filen är, på nästa rad läser jag den i koden. På sista skriver jag ut den
file = open("Martincool.txt", "r")
x = file.read()
print(x)

#Här hittar jag och filen och skriver in Martin cool kid på raden efter.
file = open("C:\\Users\\EliasAdestam\\Desktop\\Fyllning.txt", "w")
file.write("Martin cool kid")