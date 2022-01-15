import string
import copy
import math
import AdvNumber
import TreevideNConq

def basicArithmetic(val1, val2, op):
    if op == "-":
        return val1 - val2
    elif op == "*":
        return val1 * val2
    elif op == "+":
        return val1 + val2
        
        
# print(AdvNumber(3,4,"*"))
a = AdvNumber.AdvNumber(3,4,"/")
# b = AdvNumber(10,5,"/")
c = AdvNumber.AdvNumber(a, 1, "+")
print(a)
# print(b)
print(c)
# print(AdvNumber(3,4,"-"))
# print(AdvNumber(3,4,"+"))

# Shit commenting below
"""
AdvNumber(2 , [a,b,c,d] , [*,*,*,/])
2*a*b*c/d 

2*a

num_numerator = [2,a,b,c]
combine(AdvNumber , AdvNumber, *)
"""