def invert(lst):
    # nlst = []
    for i in range(len(lst)):
        # nlst.append(lst[i]*-1)
        lst[i] = lst[i]*-1
    return lst


L = int(input("Enter lenth of List : "))
lista = []

for j in range(0, L):
    lista.append(int(input("Enter a number")))


print(invert(lista))
