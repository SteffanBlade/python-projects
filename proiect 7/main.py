# automat bancar
# servicii bancare
# 

class Livrare:
    def __init__(self,materiale,valoare,tipClient,numeClient,adresa,distanta,ruta):
        self.materiale = materiale
        self.valoare = valoare
        self.tipClient = tipClient
        self.numeClient = numeClient
        self.adresa = adresa
        self.distanta = distanta
        self.ruta = ruta
        

def readDataBase(filename):
    db = []
    depozit = open(filename, 'r')
    for line in depozit:
        livlstp = line.split(',')
        # elimina spațiile albe
        lstp = []
        for x in livlstp:
            xs = x.strip()
            lstp.append(xs)
        cont = Livrare(lstp[0], lstp[1], lstp[2],lstp[3],lstp[4],lstp[5],lstp[6])
        db.append(cont)
    depozit.close()
    return db

def saveDataBase(filename, db):
    depozit = open(filename, 'w')
    for livrare in db:
        strp = str(livrare.materiale) + ',' + str(livrare.valoare) + ',' + str(livrare.tipClient) +',' + str(livrare.numeClient) +',' + str(livrare.adresa) + ','  + str(livrare.distanta) + ','  + str(livrare.ruta) + '\n'
        depozit.write(strp)
    depozit.close()

def printDataBase(db):
    print('---------------------------------------')
    print('  Materiale - Valoare - Tip client - Nume client - Adresa - Distanta - Ruta')
    for livrare in db:
        print(str(livrare.materiale) + ',' + str(livrare.valoare) + ',' + str(livrare.tipClient) +',' + str(livrare.numeClient) +',' + str(livrare.adresa) + ','  + str(livrare.distanta) + ','  + str(livrare.ruta) + '\n')
    print('---------------------------------------')

def printmes():

    print('1 - Cautarea unei comenzi dupa adresa de livrare')
    print('2 - Cautarea unui material in cadrul tuturor comenzilor')
    print('3 - Afisarea comenzilor a caror valoare este mai mare decat o valoare specificata')
    print('4 - Sortarea comenzilor dupa valoarea acestora')
    print('5 - Realizarea cu prioritate a livrarilor catre clientii fideli')
    print('6 - Livrare noua')
    print('7 - Afisarea ordinii livrarilor pe toate rutele')
    print('0 - iesire')


def crt1(livrare):
    return livrare.valoare

def crt2(livrare):
    return livrare.distanta




#	Test program
def test(filename):
    date = readDataBase(filename)
    i = 1
    while i != 0:
        printmes()

    # Selectare comanda
        i = int(input())
        

        
    # 6 - introducere de livrare
        if i == 6:
            lstp = [0,1,2,3,4,5,6]
            
            lstp[0] = input("Introduceti materialele de livrat cu spatiu intre ele:")
            lstp[1] = input("Introduceti valoarea comenzii:")
            lstp[2] = input("Introduceti tipul de client(fidel,normal):")
            lstp[3] = input("Introduceti numele clientului:")
            lstp[4] = input("Introduceti adresa de livrare:")
            lstp[5] = input("Introduceti distanta aproximativa pana la adresa:")
            lstp[6] = input("Introduceti ruta de livrare:")
      
            
            livrare = Livrare(lstp[0],lstp[1],lstp[2],lstp[3],lstp[4],lstp[5],lstp[6])
            date.append(livrare)
            printDataBase(date)

    # 1 - Cautarea unei comenzi dupa adresa de livrare
        if i == 1:
            adresa = input("Introduceti adresa cautata : ")
            for livrare in date:
                if (livrare.adresa == adresa):
                    print("Adresa de livrare corespunde clientului cu numele : " + livrare.numeClient)
    



    # 2 - Cautarea unui material in cadrul tuturor comenzilor
        if i == 2:
            material = input("Introduceti materialul cautat : ")
            for livrare in date:
                materiale = livrare.materiale
                if(materiale.find(material)):
                    print("Materialul a fost gasit in livrarea pentru clientul : "+livrare.numeClient+" cu adresa de livrare "+livrare.adresa)
            

    # 3 - Afisarea comenzilor a caror valoare este mai mare decat o valoare specificata
        if i == 3:
            valoareSpecificata = input("Introduceti valoarea dorita : ")
            for livrare in date:
                if(livrare.valoare >= valoareSpecificata):
                    print('Livrarea pentru ' +livrare.numeClient + ' cu adresa de livrare '+livrare.adresa + 'are valoarea '+livrare.valoare)
        printDataBase(date)
        
    # 4 - Sortare livrari dupa valoarea acestora
        if i == 4:
            date.sort(key=crt1)
            printDataBase(date)
            
    # 7 - Afisarea ordinii livrarilor pe fiecare ruta
        if i == 7:
            for livrare in date:
               print(' Livrarea are loc pe ruta '+livrare.ruta+' cu distanta de ' + livrare.distanta)
            ruta = input("Selectati ruta dorita : ")
            rute = []
            for livrare in date:
                if(livrare.ruta == ruta):
                    rute.append(livrare)
            rute.sort(key=crt2)
            printDataBase(rute)
            
            
            
    # 5 - Realizarea cu prioritate a livrarilor catre clientii fideli
        if i == 5:
            clienti = []
            for livrare in date:
                if(livrare.tipClient == 'fidel'):
                    clienti.append(livrare)
            clienti.sort(key=crt2)
            printDataBase(clienti)
            
    
            
                    
                        


        # 0 - Iesire
        if i == 0:
            break
        saveDataBase(filename, date)
        


