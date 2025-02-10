def fib_m(n, memo):
    if n == 0 or n == 1:
        memo[n] = n
        return n
    if memo[n] > 0:
        return memo[n]
    
    memo[n] = fib_m(n-1, memo) + fib_m(n-2, memo)
    return memo[n]

n = 10  
memo = [-1] * (n + 1) 
result = fib_m(n, memo)
print(f"Fibonacci({n}) = {result}")
