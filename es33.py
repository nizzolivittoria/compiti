pazienti = []
while True:
    paziente = input("scrivi il nome del paziente (se scriverai stop il programma si fermerà) ")
    paziente = paziente.capitalize()
    if paziente == "Stop":
        break
    else: 
        pazienti.append(paziente)
primo = pazienti.pop(0)
print("Il primo paziente nella lista è", primo)
while len(pazienti)>0:
    input("invio per passare al prossimo")
    paziente=pazienti.pop(0)
    print("il prossimo paziente è", paziente)
