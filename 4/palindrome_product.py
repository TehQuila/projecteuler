#!/usr/bin/env python3
result = 0
i = j = 100

def is_palindrome(s):
   left, right = s[:len(s)//2], s[len(s)//2:]
   if left == right[::-1]:
      return True
   return False

while i < 1000:
   while j < 1000:
      k = i * j
      if is_palindrome(str(k)) and k > result:
         result = k
      j += 1
   i += 1
   j = i

print(result)
