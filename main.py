import random

print("============================ 1 uzduotis =======================")
# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.

for i in range(10):
    print("labas")

print("============================ 2 uzduotis =======================")
# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.
numbers = [0,1,2,3,4,5,6,7,8,9]

for i in numbers:
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

numbers1 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
print(numbers1[0::2])

# for skaicius in range(10, 51, 2):
#     print(skaicius)

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
for i in range(0,21):
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
# # print(*numbers, sep=" ")

count = 0
symbol = []

for num in numbers:
    if num  > 150:
        count += 1
    if num > 275:
        symbol.append(f"[{num}]")
    else:
        symbol.append(str(num))

print(*symbol)
print("Skaičių didesnių už 150:", count)

print("============================ 2 uzduotis =======================")
# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos.
# Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

numbers = [num for num in range(0,3000)]
div_77 = [n for n in numbers if n % 77 == 0]

print(*div_77, sep=",")

print("============================ 3 uzduotis =======================")
# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”

square = 25

for i in range(square):
    print("*" * square)

print("============================ 4 uzduotis =======================")
# Prieš tai nupieštam kvadratui nupieškite istrižaines, zaigzdutę pakeisdami kitu simboliu.


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
