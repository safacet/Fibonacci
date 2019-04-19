a= 1
b= 1
liste = [a, b]
for i in range(20):
    a,b = b, b+a
    liste.append(b)
print(liste)