# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:57:07 2022

@author: afdr9
"""
#Pro.01
#def max2(x,y):
#    if x>y:
#        return x
#    return y
#def max3(x,y,z):
#    return max2(x,max2(y,z))
#print(max3(5,-2,11))

#Pro.02
#def sum(tuple):
#    s = 0
#    for i in tuple:
#        s += i
#    return s
#print(sum((8,2,3,0,7)))

#Pro.03
#def product(tuple):
#    p = 1
#    for i in tuple:
#        p *= i
#    return p
#print(product((8,2,3,-1,7)))

#Pro.04
#def reverse_str(str):
#    rstr = ''
#    index = len(str)
#    while index > 0:
#        rstr += str[index - 1]
#        index -= 1
#    return rstr
#print(reverse_str('1234abcd'))

#Pro.05
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n*factorial(n-1)
#n = int(input('Enter an integer:'))
#print(factorial(n))

#Pro.06
#def test(n):
#    if n in range (3,9):
#        print('%s is in the given range.' %n)
#    else:
#        print('%s is outside the given range.' %n)
#test(5)

#Pro.07
#def given(str):
#    d = {'UPPER_CASE':0,'lower_case':0}
#    for i in str:
#        if i.isupper():
#            d['UPPER_CASE'] += 1
#        elif i.islower():
#            d['lower_case'] += 1
#        else:
#            pass
#    print('Original string:   ',str)
#    print('No. of UPPER CASE:   ',d['UPPER_CASE'])
#    print('No. of lower case:   ',d['lower_case'])
#given('The quick Brown Fox')

#Pro.08
#def unique(lst):
#    x = []
#    for i in lst:
#        if i not in x:
#            x.append(i)
#    return x
#print(unique([1,2,3,3,3,3,4,5]))

#Pro.09
#def prm(n)            :
#    if (n == 1):
#        return False
#    elif(n == 2):
#        return True
#    else:
#        for i in range (2,n):
#            if (n%i == 0):
#                return False
#        return True
#print(prm(9))

#Pro.10
#def even(lst):
#    new_lst = []
#    for i in lst:
#        if i%2 == 0:
#            new_lst.append(i)
#    return new_lst
#print(even([1,2,3,4,5,6,7,8,9]))
                
#Pro.11
#def perfect(n):
#    s = 0
#    for i in range (1,n):
#        if n%i == 0:
#            s += i
#    return s == n
#print(perfect(10))

#Pro.12
#def palindrome(str):
#    left_pos = 0
#    right_pos = len(str) - 1
#    while right_pos >= left_pos:
#        if not str[left_pos] == str[right_pos]:
#            return False
#        left_pos += 1
#        right_pos -= 1
#    return True
#print(palindrome('aza'))

















