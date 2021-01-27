nazioni = ["Italia", "Francia", "Germania", "Spagna", "Inghilterra", "Grecia", "Turchia", "Portogallo"]
capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Londra", "Atene", "Ankara", "Lisbona"]
diz = {}
numero = len(nazioni)
for num in range(0, numero):
    diz[nazioni[num]] = capitali[num]
print("questa è una lista di paesi: Italia, Francia, Germania, Spagna, Inghilterra, Grecia, Turchia e Portogallo ")
while True:
    scelta = input("inserisci il paese di cui vuoi sapere la capitale:").capitalize()
    if scelta in diz.keys():
        print("la capitale è:", diz[scelta])
        scelta2 = int(input("premi 0 per saperne un'altra e 1 per abbandonare"))
        if scelta2 == 1:
            break
        elif scelta2 == 0:
            print("scrivi un altro paese")
        else:
            print("questo comando non fa nulla")
            break
    elif scelta not in diz.keys():
        print("scrivi un altro paese che questo non è nella lista")
    else:
        pass
