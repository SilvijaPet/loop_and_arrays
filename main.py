import random

print("============================ 1 uzduotis =======================")
# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.

for i in range(10):
    print("labas")

print("============================ 2 uzduotis =======================")
# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

for i in range(10):
    print(i)

print("============================ 3 uzduotis =======================")
# Sukurkite masyvą iš dešimties augalų pavadinimų.

augalai = ["Ąžuolas", "Beržas", "Pušis", 'Eglė', "Klevas", 'Rožė', 'Tulpė', 'Saulėgrąža', 'Levanda', 'Papartis']
print(augalai)

print("============================ 4 uzduotis =======================")
# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

for i in augalai:
    print (i)

print("============================ 5 uzduotis =======================")
# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).

augalai.reverse()
print(augalai)

print("============================ 6 uzduotis =======================")
# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

for number in range(10,51):
    if number % 2 == 0:
        print(number)

print("============================ 7 uzduotis =======================")
# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius)
# Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.)
# (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)

for i in range(10,50,2):
    if i % 10 == 0:
        continue
    print(i)

print("============================ 8 uzduotis =======================")
# Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;
count = 0
for i in range(21):
    if i % 2 == 0:
        count += 1
print(count)

print("============================ 9 uzduotis =======================")
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai,
# ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)

count = 0
for i in augalai:
    if len(i) < 5:
        count += 1

print(f"Trumpesniu zodziu nei 5 raides: {count}")

for i in augalai:
    if len(i) > 7:
        count += 1

print(f"Ilgesniu zodziu nei 7 raides: {count}")

print("============================ 10 uzduotis =======================")
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)

count = 0

for i in augalai:
    if 5 < len(i) < 10:
        count += 1
print(count)


print("============================ SUNKESNI =========================")
print("============================ 1 uzduotis =======================")
# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais vienoje eilutėje
# ir suskaičiuokite kiek tarp jų yra didesnių už 150.
# Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.

numbers = [random.randint(0,300) for num in range(0,300)]
# print(*numbers, sep=" ")

count = 0
symbol = []

for num in numbers:
    if num  > 150:
        count += 1
    if num > 275:
        symbol.append(f"[{num}]")
    else:
        symbol.append(str(num))

print(*symbol, sep=" ")
print("Skaičių didesnių už 150:", count)

print("============================ 2 uzduotis =======================")
# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

numbers = [num for num in range(0,3000)]
div_77 = [n for n in numbers if n % 77 == 0]

print(div_77, sep=",")

# nums = []

# for num in range(1,3000):
#     if num % 77 == 0:
#         nums.append(str(num))
#
# print(",".join(nums))

print("============================ 3 uzduotis =======================")
# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”

for i in range(25):
    print("*" * 25)

print("============================ 4 uzduotis =======================")
# Prieš tai nupieštam kvadratui nupieškite istrižaines, zaigzdutę pakeisdami kitu simboliu.
dydis = 25

for eilute in range(dydis):
    for stulpelis in range(dydis):

        if eilute == stulpelis or eilute + stulpelis == dydis - 1:
            print("X", end="")
        else:
            print("*", end="")

    print()
print("============================ 5 uzduotis =======================")
# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas.
# Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;

# Iškritus herbui
while True:
    coin = random.randint(0,1)
    if coin == 0:
        print("H")
        break
    else:
        print("S")

# Tris kartus iškritus herbui
print("-----------")
count_H = 0
while count_H < 3:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        count_H += 1
    else:
        print("S")

# Tris kartus iš eilės iškritus herbui;
print("-----------")
three_H = 0
while three_H < 3:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        three_H += 1
    else:
        print("S")
        three_H = 0

print("============================ 6 uzduotis =======================")
# Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25.
# Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: laimėtojo vardas”.
# Taškų kiekį generuokite funkcija random.randint(x,x).
# Žaidimą laimi tas, kas greičiau surenka 222 taškus. Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.

kazys_total = 0
petras_total = 0

while kazys_total < 222 and petras_total < 222:
    kazys_points = random.randint(5, 25)
    petras_points = random.randint(10, 20)

    kazys_total += kazys_points
    petras_total += petras_points

    # Nustatome partijos laimėtoją
    if kazys_points > petras_points:
        winner = "Kazys"
    elif petras_points > kazys_points:
        winner = "Petras"
    else:
        winner = "Lygiosios"

    print(f"Kazys: {kazys_points}, Petras: {petras_points} | Partiją laimėjo: {winner}")

# Galutinis laimėtojas
if kazys_total >= 222:
    print(f"\nŽaidimą laimėjo Kazys su {kazys_total} taškų!")
else:
    print(f"\nŽaidimą laimėjo Petras su {petras_total} taškų!")

print("============================ 7 uzduotis =======================")
# Reikia nupaišyti pilnavidurį rombą, taip pat, kaip ir pilnavidurį kvadratą, kurio aukštis 21 eilutė.

dydis = 21
puse = dydis // 2

for eilute in range(dydis):
    for stulpelis in range(dydis):
        # tikriname ar žvaigždė priklauso rombo plotui
        if abs(stulpelis - puse) <= (puse - abs(eilute - puse)):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("============================ 8 uzduotis =======================")
# Sumodeliuokite vinies kalimą.
# Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# a) “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# b) “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.

VINIES_ILGIS = 85  # mm (8.5 cm)

# a) Maži smūgiai (5–20 mm)
bendras_smugiu_skaicius_mazais = 0

for vinis in range(5):
    gylis = 0
    smugiai = 0

    while gylis < VINIES_ILGIS:
        ikalimas = random.randint(5, 20)
        gylis += ikalimas
        smugiai += 1

    bendras_smugiu_skaicius_mazais += smugiai

print("Maži smūgiai - iš viso smūgių:", bendras_smugiu_skaicius_mazais)

# b) Dideli smūgiai (20–30 mm), 50% tikimybė nepataikyti
bendras_smugiu_skaicius_dideliais = 0

for vinis in range(5):
    gylis = 0
    smugiai = 0

    while gylis < VINIES_ILGIS:
        smugiai += 1

        # 50% tikimybė pataikyti
        pataike = random.randint(0, 1)

        if pataike == 1:
            ikalimas = random.randint(20, 30)
            gylis += ikalimas

    bendras_smugiu_skaicius_dideliais += smugiai

print("Dideli smūgiai - iš viso smūgių:", bendras_smugiu_skaicius_dideliais)

print("============================ 9 uzduotis =======================")
# Sugeneruokite stringą, kurį sudarytų 50 atsitiktinių skaičių nuo 1 iki 200, atskirtų tarpais. Skaičiai turi būti unikalūs (t.y. nesikartoti).
# Sugeneruokite antrą stringą, pasinaudodami pirmu, palikdami jame tik pirminius skaičius (t.y tokius, kurie dalinasi be liekanos tik iš 1 ir patys savęs).
# Skaičius stringe sudėliokite didėjimo tvarka, nuo mažiausio iki didžiausio. (reikės split() funkcijos ir masyvų.)

numbers = random.sample(range(1,201), 50) #random.sample neleidzia kartotis skaiciams
print("Pirminis sąrašas:", *numbers, sep=" ")

pirminiai = []

for i in numbers:
    if i < 2:
        continue  # ne pirminiai
    pirminis = True
    for k in range(2, i):  # tikriname visus skaičius nuo 2 iki i-1, o ir 1 ne pirminiai todel ju netikriname
        if i % k == 0:
            pirminis = False
            break
    if pirminis:  # jei tai pirminis skaicius, pridedame ji prie saraso
        pirminiai.append(i)

print("Tik pirminiai skaičiai:",*pirminiai, sep=" ")