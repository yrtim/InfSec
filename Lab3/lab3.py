import random
import math

def keys_for_rsa(p,q):
    n=p*q
    z = (p - 1) * (q - 1)
    e = 0
    d = 0
    for i in range(2,z):
        if math.gcd(i,z)==1:
            e = i
            break
    for i in range(z):
        temp = 1 + i*z
        if temp % e == 0:
            d = int(temp/e)
    return [e,n], [d,n]

def get_prime():
    while True:
        number = random.randint(11, 999)
        if  miller_rabin(number,10000) is True:
            return number

def miller_rabin(n, k):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
     return True

def encrypt(text, keys):
    encrypted_text = []
    for i in text:
        encrypted_text.append(pow(ord(i),keys[0])%keys[1])
    return encrypted_text

def decrypt(text, keys):
    decrypted_text = ''
    for i in text:
        decrypted_text += chr(pow(i,keys[0])% keys[1])
    return decrypted_text

public, private = keys_for_rsa(get_prime(), get_prime())
text = 'ага'
en = encrypt(text,public)
print(en)
de = decrypt(en,private)
print(de)
print(text)
