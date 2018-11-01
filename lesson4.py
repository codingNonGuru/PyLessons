mancare = "sandwich"
bautura = "cafea"

pret = 12
bacsis = 5

clienti = 7

numarulClientului = 0 

profit = 0

while numarulClientului < clienti:
    profit = profit + pret
    print("Clientul cu numarul " + str(numarulClientului) + " a comandat " + mancare)

    if numarulClientului % 3 is 0:
        profit = profit + bacsis
        print("A mai comandat si " + bautura)

    print(" ")

    numarulClientului = numarulClientului + 1

print("Profitul cafenelei este de " + str(profit))
