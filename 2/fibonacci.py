#!/usr/bin/env python3
i = j = 1
sum = 0

while i < 4000000:
   if i % 2 == 0:
      sum += i

   tmp = i
   i += j
   j = tmp

print(sum)
