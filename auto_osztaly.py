class Auto:
    def __init__(self,nev:str,gyartas:int):
        self.nev=nev
        self.gyartas=gyartas

f = open("auto.txt", "r")
print(f.read())
f.close()
