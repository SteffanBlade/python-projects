# voi crea clasa pacienti

class pacienti:
    def __init__(self,numeP,prenumeP,varsta,boala,medicamente,reteta,activitate):
        self.NumeP = numeP
        self.PrenumeP = prenumeP
        self.Varsta = varsta
        self.Boala = boala
        self.Medicamente = medicamente
        self.Reteta = reteta
        self.Activitate = activitate

#CISTESTE FISIERUL CARE CONTINE BAZA DE DATE SI CRREAZA O LISTA DE LISTE

def citeste(filename):
    bazadate =[]
    fisierdes = open(filename, 'r')
    for i in fisierdes:
        lst = i.split(',')
        #ELIMINAM SPATIILE ALBE
        lst2 = []
        for j in lst:
            js=j.strip()
            lst2.append(js)
        pacient=pacienti(lst2[0], lst2[1], lst2[2], lst2[3], lst2[4], lst2[5], lst2[6])
        bazadate.append(pacient)
    fisierdes.close()
    return bazadate

#SALVEAZA BAZA DE DATE PE DISK

def savebazadate(filename,bazadate):
    fisierdes=open(filename,'w')
    for pacient in bazadate:
        str=pacient.NumeP+','+pacient.PrenumeP+','+pacient.Varsta+','+pacient.Boala+','+pacient.Medicamente+','+pacient.Reteta+','+pacient.Activitate+'\n'
        fisierdes.write(str)
    fisierdes.close()

#AFISARE BAZA DE DATE

def printbazadate(bazadate):
    print('Numele pacientului-Prenumele pacientului-Varsta pacientului-Boala pacientului-Medicamentele pacientului-Retetele pacientului-Activitatea pacientului  ')
    for pacient in bazadate:
        print(pacient.NumeP,',',pacient.PrenumeP,',',pacient.Varsta,',',pacient.Boala,',',pacient.Medicamente,',',pacient.Reteta,',',pacient.Activitate)

#AFISARE DE MESAJE

def afisaremesaj():
    print('1->introducerea unui nou pacient: ')
    print('2->afisarea tuturor pacientilor: ')
    print('3->pacientii clasati in functie de varsta: ')
    print('4->numarul de pacienti care sufera de o anumita boala: ')
    print('5->pacientii cu acelasi tratament: ')
    print('6->pacientii cu un numar de retete/luna mai mare decat un numar dat: ')
    print('7->numarul de medicamente de un anumit tip: ')
    print('8->pacientii in functie de domeniul de activitate: ')
    print('0->iesire')


#TESTAREA PROGRAMULUI

#CRITERIUL DE SORTARE
def crt(j):
    return j.Varsta

def test(filename):
    dbx=citeste(filename)
    z=1
    while z!=0:
        afisaremesaj()
        z=int(input())

        #INTRODUCEREA UNUI NOU PACIENT
        if z==1:
            nou=pacienti('Vlad','Catalin','20','Gripa','Paracetamol','1','student')
            dbx.append(nou)
            printbazadate(dbx)

        #AFISAREA PACIENTILOR
        if z==2:
            printbazadate(dbx)

        #CLASAREA PACIENTILOR IN FUNCTIE DE VARSTA
        if z==3:
            print('pacientii clasati de la cei tineri la varstnici: ')
            dbx.sort(key=crt)
            printbazadate(dbx)

        #PACIENTII CARE SUFERA DE ACEEASI BOALA
        if z==4:
            numar=0
            boala=input("introduceti boala cautata")
            for i in dbx:
                if i.Boala==boala:
                    numar=numar+1
            print("numar de pacienti care au boala respectiva  sunt in numar de :"+str(numar))

        #PACIENTII CU ACELASI TRATAMENT
        if z==5:
            nr=0
            tratament=input("introduceti tratamentul:")
            for i in dbx:
                if i.Medicamente==tratament:
                    print(" Numele pacientului  : "+i.NumeP + " cu tratamentul : " + tratament)
            

        #PACIENTII CU UN NUMAR DE RETETE/LUNA MAI MARE DECAT UN NUMAR DAT
        if z==6:
            numar=input("dati un numar:")
            for i in dbx:
                if int(i.Reteta)>int(numar):
                    print("pacientii cu un numar de retete mai mare decat numarul introdus sunt : "+ i.NumeP)

        # 7 - MEDICAMENTELE DE UN ANUMIT TIP
        if z==7:
            tratament=input("dati tipul de medicament dorit:")
            numar = 0
            for i in dbx:
                if i.Medicamente==tratament:
                    numar = numar+1
            print("Numarul de medicamente : "+tratament+" este de : "+str(numar))


        #PACIENTII IN FUNCTIE DE DOMENIUL DE ACTIVITATE4
        if z==8:
            domeniu=input("dati activitatea pacientului:")
            for i in dbx:
                if i.Activitate==domeniu:
                    print(" Numele pacientilor cu activitatea de "+ str(domeniu) + " sunt: " + i.NumeP)
        if z==0:
            break
    savebazadate(filename,dbx)