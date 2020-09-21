# voi crea clasa apartament

class Apartament:
    def __init__(self,bloc,scara,numarApartament,numeLocatar,numarPersoane,intretinere,restanta):
        self.bloc = bloc
        self.scara = scara
        self.numarApartament = numarApartament
        self.numeLocatar = numeLocatar
        self.numarPersoane = numarPersoane
        self.intretinere = intretinere
        self.restanta = restanta
   

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
        apartament=Apartament(lst2[0], lst2[1], lst2[2], lst2[3], lst2[4], lst2[5], lst2[6])
        bazadate.append(apartament)
    fisierdes.close()
    return bazadate

#SALVEAZA BAZA DE DATE PE DISK

def savebazadate(filename,bazadate):
    date=open(filename,'w')
    for apartament in bazadate:
        apartament=str(apartament.bloc)+','+str(apartament.scara)+','+str(apartament.numarApartament)+','+str(apartament.numeLocatar)+','+str(apartament.numarPersoane)+','+str(apartament.intretinere)+','+str(apartament.restanta)+'\n'
        date.write(apartament)
    date.close()

#AFISARE BAZA DE DATE

def printbazadate(bazadate):
    print('Bloc -Scara -Numar apartament- Locatar - Numarul de persoane - Intretinere (medie) - Restanta')
    for apartament in bazadate:
        print(apartament.bloc,',',apartament.scara,',',apartament.numarApartament,',',apartament.numeLocatar,',',apartament.numarPersoane,',',apartament.intretinere,',',apartament.restanta)

#AFISARE DE MESAJE

def afisaremesaj():
    print('1->introducerea unui nou apartament ')
    print('2->Sortarea locatarilor dupa nume ')
    print('3->Adaugarea unui nou locatar ')
    print('4->Cautarea unui locatar  ')
    print('5->Mai mult de 5 persoane ')
    print('6->Afisarea intretinerilor ')
    print('7->Restanta mai mare ca suma dorita  ')
    print('8->Clasarea locatarilor in rai platnici sau buni platnici ')
    print('0->iesire')


#TESTAREA PROGRAMULUI

#CRITERIUL DE SORTARE
def crt1(j):
    return j.numeLocatar

def test(filename):
    date=citeste(filename)
    z=1
    while z!=0:
        afisaremesaj()
        z=int(input())

        # 1 - INTRODUCEREA UNUI NOU APARTAMENT
        
        if z == 1:
            lstp = [0,1,2,3,4,5,6]
            
            lstp[0] = input("Introduceti blocul:")
            lstp[1] = input("Introduceti scara:")
            lstp[2] = input("Introduceti numarul apartamentului:")
            lstp[3] = input("Introduceti numele locatarului:")
            lstp[4] = input("Introduceti numarul de persoane:")
            lstp[5] = input("Introduceti media pe intretinere:")
            lstp[6] = input("Introduceti restanta actuala:")
            
            
            apartament = Apartament(lstp[0],lstp[1],lstp[2],lstp[3],lstp[4],lstp[5],lstp[6])
            date.append(apartament)
            printbazadate(date)
            print("*" *25)      

        # 2 - Sortarea locatarilor dupa nume
        if z==2:
            date.sort(key=crt1)
            printbazadate(date)
            print("*" *25)      

        # 3 - Adaugarea unui nou locatar
        if z==3:
            
            numar=input("introduceti numarul apartamentului pentru care se schimba locatarul : ")
            for apartament in date:
                if apartament.numarApartament == numar:
                    locatar = input("introduceti noul locatar : ")
                    apartament.numeLocatar = locatar
                else:
                    print("Apartamentul nu a fost gasit !")
            print("*" *25)      

        #  4 - Cautarea unui locatar
        if z==4:
            
            nume=input("introduceti numele locatarului :")
            for apartament in date:
                if apartament.numeLocatar == nume:
                    print(" Locatarul se afla in apartamentul : "+apartament.numarApartament)
            print("*" *25)      

        # 5 - Mai mult de 5 persoane
        if z==5:
            for apartament in date:
                if int(apartament.numarPersoane)>5:
                    print("In apartamentul : "+apartament.numarApartament + " locuiesc mai mult de 5 persoane")
            print("*" *25)      
        # 6 - Afisarea intretinerilor
        if z==6:
            for apartament in date:
                print("Apartamentul : "+apartament.numarApartament + " are o intretinere de : "+apartament.intretinere)
            print("*" *25)      
            
        # 7 - Restanta mai mare ca suma dorita
        if z==7:
            suma = input("Introduceti suma dorita : ")
            for apartament in date:
              if int(apartament.restanta) > int(suma):
                  print("Apartamentul : "+apartament.numarApartament + " are de plata mai mult decat suma dorita ")
        print("*" *25)      
            
        # 8 - Clasarea locatarilor in rai platnici sau buni platnici
        if z == 8:
            suma = input("Introduceti suma pentru care un locatar devine rau platnic : ")
            for apartament in date:
              if int(apartament.restanta) > int(suma):
                  print("Locatarul : "+apartament.numeLocatar + " este rau platnic")
              else:
                  print("Locatarul : "+apartament.numeLocatar + " este bun platnic")
            print("*" *25)         
            
        if z==0:
            savebazadate(filename,date)
            break