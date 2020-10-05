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

class FiboGrowth:
    def __init__(self, r0, a0, area_slope = 0.0):
        assert area_slope >= 0.0
        self.r0 = r0
        self.a0 = a0
        self.da = area_slope

    def radius(self, n):
        return self.r0 * math.sqrt((1.0 + n) * (1.0 + n * self.da / 2.0))

    def angle(self, n):
        return n * phi_rad

    def area(self, n):
        return self.a0 * (1.0 + self.da * n)
