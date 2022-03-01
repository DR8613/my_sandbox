# ZADANIE DOMOWE DODATKOWE:
# Napisz funkcje która zadanej liście zliczy
# Wszystkie elementy które mają '.pl' ale tylko '.pl' a nie 
# np. '.eu.pl', '.site.pl', '.com.pl' < --- tych nie zliczamy.
# Czyli funkcja bierze listę stringów z domenami
# Zlicza same '.pl'
# Zwraca liczbe samych '.pl'

# Możesz użyć poniższego przykładu i wcześniejszych kodów aby rozwiązać zadanie.
def policz_domeny_pl(lista):
    licz=0
    for i, adresy in enumerate(lista):
        if '.com.pl' in adresy:
           continue
        elif '.pl' in adresy:
            licz += 1
    return licz

wynik = policz_domeny_pl(linki)
print(wynik )