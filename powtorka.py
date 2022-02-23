import requests
orangutan = 'https://zajecia-programowania-xd.pl/flagi'
surowe_info = requests.get( orangutan)
text = surowe_info.text

# Cel:
# Lista linków.
efekt = text.split('</p>')
for linia in efekt:
    if '<p>' in linia:
        link = linia
        print(link)

