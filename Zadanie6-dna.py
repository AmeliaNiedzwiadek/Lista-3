def komplement(nic_kodujaca):
    """
    Tworzy nić matrycową (komplementarną) do podanej nici kodującej DNA.
    A <-> T, G <-> C, i na końcu odwracamy sekwencję.

    :param nic_kodujaca: str - nić kodująca DNA (np. "ATGC")
    :return: str - nić matrycowa DNA (np. "GCAT")
    :raises: ValueError jeśli sekwencja jest pusta lub zawiera nieprawidłowe znaki
    """
    if not nic_kodujaca:
        raise ValueError("Sekwencja DNA nie może być pusta.")
    if not all(n in "ATGC" for n in nic_kodujaca):
        raise ValueError("Sekwencja DNA zawiera nieprawidłowe znaki.")
    
    wynik = ""
    for znak in nic_kodujaca:
        if znak == "A":
            wynik += "T"
        elif znak == "T":
            wynik += "A"
        elif znak == "G":
            wynik += "C"
        elif znak == "C":
            wynik += "G"
    return wynik[::-1]

def transkrybuj(nic_matrycowa):
    """
    Tworzy RNA na podstawie nici matrycowej DNA.
    A -> U, T -> A, G -> C, C -> G. Odwracamy wynik.

    :param nic_matrycowa: str - nić matrycowa DNA
    :return: str - sekwencja RNA
    :raises: ValueError jeśli sekwencja jest pusta lub zawiera nieprawidłowe znaki
    """
    if not nic_matrycowa:
        raise ValueError("Sekwencja matrycowa nie może być pusta.")
    if not all(n in "ATGC" for n in nic_matrycowa):
        raise ValueError("Sekwencja matrycowa zawiera nieprawidłowe znaki.")
    
    wynik = ""
    for znak in nic_matrycowa:
        if znak == "A":
            wynik += "U"
        elif znak == "T":
            wynik += "A"
        elif znak == "G":
            wynik += "C"
        elif znak == "C":
            wynik += "G"
    return wynik[::-1]

def transluj(rna):
    """
    Tłumaczy RNA na białko, zakładając znajomość tylko kilku kodonów.

    :param rna: str - sekwencja RNA
    :return: str - sekwencja białka (np. "MA")
    :raises: ValueError jeśli sekwencja jest pusta lub zawiera nieprawidłowe znaki
    """
    if not rna:
        raise ValueError("Sekwencja RNA nie może być pusta.")
    if not all(n in "AUCG" for n in rna):
        raise ValueError("Sekwencja RNA zawiera nieprawidłowe znaki.")
    
    bialko = ""
    i = 0
    while i < len(rna) - 2:
        kodon = rna[i:i+3]
        if kodon == "AUG":
            bialko += "M"
        elif kodon == "UUU":
            bialko += "F"
        elif kodon in ["UAA", "UAG", "UGA"]:
            break  # kodon STOP
        else:
            bialko += "X"  # nieznany kodon
        i += 3
    return bialko

print("TESTY DNA/RNA")

print("\nTest 1 — Poprawna sekwencja: 'ATGC'")
try:
    m = komplement("ATGC")
    r = transkrybuj(m)
    b = transluj(r)
    print("Matrycowa:", m)
    print("RNA:", r)
    print("Białko:", b)
    print("Poprawny wynik")
except ValueError as e:
    print("Błąd:", e)

print("\nTest 2 — Sekwencja z błędnymi znakami: 'ATBX'")
try:
    m = komplement("ATBX")
    print("Matrycowa:", m)
except ValueError as e:
    print("Błąd:", e)

print("\nTest 3 — Pusta sekwencja DNA")
try:
    m = komplement("")
    print("Matrycowa:", m)
except ValueError as e:
    print("Błąd:", e)

print("\nTest 4 — Sekwencja RNA z błędnymi znakami: 'AUGZ'")
try:
    b = transluj("AUGZ")
    print("Białko:", b)
except ValueError as e:
    print("Błąd:", e)

print("\nTest 5 — RNA zawierające kodon STOP: 'AUGUUUUAA'")
try:
    b = transluj("AUGUUUUAA")
    print("Białko:", b)
    print("Poprawny wynik — translacja zakończona kodonem STOP")
except ValueError as e:
    print("Błąd:", e)

print("\nTest 6 — RNA bez znanych kodonów: 'ACGACG'")
try:
    b = transluj("ACGACG")
    print("Białko:", b)
    print("Wynik powinien zawierać same 'X'")
except ValueError as e:
    print("Błąd:", e)
#Podczas tworzenia kodu korzystałam z następujących źródeł:
#https://pl.wikipedia.org/wiki/Kod_genetyczny#Tabela_kodów
#https://docs.python.org/3/
#https://www.youtube.com/watch?v=M-ky7LkBWCk
#ChatGPT

    

