#Zadanie 1
def oblicz_kwadrat(liczba):    
    return liczba ** 2
liczba = float(input("Podaj liczbę: "))
kwadrat = oblicz_kwadrat(liczba)
print("Kwadrat twojej liczby to: ", kwadrat)

#Zadanie 2
def odwróć_string(tekst):    return tekst[::-1]
string = input("Podaj tekst: ")
odwrócony_string = odwróć_string(string)
print("Odwrócony tekst:",odwrócony_string)

#Zadanie 3
def powitanie(imie="Użytkowniku", język="polski"):    
    if język == 'polski':
      print("Cześć:", imie)
    elif język == 'angielski':
        print("Hello:", imie)    
    elif język == 'niemiecki':
        print("Guten Morgen:", imie)    
    else:
        print("Witaj", imie)        
powitanie("Anna", "polski")
powitanie("John", "angielski")
powitanie("Hens", "niemiecki")
#Zadanie 4
def średnie(lista):
    if not lista:
        return 0
    suma = sum(lista)
    return suma / len(lista)
liczby = [10,20,30,40,50]
wynik = średnie(liczby)
print("średnia z listy liczb",wynik)

#Zadanie 5
def oblicz_bmi(waga,wzrost):
    bmi = waga / (wzrost **2)    
    if bmi < 18.5:
        kategoria = "niedowaga"
    elif 18.5 <= bmi <= 24.9:
        kategoria = "pożądana masa ciała"
    elif 25 <= bmi <= 29.9:
        kategoria = "nadwaga"
    elif 30 <= bmi <= 34.9:
        kategoria = "otyłość I stopnia"
    elif 35 <= bmi <= 39.9:
        kategoria = "otyłość II stopnia"
    else:
        kategoria = "otyłość III stopnia"
    
    return "Twoje BMI wynosi:",bmi,"Kategoria:",kategoria
waga = float(input("Podaj wage (w kg):"))
wzrost = float(input("Wzrost (w metrach):"))
wynik = oblicz_bmi(waga, wzrost)
print(wynik)

#Zadanie 6
import math
def oblicz_pole_trojkata(a, b, c):
    try:
        if a <= 0 or b <= 0 or c <= 0:
            print("Boki trójkąta muszą być dodatnie.")
        if a + b <= c or a + c <= b or b + c <= a:
            print("Podane boki nie tworzą trójkąta.")
        s = (a+b+c)/2
        pole = math.sqrt(s*(s - a) * (s - b) * (s - c))
        return round(pole,2)
    except ValueError as wynik:
        return "Błąd:",wynik
a = float(input("Podaj strone a:"))
b = float(input("Podaj strone b:"))
c = float(input("Podaj strone c:"))
wynik = oblicz_pole_trojkata(a, b, c)
print(f"Pole trójkąta o bokach {a}, {b}, {c} wynosi: {wynik}")

#Zadanie 7
def obliczanie_potęgę(a,n):
    if n == 0:
        return 1
    elif n > 0:
        return a * obliczanie_potęgę(a, n - 1)
    else:
       if n % 2 == 0:
            return a * obliczanie_potęgę(a, -(n + 1))
       else:
            return -a * obliczanie_potęgę(a, -(n + 1))  
a = float(input("Wprowadź liczbę (a), którą chcesz podnieść  do n:"))
n = float(input("Wprowadź potęgę(n):"))
wynik = obliczanie_potęgę(a,n)
print("Wynik",wynik)

#Zadanie 8(A)
def wyswietl_parametry(*args):
    for arg in args:
        print(arg)
wyswietl_parametry(1, 20, 35, "qwerty", 4.5) 
#8(B)
def max_parametr(*args):
    if args:
        return max(args)
    else:
        return None

dane = input("Wprowadź liczby: ")

lista_liczb = [float(x) for x in dane.split()]
maksymalna_wartosc = max_parametr(*lista_liczb)

print(f"Maksymalna wartość: {maksymalna_wartosc}")

#Zadanie 9 
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = float(input("Podaj numer wyrazu ciągu Fibonacciego (n): "))

wynik = fibonacci(n)
print("Wyraz ciągu Fibonacciego to:",wynik)

#Zadanie 10
def wspolne_elementy(obiekt1, obiekt2):
    wspolne = set(obiekt1) & set(obiekt2)
    return list(wspolne)


obiekt1 = [10, 20, 30, 40]
obiekt2 = [20, 50, 30,25]

wynik = wspolne_elementy(obiekt1, obiekt2)
print("Wspólne elementy:", wynik)




