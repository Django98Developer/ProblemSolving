def index(list, n):
    if len(list)-1 < n:
        return -1
    else:
        return (len(list)-1)**n


list = [1]
print(index(list, 0))
