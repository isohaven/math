# sieve of eratosthenes implementation
def prime_factors(n):
    A = [True] * n
    A[0] = A[1] = False
    for (i, is_prime) in enumerate(A):
        if is_prime:
            yield i
            for j in range(i*i, n, i):
                A[j] = False
print(list(prime_factors(1000)))
