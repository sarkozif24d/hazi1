# ...existing code...
import math
import sys

def task1():
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
    except ValueError:
        print("Érvénytelen szám.")
        return
    if a == 0:
        if b == 0:
            print("Nem egyenlet (a és b is 0).")
        else:
            x = -c / b
            print(f"Lineáris egyenlet egy gyök: {x}")
        return
    D = b*b - 4*a*c
    if D < 0:
        print("Nincs valós gyök")
    elif D == 0:
        x = -b / (2*a)
        print(f"Egy valós gyök: {x}")
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Két valós gyök: {x1}, {x2}")

def task2():
    try:
        ev = int(input("Év = "))
    except ValueError:
        print("Érvénytelen év.")
        return
    is_leap = (ev % 4 == 0) and ((ev % 100 != 0) or (ev % 400 == 0))
    print("Szökőév." if is_leap else "Nem szökőév.")

def task3():
    try:
        x = float(input("Első szám = "))
        y = float(input("Második szám = "))
    except ValueError:
        print("Érvénytelen szám.")
        return
    op = input("Művelet (+, -, *, /) = ").strip()
    if op == "+":
        print("Eredmény:", x + y)
    elif op == "-":
        print("Eredmény:", x - y)
    elif op == "*":
        print("Eredmény:", x * y)
    elif op == "/":
        if y == 0:
            print("Hiba: osztás nullával.")
        else:
            print("Eredmény:", x / y)
    else:
        print("Ismeretlen művelet.")

def task4():
    try:
        n = int(input("Pozitív egész szám = "))
    except ValueError:
        print("Érvénytelen szám.")
        return
    if n < 0:
        print("A szám nem lehet negatív.")
        return
    r = math.isqrt(n)
    if r*r == n:
        print(f"Tökéletes négyzet. Gyök: {r}")
    else:
        print("Nem tökéletes négyzet.")

def task5():
    try:
        osszeg = float(input("Vásárlási összeg (Ft) = "))
    except ValueError:
        print("Érvénytelen összeg.")
        return
    if osszeg <= 10000:
        kedv = 0.0
    elif osszeg <= 50000:
        kedv = 0.10
    else:
        kedv = 0.20
    fizetendo = osszeg * (1 - kedv)
    print(f"Kedvezmény: {kedv*100:.0f}%. Fizetendő: {fizetendo:.2f} Ft")

def task6():
    try:
        ora = int(input("Óra (0-23) = "))
    except ValueError:
        print("Érvénytelen óra.")
        return
    if not (0 <= ora <= 23):
        print("Az óra nincs 0 és 23 között.")
        return
    if 0 <= ora <= 5:
        print("Éjszaka")
    elif 6 <= ora <= 11:
        print("Reggel")
    elif 12 <= ora <= 17:
        print("Délután")
    else:
        print("Este")

def task7():
    try:
        n = int(input("Pozitív egész szám = "))
    except ValueError:
        print("Érvénytelen szám.")
        return
    if n < 0:
        print("A szám nem lehet negatív!")
        return
    fact = 1
    for i in range(2, n+1):
        fact *= i
    print(f"{n}! = {fact}")

def task8():
    try:
        honap = int(input("Hónap (1-12) = "))
    except ValueError:
        print("Érvénytelen hónap.")
        return
    days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if 1 <= honap <= 12:
        print(f"A hónap {days[honap]} napos.")
    else:
        print("Hónapnak 1 és 12 között kell lennie.")

def task9():
    try:
        jovedelem = float(input("Jövedelem (Ft) = "))
    except ValueError:
        print("Érvénytelen összeg.")
        return
    if jovedelem <= 500000:
        rate = 0.10
    elif jovedelem <= 1000000:
        rate = 0.20
    else:
        rate = 0.30
    ado = jovedelem * rate
    netto = jovedelem - ado
    print(f"Adó: {ado:.2f} Ft, Nettó jövedelem: {netto:.2f} Ft")

def menu():
    ops = {
        "1": task1, "2": task2, "3": task3, "4": task4,
        "5": task5, "6": task6, "7": task7, "8": task8, "9": task9
    }
    while True:
        print("\nVálassz feladatot (1-9), 0 kilépés:")
        choice = input("> ").strip()
        if choice == "0":
            print("Kilépés.")
            return
        fn = ops.get(choice)
        if fn:
            fn()
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    menu()
# ...existing code...
# filepath: c:\Users\sarkozif.24d\Documents\GitHub\hazi1\idk.py
# ...existing code...
import math
import sys

def task1():
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
    except ValueError:
        print("Érvénytelen szám.")
        return
    if a == 0:
        if b == 0:
            print("Nem egyenlet (a és b is 0).")
        else:
            x = -c / b
            print(f"Lineáris egyenlet egy gyök: {x}")
        return
    D = b*b - 4*a*c
    if D < 0:
        print("Nincs valós gyök")
    elif D == 0:
        x = -b / (2*a)
        print(f"Egy valós gyök: {x}")
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Két valós gyök: {x1}, {x2}")

def task2():
    try:
        ev = int(input("Év = "))
    except ValueError:
        print("Érvénytelen év.")
        return
    is_leap = (ev % 4 == 0) and ((ev % 100 != 0) or (ev % 400 == 0))
    print("Szökőév." if is_leap else "Nem szökőév.")

def task3():
    try:
        x = float(input("Első szám = "))
        y = float(input("Második szám = "))
    except ValueError:
        print("Érvénytelen szám.")
        return
    op = input("Művelet (+, -, *, /) = ").strip()
    if op == "+":
        print("Eredmény:", x + y)
    elif op == "-":
        print("Eredmény:", x - y)
    elif op == "*":
        print("Eredmény:", x * y)
    elif op == "/":
        if y == 0:
            print("Hiba: osztás nullával.")
        else:
            print("Eredmény:", x / y)
    else:
        print("Ismeretlen művelet.")

def task4():
    try:
        n = int(input("Pozitív egész szám = "))
    except ValueError:
        print("Érvénytelen szám.")
        return
    if n < 0:
        print("A szám nem lehet negatív.")
        return
    r = math.isqrt(n)
    if r*r == n:
        print(f"Tökéletes négyzet. Gyök: {r}")
    else:
        print("Nem tökéletes négyzet.")

def task5():
    try:
        osszeg = float(input("Vásárlási összeg (Ft) = "))
    except ValueError:
        print("Érvénytelen összeg.")
        return
    if osszeg <= 10000:
        kedv = 0.0
    elif osszeg <= 50000:
        kedv = 0.10
    else:
        kedv = 0.20
    fizetendo = osszeg * (1 - kedv)
    print(f"Kedvezmény: {kedv*100:.0f}%. Fizetendő: {fizetendo:.2f} Ft")

def task6():
    try:
        ora = int(input("Óra (0-23) = "))
    except ValueError:
        print("Érvénytelen óra.")
        return
    if not (0 <= ora <= 23):
        print("Az óra nincs 0 és 23 között.")
        return
    if 0 <= ora <= 5:
        print("Éjszaka")
    elif 6 <= ora <= 11:
        print("Reggel")
    elif 12 <= ora <= 17:
        print("Délután")
    else:
        print("Este")

def task7():
    try:
        n = int(input("Pozitív egész szám = "))
    except ValueError:
        print("Érvénytelen szám.")
        return
    if n < 0:
        print("A szám nem lehet negatív!")
        return
    fact = 1
    for i in range(2, n+1):
        fact *= i
    print(f"{n}! = {fact}")

def task8():
    try:
        honap = int(input("Hónap (1-12) = "))
    except ValueError:
        print("Érvénytelen hónap.")
        return
    days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if 1 <= honap <= 12:
        print(f"A hónap {days[honap]} napos.")
    else:
        print("Hónapnak 1 és 12 között kell lennie.")

def task9():
    try:
        jovedelem = float(input("Jövedelem (Ft) = "))
    except ValueError:
        print("Érvénytelen összeg.")
        return
    if jovedelem <= 500000:
        rate = 0.10
    elif jovedelem <= 1000000:
        rate = 0.20
    else:
        rate = 0.30
    ado = jovedelem * rate
    netto = jovedelem - ado
    print(f"Adó: {ado:.2f} Ft, Nettó jövedelem: {netto:.2f} Ft")

def menu():
    ops = {
        "1": task1, "2": task2, "3": task3, "4": task4,
        "5": task5, "6": task6, "7": task7, "8": task8, "9": task9
    }
    while True:
        print("\nVálassz feladatot (1-9), 0 kilépés:")
        choice = input("> ").strip()
        if choice == "0":
            print("Kilépés.")
            return
        fn = ops.get(choice)
        if fn:
            fn()
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    menu()
# ...existing code...