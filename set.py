# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:18:55 2022

@author: afdr9
"""
#Pro.01
#s = set()
#s = set(0,1,2,3,4)
#print(s)

#Pro.02
#s = set([0,1,2,3,4,5])
#for n in s:
#    print(n, end = ' ')
#print('\nCreating a set using string: ')
#char_set = set('w3resource')
#for val in char_set:
#    print(val, end =' ')
    
#Pro.03
#color = set()
#print(color)
#print('\nAdd single element:')
#color.add('Red')
#print(color)
#print('\nAdd mutiple items:')
#color.update(['Blue','Green'])
#print(color)

#Pro.04
#given = {0,1,2,3,4,5}
#print('Original set: ',given)
#given.pop()
#print('After removing: ',given)

#Pro.05
#given = {0,1,2,3,4,5}
#print('Original set: ', given)
#given.discard(4)
#print('Remove 4 from original set: ',given)
#given.discard(5)
#print('Continue removing 5: ',given)
#given.discard(5)
#print('Continue removing 5: ',given)
#given.discard(15)
#print('Continue removing 15: ', given)

#Pro.06
#setx = set(['green', 'blue'])
#sety = set(['blue','yellow'])
#print('Original set elements: ')
#print(setx)
#print(sety)
#print('Intersection of two given sets:')
#print(setx & sety)

#Pro.07
#set1 = set(['green', 'blue'])
#set2 = set(['blue', 'yellow'])
#set12 = set1.union(set2)
#print(set1)
#print(set2)
#print('Union set:\n',set12)
#set3 = set([1,1,2,3,4,5])
#set4 = set([1,5,6,7,8,9])
#set34 = set3.union(set4)
#print(set3)
#print(set4)
#print('Union set:\n',set34)

#Pro.08
#set1 = set(['green','blue'])
#set2 = set(['blue','yellow'])
#set1_2 = set1.difference(set2)
#set2_1 = set2.difference(set1)
#print('Difference of set 1:\n', set1_2)
#print('Difference of set 2:\n', set2_1)
#set3 = set([1,1,2,3,4,5])
#set4 = set([1,5,6,7,8,9])
#set3_4 = set3.difference(set4)
#set4_3 = set4.difference(set3)
#print('Difference of set 3:\n', set3_4)
#print('Difference of set 4:\n', set4_3)

#Pro.09
#set1 = set(['green','blue'])
#set2 = set(['blue','yellow'])
#set12 = set1.symmetric_difference(set2)
#print('Symmetric difference:\n',set12)
#set3 = set([1,1,2,3,4,5])
#set4 = set([1,5,6,7,8,9])
#set34 = set3.symmetric_difference(set4)
#print('Symmetric difference:\n',set34)

#Pro.10
#setx = set(['apple','mango'])
#sety = set(['mango','orange'])
#setz = set(['mango'])
#print('If x is subset of y:   ', setx <= sety)
#print('If y is subset of x:   ', sety <= setx)
#print('If y is subset of z:   ', sety <= setz)
#print('If z is subset of y:   ', setz <= sety)
