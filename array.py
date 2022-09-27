# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 17:09:34 2022

@author: afdr9
"""

#Pro.01
#import array as ar
#given = ar.array('i',[1,3,5,7,9])
#print(given[0])
#print(given[1])
#print(given[2])

#Pro.02
#import array as ar
#given = ar.array('i',[1,3,5,7,9])
#given.append(11)
#x = str(given)
#print('New array: ', x)

#Pro.03
#import array as ar
#given = ar.array('i',[1,3,5,3,7,1,9,3])
#given.reverse()
#x = str(given)
#print('Reverse the order of the items:   ', x)

#Pro.04
#import array as ar
#given = ar.array('i',[1,3,5,7,9])
#x = given.itemsize
#print('Length in bytes of one array item: ',x)

#Pro.05
#import array as ar
#given = ar.array('i',[1,3,5,7,9])
#b = given.buffer_info()
#i = given.itemsize
#print('Current memory and length in elements of the buffer:   ',b)
#print('The size of the memory buffer in byte:   ',i)

#Pro.06
#import array as ar
#given = ar.array('i',[1,3,5,3,7,9,3])
#x = given.count(5)
#print('Number of occurrences of the number 3 in given array: ',x)

#Pro.07
#import array as ar
#given = ar.array('i',[1,3,5,7,9])
#given.extend(given)
#a = str(given)
#print('Extended array: ',a)

#Pro.08
#import array as ar
#print('Bytes to string: ')
#given = ar.array('i',[119,51,114,101,115,117,114,99,101])
#y = given.tobytes()
#print(y)
#Pro.09
#import array as ar
#given_list = [1,2,6,-8]
#given_array = ar.array('i',[])
#given_array.fromlist(given_list)
#a = str(given_array)
#print('Items in the array: ',a)

#Pro.10
#import array as ar
#given = ar.array('i',[1,3,5,7,9])
#given.insert(1,4)
#a = str(given)
#print('New array: ',a)