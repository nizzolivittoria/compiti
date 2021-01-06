print ("elezioni ballottaggio")
x = int (input("il primo quanti voti ha ottenuto?"))
y = int (input("il secondo quanti voti ha ottenuto?"))
z = x + y
d = (x/z)*100
u = (y/z)*100
print ("la percentuale del primo è", d, "%")
print ("la percentuale del secondo è", u, "%")
if d > u:
    print ("il primo candidato è il vincitore")
if u > d:
    print ("il secondo candidato è il vincitore")
if d == u:
    print ("i due candidati sono pari")       
