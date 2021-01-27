nazioni = ["Italia", "Francia", "Germania", "Spagna", "Inghilterra", "Grecia", "Turchia", "Portogallo"]
capitali = ["Roma", "Parigi", "Berlino", "Madrid", "Londra", "Atene", "Ankara", "Lisbona"]
print("questo è l'elenco dei paesi tra i quali puoi sceglliere: Italia, Francia, Germania, Spagna, Inghilterra, Grecia, Turchia e Portogallo ")

while True:
    scelta = input("scrivi il paese:").capitalize()
    numero = nazioni.index(scelta)
    if scelta in nazioni:
        print("la capitale di", scelta, ":", capitali[numero])
        scelta2 = int(input("premi 0 per saperne un'altra e 1 per uscire"))
        if scelta2 == 1:
            break
        elif scelta2 == 0:
            print("scrivi un altro paese")
        else:
            print("questo comando non fa nulla")
            break
    elif scelta not in nazioni:
        print("scrivi un altro paese che questo non è nella lista")
    else:
        pass
