print ("media stipendi diependenti azienda")
st = 0
count = 0
while True:
    s = int(input("stipendio del dipendente:"))
    if s == -1:
        break
    st += s
    count += 1
print (st / count)
