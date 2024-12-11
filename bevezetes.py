import datetime
def elso():
    print("I/A:")
    nev:str= input("Autó neve: ")
    ev:int = int (input("Gyártási dátum: "))
    print("I/B:")
    if(ev<2000):
        print(f"Ez a {nev} öreg autó.")
    elif(ev==2024):
        print(f"Ez a {nev} friss gyártású.")
    else:
     print(f"Ez a {nev} átlagos korú.")

