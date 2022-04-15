a = 315
b = 840
while b>0:
    a %= b
    a, b = b, a

print(a)

def func(a, b):
    if b==0:
        return 1
    print(a, b)
    tmp = func(a, b//2)
    if b%2!=0:
        return tmp*tmp*a
    else:
        return tmp*tmp

res = func(3,5)
print(res)

