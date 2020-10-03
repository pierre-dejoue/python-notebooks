"""
References:
- Helmut Vogel (1979) A better way to construct the sunflower head
"""
import math

golden =  (math.sqrt(5) + 1.0) / 2.0
phi =     (math.sqrt(5) - 1.0) / 2.0
phi_rad = 2.0 * math.pi * phi

def fibo(n):
    """Returns the nth Fibonacci number"""
    if n < 2:
        return 1
    else:
        return int(round(pow(golden, n + 1) / math.sqrt(5)))

def radius(n):
    return math.sqrt(n + 1)

def angle(n):
    return n * phi_rad
