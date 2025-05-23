from typing import List

def podzbiory(x: List[str]) -> List[List[str]]:
    """
    Funkcja generuje wszystkie możliwe podzbiory danej listy ciągów znaków.

    :param x: List[str] - lista elementów wejściowych, dla której mają zostać wygenerowane podzbiory.
    :return: List[List[str]] - lista wszystkich możliwych podzbiorów.
    :raises ValueError: jeśli lista wejściowa jest pusta.
    """
    if not x:
        raise ValueError("Lista nie może być pusta.")

    wynik: List[List[str]] = [[]]  # zaczynamy od pustego podzbioru

    for element in x:
        #Robimy kopię aktualnych podzbiorów, żeby nie iterować po rozszerzanej liście
        nowe_podzbiory = [podzbior + [element] for podzbior in wynik]
        wynik.extend(nowe_podzbiory)

    # Usuwamy pusty podzbiór
    return [podzbior for podzbior in wynik if podzbior]

#TESTY

print("\nPoprawny zbiór: [a,b,c]")
try:
    wynik = podzbiory(["a", "b", "c"])
    print("Wszystkie podzbiory zbioru [a,b,c]:")
    for podzbior in wynik:
        print(podzbior)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

print("\nDuży zbiór: [a,b,c,d,e,f]")
try:
    wynik = podzbiory(["a","b","c","d","e","f"])
    print("Wszystkie podzbiory zbioru [a,b,c,d,e,f]:")
    for podzbior in wynik:
        print(podzbior)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)
print("\nPusty: []")
try:
    wynik = podzbiory([])
    print("Wszystkie podzbiory zbioru []:")
    for podzbior in wynik:
        print(podzbior)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

print("\nDla pojedyńczego elementu [b]")
try:
    wynik = podzbiory(["b"])
    print("Wszystkie podzbiory zbioru [b]:")
    for podzbior in wynik:
        print(podzbior)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

print("\nDla różnych elementów: [a,b,1,c,d]")
try:
    wynik = podzbiory(["a","b","1","c","d"])
    print("Wszystkie podzbiory zbioru [a,b,1,c,d]:")
    for podzbior in wynik:
        print(podzbior)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

print("\nDla samych liczb: [1,2,3,4,5]")
try:
    wynik = podzbiory(["1","2","3","4","5"])
    print("Wszystkie podzbiory zbioru [1,2,3,4,5]:")
    for podzbior in wynik:
        print(podzbior)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

print("\nDla znaków: [.,!,&,#,@]")
try:
    wynik = podzbiory([".","!","&","#","@"])
    print("Wszystkie podzbiory zbioru [.,!,&,#,@]:")
    for podzbior in wynik:
        print(podzbior)
    print("Poprawny wynik")
except Exception as e:
    print("Błąd!", e)

    
#Podczas tworzenia kodu korzystałam z następujących źródeł:
#https://github.com/AmeliaNiedzwiadek/jezykiprogramowania
#https://www.youtube.com/watch?v=Au3LR8GUKrc
#https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
#https://docs.python.org/3/library/stdtypes.html#typesseq-mutable
#https://www.geeksforgeeks.org/power-set/

    

    

    

