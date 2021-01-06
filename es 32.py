numeroa = int(input("scrivi il valore di a"))
numerob = int(input("scrivi il valore di b"))

if numeroa == 0 and numerob == 0 :
    print("l'equazione è indeterminata")
elif numeroa != 0 and numerob == 0:
    print("la risoluzione dell'equazione è x=0")
elif numeroa == 0 and numerob != 0:
    print("l'equazione è impossibile")
elif numeroa != 0 and numerob != 0:
    print("la risoluzione dell'equazione è x=-b/a")
