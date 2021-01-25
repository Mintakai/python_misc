# Toisessa tehtävässä luodaan ohjelma, joka osaa selviytyä useammasta virhetyypistä. Tee ohjelma, joka pyytää käyttäjältä tiedoston nimen, 
# sekä avaa ja lukee tiedoston sisällön. Tämän jälkeen ohjelma yrittää muuttaa tiedostosta luetun arvon kokonaisluvuksi, sekä lisätä siihen arvon 313. 
# Jos kaikki menee oikein, ohjelma tulostaa vastauksen "Saatiin tulos [tulos]". Jos annettu tiedoston nimi on virheellinen, tulostetaan "Virheellinen tiedostonnimi". 
# Jos taas tiedoston sisältö on virheellinen eikä käänny kokonaisluvuksi, tulostetaan "Tiedoston sisältö virheellinen!". Toimiessaan ohjelma tulostaakin seuraavaa:

filen = input("Anna tiedoston nimi: ")

try:
    with open(filen, 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("Virheellinen tiedostonimi")
    quit()

try:
    content = int(content)
except ValueError:
    print("Tiedoston sisältö virheellinen!")
content += 313

print(f"Saatiin tulos: {content}")