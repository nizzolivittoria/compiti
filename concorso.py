print("concorso")
l = input("nome primo candidato")
r = input ("nome secondo candidato")
x = int (input("punteggio primo candidato:"))
y = int (input("punteggio secondo candidato;"))
if x>y:
    print("ordine decrescente punteggio:", x, y)
if x<y:
    print("ordine decrescente punteggio", y, x)
list = [l, r]
list.sort()
print("ordine alfabetico:", list)
