from random import*
inimesed = ["A", "B", "C", "D", "E"]
palgad = [1200,2500,750,395,1200]
def sisesta_andmed(i, p):
    """Kasutaja lisamine nimekirja, samuti palk
    """
    N = 1
    for n in range(N):
        inimene = input("Sisestage oma nimi: ")
        i.append(inimene)
        palk=int(input("Sisestage palk: "))
        p.append(palk )
    return i,p
def andmed_ekranile(i, p):
    """Kuva inimeste nimekiri ja palgad
    """
    N=len(i)
    for n in range(N):
        print(f"{i[n]} - {p[n]}")
def kustutamine(i, p):
    """Eemaldab nimekirjast inimese nime ja palga
    """
    nimi=input("Sisestage selle isiku nimi, kelle soovite eemaldada: ")
    n=i.count(nimi)
    abi_list=[]
    if n > 0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e))
                print(f"{t}.{i[e]} - {p[e]}")
        j=int(input("Isiku seerianumber: "))
        i.pop(abi_list[j-1])
        p.pop(abi_list[j-1])
        andmed_ekranile(i,p)
    return i,p
def maksimum(i, p):
    """Kuvab ekraanil olevast loendist kasutaja maksimaalse palga
    """
    max_palk = palgad[0] 
    kellel = inimesed[0]
    for p in palgad:
        if p > max_palk:
            max_palk = p
            i = palgad.index(max_palk)
            kellel = inimesed[i]
    print(f"Maksimaalne palk - {max_palk} saab - {kellel}")
def minimum(i, p):
    """Kuvab ekraanil olevast nimekirjast kasutaja miinimumpalga
    """
    min_palk = palgad[0]
    kellel = inimesed[0]
    for p in palgad:
        if p < min_palk:
            min_palk = p
            i = palgad.index(min_palk)
            kellel = inimesed[i]
    print(f"Miinimumpalk - {min_palk} saab - {kellel}.")
def koik_palk(i, p):
    """Lisab kõik palgad ja väljapanekud
    """
    summa=sum(palgad)
    print("Kõigi töötajate palgad -", summa)
def koik_del(i, p):
    """Puhastab loendi
    """
    delit=int(input("Tahad nimekirja tühjendada?\n1 - Jah\n2 - Ei"))
    if delit == 1:
        palgad = []
        inimesed = []
    elif delit == 2:
        print("Väljund")
    else:
        ValueError
def modulizm(i, p):
    """Kontrollib, kas kasutaja on loendis, otsides nime
    """
    imya=str(input("Sisestage loendist selle inimese nimi, keda soovite leida"))
    if imya in (inimesed):
        print (imya)
    elif imya not in (inimesed):
        vvod=int(input("Seda nime pole loendis, kas soovite kasutaja lisada?\n1-Jah\n2-Ei"))
        if vvod == 1:
            sisesta_andmed(i, p)
        elif vvod == 2:
            return
        else:
            ValueError
def zarplatvsem(i, p):
    zp=int(input("Tõsta kõigi töötajate palka"))
    itog=palgad+zp
    return
def keskmine(i, p):
    summa=0
    for palk in p:
        summa+=palk
        kesk=summa/len(p)
        print(kesk)
        vahe=0
        if 0<p.indes(kesk)<len(p)-1:
            kesk=i[p.index(kesk)]
            return kesk
        else:
            kesk="Puudub"
            return kesk