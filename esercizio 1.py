print("parole polindrome")

s = input("inserisci una parola per scoprire se è polindroma:\n")
s2 = s [:: - 1]
if s == s2:
    print("è polindroma!")
else:
    print("non è polindroma")
