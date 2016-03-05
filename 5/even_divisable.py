#!/usr/bin/env python3
i = 2520

while not all(i % x == 0 for x in [11, 13, 14, 16, 17, 18, 19, 20]):
   i += 2520

print(i)
