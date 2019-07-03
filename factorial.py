# memoized factorial recursive algo
# AZR

factorial_cache = {}
def memoized_factorial(n):
    if n == 0:
        return 1
    elif n in factorial_cache:
        return factorial_cache[str(n)]
    else:
        ans = n * memoized_factorial(n-1)
        factorial_cache[str(n)] = ans
        return ans

def main():
    n = -1
    while n < 0:
        print('enter positive integer')
        try:
            n = int(input())
        except ValueError:
            n = -1
            print('invalid input')
    ans = memoized_factorial(n)
    print(f'{n}! = {ans}')

main()


