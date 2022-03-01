from re import L
import requests
orangutan = 'https://zajecia-programowania-xd.pl/flagi'
surowe_info = requests.get( orangutan)
text = surowe_info.text

# Cel:
# Lista linków (wszystkich).

#Przygotowanie
lista_linii = text.split('</p>') #rozdziela po </p> i przechodzi do nowej lini

#Realizacja
linki = [] #tworzenie listy
#linki = list # drugi sposób tworzenia listy
for linia in lista_linii:

    link = linia.replace('<p>', '')  #przypisz linia jako LINK i zamień znaki <p> na '' za pomocą metody replace
    link = link.replace('- ', '')
    link = link.strip()
    if ' ' in link or '<' in link: # jesli jest spacja w lini lub dziubek
        continue
    linki.append( link)

for i, l in enumerate(linki):
    print(i, l) # wydrukuj LINIA - nowa zmienna

#Cel
#Policz ile jest domen pl
domeny_pl = 0
domeny_com = 0
domeny_x = 0

#Ile jest wszystkich kropek w linkach

wszystkie_kropki = 0

for i, link in enumerate(linki):
    if '.pl' in link:
        domeny_pl += 1
    if '.com' in link:
        domeny_com += 1
    if ('.pl' in link) and ('.com' in link):
        domeny_x += 1
    #Policz ile jest kropek w linku
    n_kropek = link.count('.')
    wszystkie_kropki += n_kropek

print(wszystkie_kropki)

print(domeny_pl)
print(domeny_com)
print(domeny_x)


 