def wspolne(x, y):
    """
    Funkcja zwraca część wspólną dwóch list.
    
    :param x: List[int] - pierwsza lista
    :param y: List[int] - druga lista
    :return: List[int] - lista wspólnych elementów (bez powtórzeń)
    """
    if not isinstance(x, list) or not isinstance(y, list):
        raise ValueError("Oba argumenty muszą być listami.")
    
    if not x or not y:
        raise ValueError("Listy nie mogą być puste.")

    if not all(isinstance(el, (int, float)) for el in x + y):
        raise ValueError("Listy muszą zawierać tylko liczby.")

    wynik = []
    y_kopia = y.copy() #Tworzymy kopię listy y, żeby móc usuwać elementy

    for el in x:
        if el in y_kopia:
            wynik.append(el)  #Dodajemy wspólny element do wyniku
            y_kopia.remove(el) #Usuwamy go z kopii, żeby nie zliczyć go ponownie

    return wynik


# TESTY
print("TESTY")

print("\nPoprawna lista: [1, 2, 3, 4] i [2, 4, 5]")
try:
    wynik = wspolne([1, 2, 3, 4], [2, 4, 5])
    print("Poprawny wynik:", wynik)
except ValueError as e:
    print("Błąd:", e)

print("\nLista pusta: [], [1, 2, 3]")
try:
    wynik = wspolne([], [1, 2, 3])
    print("Wynik:", wynik)
except ValueError as e:
    print("Błąd:", e)

print("\nLista z nie-liczbami:[1, a, 3], [1, 2]")
try:
    wynik = wspolne([1, "a", 3], [1, 2])
    print("Wynik:", wynik)
except ValueError as e:
    print("Błąd:", e)

print("\nLista  bez żadnego wspólnego elementu:[1, 2, 3], [4, 5]")
try:
    wynik = wspolne([1, 2, 3], [4, 5])
    print("Wynik:", wynik)
except ValueError as e:
    print("Błąd:", e)

print("\nLista z dużymi wartościami: [1000, 1001, 1002, 1003] i [1000, 2000, 3000]")
try:
    wynik = wspolne( [1000, 1001, 1002, 1003], [1000, 2000, 3000])
    print("Poprawny wynik:", wynik)
except ValueError as e:
    print("Błąd:", e)
    
#Podczas tworzenia kodu korzystałam z następujących źródeł:
#https://github.com/AmeliaNiedzwiadek/jezykiprogramowania
#https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#https://www.w3schools.com/python/python_lists.asp
#https://www.geeksforgeeks.org/python-intersection-two-lists/
#https://www.youtube.com/watch?v=WnQ36z4CR-4
    
    


        
