print ("transito veicoli")
lista_v = []
count = True
n = 0
r = 0
s = 0
while count == True:
    n += 1
    r += 1
    print(" il numero dei veicoli entrati nel giorno", n,": ")
    v = int(input())
    lista_v.append(v)

    if r == 3:
        x = int(input("vuoi uscire dal casello? se vuoi uscire scrivi 0, se no premi 1 : "))
        r = 0
        if x == 0:
            count = False
        else:
            pass
for i in lista_v:
    s += i
print("in", n,"giorni, sono entrati", s, "veicoli")
