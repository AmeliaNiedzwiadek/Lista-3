def fib_iter(n):
    """
    Oblicza listę n pierwszych liczb ciągu Fibonacciego przy użyciu iteracji.

    :param n: int – liczba elementów ciągu do wygenerowania (n >= 0)
    :return: list[int] – lista n pierwszych liczb Fibonacciego
    :raises ValueError: jeśli n nie jest liczbą całkowitą lub jest mniejsze od 0
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi być liczbą całkowitą >= 0")

    a, b = 0, 1
    wynik = []
    for _ in range(n):
        wynik.append(a)
        a, b = b, a + b

    return wynik



def fib_rek(n):

    """
    Oblicza listę n pierwszych liczb ciągu Fibonacciego przy użyciu rekurencji.
    
    :param n: int - liczba elementów ciągu do wygenerowania (n >= 0)
    :return: list[int] - lista n pierwszych liczb Fibonacciego
    :raises ValueError: jeśli n nie jest liczbą całkowitą lub jest mniejsze od 0
    """
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("n musi być liczbą całkowitą >= 0")

    def fib(k):
        if k == 0:
            return 0
        elif k == 1:
            return 1
        return fib(k - 1) + fib(k - 2)

    wynik = [fib(i) for i in range(n)]


    return wynik


        # TESTY dla fib_iter i fib_rek

print("TEST 1: n = 5 (oczekiwany wynik: [0, 1, 1, 2, 3])")
try:
    wynik = fib_iter(5)
    print("fib_iter(5):", wynik)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

try:
    wynik = fib_rek(5)
    print("fib_rek(5):", wynik)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

print("\nTEST 2: n = 0 (oczekiwany wynik: [])")
try:
    print("fib_iter(0):", fib_iter(0))
except Exception as e:
    print("Błąd!", e)

try:
    print("fib_rek(0):", fib_rek(0))
except Exception as e:
    print("Błąd!", e)

print("\nTEST 3: n = 1 (oczekiwany wynik: [0])")
try:
    print("fib_iter(1):", fib_iter(1))
except Exception as e:
    print("Błąd!", e)

try:
    print("fib_rek(1):", fib_rek(1))
except Exception as e:
    print("Błąd!", e)

print("\nTEST 4: n = -3")
try:
    print("fib_iter(-3):", fib_iter(-3))
except Exception as e:
    print("Błąd!", e)

try:
    print("fib_rek(-3):", fib_rek(-3))
except Exception as e:
    print("Błąd!", e)

print("\nTEST 5: n = 'tekst'")
try:
    print("fib_iter('tekst'):", fib_iter("tekst"))
except Exception as e:
    print("Błąd!", e)

try:
    print("fib_rek('tekst'):", fib_rek("tekst"))
except Exception as e:
    print("Błąd!", e)

    print("\nTEST 6: n = 10")
try:
    wynik = fib_iter(10)
    print("fib_iter(10):", wynik)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

try:
    wynik = fib_rek(10)
    print("fib_rek(10):", wynik)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)




#Podczas tworzenia kodu korzystałam z następujących źródeł:
#https://www.algorytm.edu.pl/algorytmy-w-python/ciag-fibonacciego-python
#https://www.youtube.com/watch?v=7Sv4NmvdHcw
#https://github.com/AmeliaNiedzwiadek/jezykiprogramowania
#https://docs.python.org/3/
