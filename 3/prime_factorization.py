#!/usr/bin/env python3
n = 600851475143
i = 2

while i * i <= n:
   if n % i == 0: n //= i
   else: i += 1

print(n)