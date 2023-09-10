import random
import time

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = random.randint(15, 35)

start = time.time()
print(f"fib({n})={fibonacci(n)}")
end = time.time()
print(f"fib({n}) took {end - start} seconds")