import random
def veletlen_szam():
    print("II/A,B,C:")
    v_szam_lista=[]
    i:int=0
    while(i<5):
        v_szam:int= int(random.random()*1)+100
        v_szam_lista.append(v_szam)
    i+=1
    print(v_szam_lista)

def egyjegyuek_szama(v_szam_lista):
    print("II/D,E")
    i:int=0
    db:int=0
    while(i<(len(v_szam_lista))):
        if(v_szam_lista[i]<10):
            db+=1
        i+=1
    return db

def konzol_kiir(db):
    print("II/D,E")
    print(f"Az egyjegyűek száma: {db}")

def file_kiir():
    print("II/F")
