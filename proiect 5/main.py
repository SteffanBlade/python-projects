# Sa se realizeze unprogram care sa asigure gestionarea unui supermaket cu diferite produse (Alimentare,cosmetice,bauturi)
# Se incarca intr-un fisier sub formatu : 
# cod_produs(int),
# furnizor(string),
# (unitate de masura(int)),
# pret furnizor(int),
# adaus(procent),
# cantitate int,
# termen valabilitate (int)

#Adaugare
#Cautare dupa furnizor
#Stergere dupa valabilitate
#Vanzare (cantitate -1)
#Calcul adaos
#Iesire

class Produs :
    def __init__(self,codProdus,furnizor,unitateMasura,pretFurnizor,adaos,termenValabilitate,cantitate):
        self.codProdus = codProdus
        self.furnizor = furnizor
        self.unitateMasura = unitateMasura
        self.pretFurnizor = pretFurnizor
        self.adaos = adaos
        self.termenValabilitate = termenValabilitate
        self.cantitate = cantitate
    

def readDataBase(filename):
    db = []
    inventar = open(filename, 'r')
    for line in inventar:
        prodlst = line.split(',')
        # elimina spațiile albe
        lstp = []
        for x in prodlst:
            xs = x.strip()
            lstp.append(xs)
        prod = Produs(lstp[0], lstp[1], lstp[2],lstp[3],lstp[4],lstp[5],lstp[6])
        db.append(prod)
    inventar.close()
    return db

def saveDataBase(filename, db):
    inventar = open(filename, 'w')
    for prod in db:
        strp = str(prod.codProdus) + ',' + str(prod.furnizor) + ',' + str(prod.unitateMasura) +',' + str(prod.pretFurnizor) + ','  + str(prod.adaos) + ',' +str(prod.termenValabilitate) +','+str(prod.cantitate)+ '\n'
        inventar.write(strp)
    inventar.close()

def printDataBase(db):
    print('---------------------------------------')
    print('  codProdus - furnizor - unitateMasura - pretFurnizor - adaos - termenValabilitate-cantitate')
    for prod in db:
        print(str(prod.codProdus) + ',' + str(prod.furnizor) + ',' + str(prod.unitateMasura) +',' + str(prod.pretFurnizor) + ','  + str(prod.adaos) + ',' +str(prod.termenValabilitate) +str(prod.cantitate) + '\n')
    print('---------------------------------------')

def printmes():

    print('1 - Adaugare')
    print('2 - Cautare dupa furnizor')
    print('3 - Stergere dupa valabilitate')
    print('4 - Vanzare (cantitate -1)')
    print('5 - Calcul pret cu adaos')
    print('0 - iesire')
    
#	Test program
#	Criteriile de sortare : Nume,Cantitate,PretUnitar


def crt1(x):
    return x.furnizor


def crt2(x):
    return x.valabilitate



#	Test program
def test(filename):
    inventar = readDataBase(filename)
    i = 1
    while i != 0:
        printmes()

    # Selectare comanda
        i = int(input())

        # 3 - Adaugare
        if i == 1:
            lstp = [0,1,2,3,4,5,6]
            lstp[0] = input("Introduceti cod produs:")
            lstp[1] = input("Introduceti furnizor:")
            lstp[2] = input("Introduceti unitateMasura:")
            lstp[3] = input("Introduceti pretFurnizor:")
            lstp[4] = input("Introduceti adaos:")
            lstp[5] = input("Introduceti termen de valabilitate:")
            lstp[6] = input("Introduceti cantitate:")
            prod = Produs(lstp[0],lstp[1],lstp[2],lstp[3],lstp[4],lstp[5],lstp[6])
            inventar.append(prod)
            printDataBase(inventar)

    # 2 - Cautare dupa furnizor
        if i == 2:
            inventar.sort(key=crt1)
            printDataBase(inventar)

    # 3 - Stergere dupa valabilitate
        if i == 3:
            termenValabilitateMaxim=(input("introduceti data de valabilitate:"))
            for prod in inventar:
                if(prod.termenValabilitate>termenValabilitateMaxim):
                    inventar.remove(prod)
            printDataBase(inventar)



    # 4 - Vanzare (cantitate -1)
        if i == 4:
            codProdusIntrodus = (input("Introduceti produsul care se vinde:"))
            for x in inventar:
                if(x.codProdus == codProdusIntrodus):
                   cantitateActuala =int(x.cantitate) - 1
            print("Cantitatea actuala:",cantitateActuala)
            



    # 5 - Calcul pret cu adaos
        if i == 5:
            codProdusIntrodus = input("Introduceti produsul la care vreti sa vedeti pretul cu adaos")
            for x in inventar:
                if(x.codProdus == codProdusIntrodus):
                    pretComplet = int(x.pretFurnizor)+int(x.adaos)
            print("Pretul complet:",pretComplet)
            



        # 0 - Iesire
        if i == 0:
            break
        saveDataBase(filename, inventar)
        

