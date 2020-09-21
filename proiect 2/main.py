

class Echipa :
    def __init__(self,numeEchipa,valoareEchipa,numarVictorii,numarInfrangeri,numarEgaluri,punctaj,etapa,tipCampionat,numeCampionat,numarEchipe,numarEtape):
        self.numeEchipa = numeEchipa
        self.valoareEchipa = valoareEchipa
        self.numarVictorii = numarVictorii
        self.numarInfrangeri = numarInfrangeri
        self.numarEgaluri = numarEgaluri
        self.punctaj = punctaj
        self.etapa = etapa
        self.tipCampionat = tipCampionat
        self.numeCampionat = numeCampionat
        self.numarEchipe = numarEchipe
        self.numarEtape = numarEtape
        
    

def readDataBase(filename):
    db = []
    campionat = open(filename, 'r')
    for line in campionat:
        camplst = line.split(',')
        # elimina spațiile albe
        lstp = []
        for x in camplst:
            xs = x.strip()
            lstp.append(xs)
        camp = Echipa(lstp[0], lstp[1], lstp[2],lstp[3],lstp[4],lstp[5],lstp[6],lstp[7],lstp[8],lstp[9],lstp[10])
        db.append(camp)
    campionat.close()
    return db

def saveDataBase(filename, db):
    campionate = open(filename, 'w')
    for campionat in db:
        strp = str(campionat.numeEchipa) + ',' + str(campionat.valoareEchipa) + ',' + str(campionat.numarVictorii)+ ',' + str(campionat.numarInfrangeri)+',' + str(campionat.numarEgaluri)+',' + str(campionat.punctaj)+',' + str(campionat.etapa)+','+str(campionat.tipCampionat)+','+str(campionat.numeCampionat)+','+str(campionat.numarEchipe)+','+str(campionat.numarEtape)+ '\n'
        campionate.write(strp)
    campionate.close()

def printDataBase(db):
    print('==========================================')
    print('  Nume Echipa - Valoare Echipa - Numar Victorii - Numar Infrangeri - Numar Egaluri - Punctaj - Etapa - Tip campionat  - Nume Campionat  - Numar echipe - Numar etape ')
    for campionat in db:
        print(str(campionat.numeEchipa) + ',' + str(campionat.valoareEchipa) + ',' + str(campionat.numarVictorii) + ',' + str(campionat.numarInfrangeri)+',' + str(campionat.numarEgaluri)+',' + str(campionat.punctaj)+',' + str(campionat.etapa)+','+str(campionat.tipCampionat)+','+str(campionat.numeCampionat)+','+str(campionat.numarEchipe)+','+str(campionat.numarEtape)+ '\n')
    print('==========================================')

def printmes():

    print('1 - Adaugarea unui nou campionat ')
    print('2 - Retrogradarea unei echipe')
    print('3 - Promovarea unei echipe')
    print('4 - Afisarea, dupa fiecare etapa a campionatului, a clasamentului in in functie de numarul de puncte')
    print('5 - Afisarea locului ocupat de o anumita echipa')
    print('6 - Sortarea dupa valoarea echipei')
    print('7 - Compararea intre numarul de puncte si valoarea unei echipe')
    print('8 - iesire')

#	Test program


def crt1(x):
    return x.punctaj


def crt2(x):
    return x.valoareEchipa


#	Test program
def test(filename):
    date = readDataBase(filename)
    i = 1
    while i != 0:
        printmes()

    # Selectare comanda
        i = int(input())   
        

        # 1 - Adaugare unei echipe noi si a unui campionat
        if i == 1:
            lstp = [0,1,2,3,4,5,6,7,8,9,10]
            
            lstp[0] = input("Introduceti numele echipei:")
            lstp[1] = input("Introduceti valoarea echipei:")
            lstp[2] = input("Introduceti numarul de victorii:")
            lstp[3] = input("Introduceti numarul de infrangeri:")
            lstp[4] = input("Introduceti numarul de egaluri:")
            lstp[5] = input("Introduceti punctajul actual:")
            lstp[6] = input("Introduceti etapa actuala:")
            lstp[7] = input("Introduceti tipul de campionat :")
            lstp[8] = input("Introduceti numele campionatului :")
            lstp[9] = input("Introduceti numarul de echipe:")
            lstp[10] = input("Introduceti numarul de etape:")
            
            
            echipa = Echipa(lstp[0],lstp[1],lstp[2],lstp[3],lstp[4],lstp[5],lstp[6],lstp[7],lstp[8],lstp[9],lstp[10])
            date.append(echipa)
            printDataBase(date)

    # 2 - Retrogradarea unei echipe
        if i == 2:
            numeEchipa = input("introduceti numele echipei ")
            for echipa in date:
                if(echipa.numeEchipa == numeEchipa):
                    echipa.etapa = int(echipa.etapa) - 1
                    print("Echipa a retrogradat in etapa  : "+ str(echipa.etapa))
                    print("-"*20)
                
            
    
    # 3 - Promovarea unei echipe
        if i == 3:
            numeEchipa = input("introduceti numele echipei ")
            for echipa in date:
                if(echipa.numeEchipa == numeEchipa):
                    echipa.etapa = int(echipa.etapa) + 1
                    print("Echipa a promovat in etapa  : "+ str(echipa.etapa))
                    print("-"*20)

    
    # 4 - Afisarea, dupa fiecare etapa a campionatului, a clasamentului in in functie de numarul de puncte
        if i == 4:
            etapa = input("introduceti etapa dorita : ")
            for echipa in date:
                if(echipa.etapa == etapa):
                    print("Echipa : "+echipa.numeEchipa + " are un punctaj de : "+echipa.punctaj)
            printDataBase(date)
            print("-"*20)

    
    # 5 - Afisarea locului ocupat de o anumita echipa
        if i == 5:
            date.sort(key=crt1)
            printDataBase(date)
            print("-"*20)

            
            
    # 6 - Sortarea dupa valoarea echipei
        if i == 6:
            date.sort(key=crt2)
            printDataBase(date)
            print("-"*20)


    # 7 - Compararea intre numarul de puncte si valoarea unei echipe
        if i == 7:
            for echipa in date:
                print("Echipa : "+echipa.numeEchipa+" are punctajul de :"+echipa.punctaj+" si valoarea de : "+echipa.valoareEchipa)
            print("-"*20)

                
                
        # 8 - Iesire
        if i == 8:
            break
        saveDataBase(filename, date)
        