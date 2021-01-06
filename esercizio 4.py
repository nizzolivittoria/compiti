print ("area quadrato, rettangolo, triangolo e cerchio")

latoq = int(input ("quanto è il lato del quadrato?"))
areaq = latoq ** 2
print ("l'area del quadrato è:", areaq)

altezzar = int(input ("quanto è l'altezza del rettangolo?"))
baser = int(input ("quanto è la base del rettangolo?"))
arear = altezzar * baser
print ("l'area del rettangolo è:", arear)

altezzat = int(input ("quanto è l'altezza del triangolo?"))
baset = int(input ("quanto è la base del triangolo?"))
areat = (altezzat * baset)/2
print ("l'area del triangolo è:", areat)

raggioc = int(input ("quanto è il raggio del cerchio?"))
areac = (raggioc * 2) * 3.14
print ("l'area del cerchio è:", areac)
