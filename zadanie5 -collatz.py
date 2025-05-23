from typing import List

def collatz(c0: int) -> List[int]:
    """
    Funkcja generuje ciąg Collatza dla zadanej liczby początkowej c0.

    :param c0: int - liczba początkowa, musi być większa od zera.
    :return: List[int] - lista zawierająca kolejne wartości ciągu Collatza.
    :raises ValueError: jeśli podana liczba jest mniejsza lub równa zero.
    """
    if c0 <= 0:
        raise ValueError("c0 musi być większe od zera.")

    wynik = []
    c = c0

    while c != 1:
        wynik.append(c)
        c = c // 2 if c % 2 == 0 else 3 * c + 1

    wynik.append(1)
    return wynik

# TESTY
print("TESTY FUNKCJI COLLATZ")

print("\nLiczba: 6")
try:
    wynik = collatz(6)
    print("Wynik:", wynik)
    print("Poprawny wynik")
except ValueError as e:
    print("Błąd:", e)

print("\nLiczba: 1")
try:
    wynik = collatz(1)
    print("Wynik:", wynik)
    print("Poprawny wynik")
except ValueError as e:
    print("Błąd:", e)

print("\nLiczba: -5")
try:
    wynik = collatz(-5)
    print("Wynik:", wynik)
except ValueError as e:
    print("Błąd:", e)

print("\nLiczba: 0")
try:
    wynik = collatz(0)
    print("Wynik:", wynik)
except ValueError as e:
    print("Błąd:", e)

print("\nliczba: 27")
try:
    wynik = collatz(27)
    print("Długość ciągu:", len(wynik))
    print("Ostatnie elementy:", wynik[-5:])  # tylko ostatnie, bo ciąg jest długi
    print("Poprawny wynik")
except ValueError as e:
    print("Błąd:", e)

print("\nNieprawidłowy typ: 'tekst'")
try:
    wynik = collatz("tekst")
    print("Wynik:", wynik)
except ValueError as e:
    print("Błąd:", e)
except TypeError as e:
    print("Błąd typu:", e)

#Do utworzenia tego kodu korzystałam z następujących źródeł:
#https://github.com/AmeliaNiedzwiadek/jezykiprogramowania/blob/main/zadanie5.kt
#https://www.youtube.com/watch?v=utoIoLDMDTs
#https://how.dev/answers/how-to-generate-the-collatz-sequence-in-python
#https://docs.python.org/3/
    
