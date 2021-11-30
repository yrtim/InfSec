import math
import random

def make_list_of_primes(n):
    list_of_primes = [2]
    prime = 3
    while prime < n:
        is_prime = True
        i = 0
        root = int(math.sqrt(prime))
        while list_of_primes[i] <= root:
            if prime % list_of_primes[i] == 0:
                is_prime = False
            i += 1
        if is_prime:
            list_of_primes.append(prime)

        prime += 1
    return list_of_primes

def get_a():
    return random.randint(0,1000)

def base(list):
    list.append(get_g())
    list.append(get_g())
    list.append(get_a())

def get_g():
    return make_list_of_primes(1000)[random.randint(0,len(make_list_of_primes(1000)))]


def get_key(alice, bob):
    alice.append(get_partial_key(bob,0))
    bob.append(get_partial_key(alice,0))
    alice.append(get_partial_key(alice,3))
    bob.append(get_partial_key(bob,3))

    return alice[3],bob[3]

def get_partial_key(list,n):
    return list[n]**list[2]%list[1]


alice = []
base(alice)
bob = alice[:2]
bob.append(get_a())
a,b = get_key(alice,bob)
print(alice, bob)



