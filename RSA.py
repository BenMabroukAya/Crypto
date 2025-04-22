def RSAd(n,b):
    n0 = n
    b0 = b
    t0 = 0
    t = 1
    q = int(n0 / b0)
    r = n0 - q * b0
    print("r=", r)
    while r > 0:
        temp = t0 - q * t
        if temp >= 0:
            temp = temp % n
        else:
            temp = ((n - (-temp)) % n)
        t0 = t
        t = temp
        n0 = b0
        b0 = r
        q = int(n0 / b0)
        r = n0 - q * b0
    if (b0 != 1):
        print("b n'a pas d'inverse modulo n ")
    else:
        print("b-1=", t)
print(RSAd(2668,335))

def RSA():
    