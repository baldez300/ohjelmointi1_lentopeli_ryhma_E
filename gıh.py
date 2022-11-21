"""fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("Lämpötila Celsius-asteina: " + str(celsius))
komento = input ("Anna komento: ")
while komento!="lopeta":
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")

print ("Toiminnot lopetettu.")
import random
noppa1 = noppa2 = heitot = 0
while (noppa1!=6 or noppa2!=6):
    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")
import random
toistot = 0
heitot_yhteensä = 0
while toistot < 100000:
    noppa1 = noppa2 = heitot = 0
    while (noppa1!=6 or noppa2!=6):
        noppa1 = random.randint(1,6)
        noppa2 = random.randint(1,6)
        heitot = heitot + 1
    #print(f"Tarvittiin {heitot:d} heittoa.")
    toistot = toistot + 1
    heitot_yhteensä = heitot_yhteensä + heitot
heitot_keskimäärin = heitot_yhteensä/toistot
print(toistot)
print(heitot_yhteensä)
print(heitot_keskimäärin)
print(f"Heitot keskimäärin: {heitot_keskimäärin:6.2f}")
komento = input ("Anna komento: ")
while komento!="lopeta" :
    if komento == "MAYDAY":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print("Näkemiin.")
print ("Toiminnot lopetettu.")"""
for luku in range(6):
    print ("Moi!")