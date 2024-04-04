import math
import random

# 2 cromozomi si pozitia de la care se incruciseaza
def incrucisare(c1, c2, poz):
    sol1 = c1[:poz] + c2[poz:]
    sol2 = c2[:poz] + c1[poz:]
    return sol1, sol2

# cromozom si lista de pozitii pe care se inverseaza bitii din cromozom
def mutatie(c, list):
    for i in list:
        c = c[:i] + str(int(not bool(int(c[i])))) + c[(i+1):]
    return c

# elem din list sa fie float
# a, b, c sunt coeficientii functiei
def selectie(a,b,c, list):
    v = [0]
    sum = 0
    for x in list:
        sol = a * x * x + b * x + c
        sum += sol
        v.append(sol)
    interv = []
    sum2 = 0
    for x in v:
        sum2 += x
        interv.append(sum2 / sum)
    return interv

# num = int, lung = int, returneaza string de 1 si 0
def DecimalToBinary(num, lung):
    bin = ""
    for i in range(lung):
        bin = str(num % 2) + bin
        num = num // 2
    return bin

# bin e un sir binar (de 0 si 1) dat ca string returneaza un int
def BinaryToDecimal(bin):
    nr = 0
    z = 0
    for i in range(len(bin)-1, -1, -1):
        if bin[i] == "1":
            nr = nr + 2 ** z
        z += 1
    return nr

# [a, b] intervaul, l lungimea cromozomului
# din codificare in cromozom
def decodificare(a,b,l,codif):
    d = (b-a)/2**l
    for i in range((int)(2**l)):
        if codif < a+(i+1)*d and codif >= a+i*d:
            return DecimalToBinary(i, l)


# din cromozom in codificare
def codificare(a,b,l, crom):
    d = (b-a)/2**l
    return a + d * BinaryToDecimal(crom)


# genereaza un cromozom random ca sir de caractere
def genereaza_cromozom(l):
    bits = ["0", "1"]
    cromozom = ""
    for x in range(l):
        cromozom += random.choice(bits)
    return cromozom


#---------------------------------------------------------
# DATE DE INTRARE

# precizia:
p = 2

# functia:
a, b, c = -2, -12, 5

# intervalul:
x, y = -5, 0

# numar cromozomi:
nr_crom = 20

# numar de generatii:
nr_gen = 50

# probabilitate recombinare
p_recomb = 0.25

# probabilitate mutatie
p_mut = 0.01

# lungime cromozomi:
l = math.ceil(math.log((y-x) * 10**p, 2))

#-------------------------------------------------
# ALGORITMUL

# cromozomi codificati
lista_cromozomi = []
for i in range(nr_crom):
    lista_cromozomi.append(codificare(x, y, l, genereaza_cromozom(l)))

print(lista_cromozomi)

for _ in range(nr_gen):
    #print(lista_cromozomi)
    intervale_selectie = selectie(a, b, c, lista_cromozomi)


    #selectie:

    generatie = []
    for i in range(nr_crom - 1):
        r = random.random()

        # tentativa cautare binara...
        # st = 0
        # dr = nr_crom - 1
        # while st < dr:
        #     mij = (st + dr) // 2
        #
        #     if intervale_selectie[mij] > r:
        #
        #         if intervale_selectie[mij - 1] <= r:
        #             generatie.append(lista_cromozomi[mij - 1])
        #             #print(lista_cromozomi[mij - 1])
        #             break
        #         else:
        #             dr = mij - 1
        #     else:
        #         st = mij + 1


        for j in range(nr_crom + 1):
            if intervale_selectie[j] > r:
                generatie.append(lista_cromozomi[j - 1])
                break


    elem_elitist = lista_cromozomi[0]
    for elem in lista_cromozomi:
        if elem_elitist*a*elem_elitist + b*elem_elitist + c < a*elem*elem + b*elem + c:
            elem_elitist = elem

    #print(m_selectie)

    crom1 = "*"
    poz1 = "*"
    vals = [x for x in range(2, l - 1)]
    #incrucisare
    for cc in range(len(generatie) - 1):
        if p_recomb > random.random():
            if crom1 == "*":
                crom1 = generatie[cc]
                poz1 = cc
            else:
                v1, v2 = incrucisare(decodificare(x, y, l, crom1), decodificare(x, y, l, generatie[cc]), random.choice(vals))
                generatie[poz1] = codificare(x, y, l, v1)
                generatie[cc] = codificare(x, y, l, v2)
                crom1 = "*"

    #mutatie
    for i in range(len(generatie) - 1):
        if p_mut > random.random():
            generatie[i] = codificare(x, y, l, mutatie(decodificare(x, y, l, generatie[i]), [random.choice(vals)]))


    lista_cromozomi = generatie
    lista_cromozomi.append(elem_elitist)


print(elem_elitist)
print(a * elem_elitist * elem_elitist + b * elem_elitist + c)
