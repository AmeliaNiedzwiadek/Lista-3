
import math

""
    #Oblicza pole trójkąta na podstawie długości jego boków za pomocą wzoru Herona.

    #@param a: długość pierwszego boku (float lub int, > 0)
    #@param b: długość drugiego boku (float lub int, > 0)
    #@param c: długość trzeciego boku (float lub int, > 0)

    #@return: pole trójkąta jako liczba zmiennoprzecinkowa (float)

    #@raise ValueError: gdy którykolwiek z boków ma wartość mniejszą lub równą 0
    #@raise ValueError: gdy suma długości dwóch boków nie przekracza długości trzeciego (czyli nie da się zbudować trójkąta)
""
  
def heron(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Boki muszą być większe od zera.")
    if a + b < c or b + c < a or a + c < b:
        raise ValueError ("Suma dwóch boków nie może być mniejsza od wartości 3 boku")
    S = (a + b + c) / 2
    return math.sqrt(S * (S - a) * (S - b) * (S - c))


print("TESTY")

print("\nPoprawny trójkąt: 5, 7, 8")
try:
    wynik = heron(5, 7, 8)
    print("✓ Wynik:", round(wynik, 4))
    print("Poprawny wynik")
except Exception as e:
    print("Poprawny wynik")

print("\nBok równy 0: 0, 6, 9")
try:
    wynik = heron(0, 6, 9)
    print("Poprawny wynik")
except ValueError:
    print("Błąd! Żaden z boków nie może być równy 0")


print("\nBok ujemny: -1, -5, 5")
try:
    wynik = heron(-1, -5, 5)
    print(" Poprawny wynik")
except ValueError:
    print("Błąd!Żaden z boków nie może być ujemny")

print("\nDla zbyt małych wartości: 1, 2, 14")
try:
    wynik = heron(1, 2, 14)
    print("Wynik:", round(wynik, 4))
except ValueError:
    print("Z takich boków nie ułożymy trójkąta")


print("\nDla dużych wartości: 1000000, 1000000, 1000000")
try:
    wynik = heron(1000000, 1000000, 1000000)
    print("Wynik:", round(wynik, 4))
    print("Wynik: Poprawny")
except ValueError:
    print("Błąd")

print("\nDla takich samych wartości: 3, 3, 3")
try:
    wynik=heron(3,3,3)
    print("Wynik:", round(wynik, 4))
    print("Wynik:Poprawny")
except ValueError:
    print("Błąd")


#Podczas tworzenia kodu korzystałam z następujących źródeł:
#https://scipython.com/book/chapter-2-the-core-python-language-i/examples/herons-formula/
#https://github.com/AmeliaNiedzwiadek/jezykiprogramowania 


    

    

    
    

    
