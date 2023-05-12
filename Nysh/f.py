def inp( n, a[n]):
    for i in range(n):
        el = int(input())
        a.append(el)

def televna( n, a[n], summa):
    for i in range(n):
        if a[i] % 2 == 0:
            summa += a[i]
