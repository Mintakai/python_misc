# Toisessa tehtävässä luodaan ohjelma, joka osaa selviytyä useammasta virhetyypistä. Tee ohjelma, joka pyytää käyttäjältä tiedoston nimen, 
# sekä avaa ja lukee tiedoston sisällön. Tämän jälkeen ohjelma yrittää muuttaa tiedostosta luetun arvon kokonaisluvuksi, sekä lisätä siihen arvon 313. 
# Jos kaikki menee oikein, ohjelma tulostaa vastauksen "Saatiin tulos [tulos]". Jos annettu tiedoston nimi on virheellinen, tulostetaan "Virheellinen tiedostonnimi". 
# Jos taas tiedoston sisältö on virheellinen eikä käänny kokonaisluvuksi, tulostetaan "Tiedoston sisältö virheellinen!". Toimiessaan ohjelma tulostaakin seuraavaa:

while True:
    try:
        with open(input("Anna tiedoston nimi: "), 'r') as f:
            content = f.read()
        print(f"Saatiin tulos {int(content) + 313}")
    except IOError:
        print("Virheellinen tiedoston nimi")
    except ValueError:
        print("Tiedoston sisältö virheellinen!")