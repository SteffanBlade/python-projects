# agentie imobiliara
# intermediara - percepe comision
# poate cumpara sau vinde
# p.juridica - p.juridica - comision + 10%
# p.fizica - p.fizica
# p.fizica - p.juridica
# operatie vanzare cumparare(upgrade reducere 30%) sau inchiriere
# clienti fideli reducere 50%
# Cerere-pret maxim
# oferta - pret minim
# imperecherea cererilor si ofertelor


class Tranzactie:
    def __init__(self,numePersoana,tipPersoana,tipClient,tipTranzactie,reducere,pret):
        self.numePersoana = numePersoana
        self.tipPersoana = tipPersoana
        self.tipClient = tipClient
        self.tipTranzactie = tipTranzactie
        self.reducere = reducere
        self.pret = pret


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
        prod = Tranzactie(lstp[0], lstp[1], lstp[2],lstp[3],lstp[4],lstp[5])
        db.append(prod)
    inventar.close()
    return db

def saveDataBase(filename, db):
    inventar = open(filename, 'w')
    for prod in db:
        strp = str(prod.numePersoana) + ',' + str(prod.tipPersoana) + ',' + str(prod.tipClient) +',' + str(prod.tipTranzactie) + ','  + str(prod.reducere) +','+ str(prod.pret)+ '\n'
        inventar.write(strp)
    inventar.close()

def printDataBase(db):
    print('////////////////////////////////////////')
    print('  numePersoana - tipPersoana - tipClient - tipTranzactie - reducere ')
    for prod in db:
        print(str(prod.numePersoana) + ',' + str(prod.tipPersoana) + ',' + str(prod.tipClient) +',' + str(prod.tipTranzactie) + ','  + str(prod.reducere)+','+ str(prod.pret) + '\n')
    print('////////////////////////////////////////')

def printmes():

    print('1 - Introducere tranzactie')
    print('2 - Introducere pret maxim pentru oferta')
    print('3 - Introducere pret minim pentru cerere')
    print('4 - Imperecherea cererilor si ofertelor in functie de pret')
    print('0 - iesire')
    
#	Test program


#	Test program
def test(filename):
    tranzactii = readDataBase(filename)
    i = 1
    while i != 0:
        printmes()

    # Selectare comanda
        i = int(input())

        # 1 - Introducere tranzactie
        if i == 1:
            lstp = [0,1,2,3,4,5]
            lstp[0] = input("Introduceti nume persoana: ")
            lstp[1] = input("Introduceti tipul de persoana: ")
            lstp[2] = input("Introduceti tipul de client: ")
            lstp[3] = input("Introduceti tipul de tranzactie: ")
            lstp[4] = input("Introduceti reducere: ")
            lstp[5] = input("Introduceti pretul initial: ")
            tranz = Tranzactie(lstp[0],lstp[1],lstp[2],lstp[3],lstp[4],lstp[5])
            tranzactii.append(tranz)
            printDataBase(tranzactii)
        
        # 2 - introducere pret maxim pentru oferta
        if i == 2:
            nume = input("Introduceti numele persoanei pentru care se specifica pretul : ")
            for tran in tranzactii:
                if((tran.numePersoana == nume) and (tran.tipTranzactie == "oferta")):
                    pretNou = input("Introduceti noul pretul pentru oferta: ")
                    if(tran.tipClient == "juridica"):
                        tran.pret = pretNou + tran.pret/10
                    else:
                        tran.pret = pretNou
            else:
                print("Nu s-a gasit o tranzactia respeciva sau persoana nu a depus o oferta")
            printDataBase(tranzactii)

        
        # 3 - introducere pret minim pentru cerere
        if i == 3 :
            nume = input("Introduceti numele persoanei pentru care se specifica pretul : ")
            for tran in tranzactii:
                if((tran.numePersoana == nume) and (tran.tipTranzactie == "cerere") ):
                    pretNou = input("Introduceti noul pretul pentru cerere: ")
                    if(tran.tipClient == "juridica"):
                        tran.pret = pretNou + tran.pret/10
                    else:
                        tran.pret = pretNou
            else:
                print("Nu s-a gasit o tranzactia respectiva sau aceasta nu este de tip cerere")
            printDataBase(tranzactii)

        
        # 4 - imperecherea cererilor si a ofertlor : le sortam dupa tipul de tranzactie si daca ele difera dar pretul corespunde le afisam impreuna
        if i == 4:
            for tran1 in tranzactii:
                for tran2 in tranzactii:
                    if(tran1.numePersoana != tran2.numePersoana and tran1.tipTranzactie != tran2.tipTranzactie and tran1.pret == tran2.pret):
                        print("Este posibila o tranzactie intre : ",tran1.numePersoana," si ",tran2.numePersoana)



        # 0 - Iesire
        if i == 0:
            break
        saveDataBase(filename, tranzactii)

