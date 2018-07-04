#!/usr/bin/env python
from pythonds.basic.deque import Deque

def palindrome(str):
    match = true
    deqChk = Deque()
    
    for s in str:
        deqChk.addFront(s)

    i=1
    while i < deqChk.size() and match:
        first = deqChk.removeFront()
        last = deqChk.removeRear()

        if first != last:
           match = false
       
    return match

print(palindrome('radar'))
print(palindrome('gurpreet'))
 
if _name_== "_main_":
   main()
