# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 21:29:27 2022

@author: afdr9
"""
#Pro.01
#import operator
#d = {1:2, 3:4, 4:3, 2:1, 0:0}
#print('Original dictionary:',d)
#sorted_d = sorted(d.items(), key = operator.itemgetter(1))
#print('Dictionary in ascending order by value: ', sorted_d)
#sorted_d = dict(sorted(d.items(), key = operator.itemgetter(1), reverse = True))
#print('Dictionary in descending order by value: ', sorted_d)

#Pro.02
#d = {0:10, 1:20}
#print(d)
#d.update({2:30})
#print(d)

#Pro.03
#dic1 = {1:10, 2:20}
#dic2 = {3:30, 4:40}
#dic3 = {5:50, 6:60}
#dic4 = {}
#for i in (dic1, dic2, dic3):
#    dic4.update(i)
#print(dic4)

#Pro.04
#d = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
#def already(i):
#    if i in d:
#        print('Key is present in the dictionary')
#    else:
#        print('Key is not present in the dictionary')
#already(5)
#already(9)

#Pro.05
#d = {'x':10, 'y':20, 'z':30}
#for key,value in d.items():
#    print(key, '->', value)
    
#Pro.06
#n = int(input('Input a number: '))
#d = dict()
#for x in range(1,n+1):
#    d[x] = x*x
#print(d)

#Pro.07
#d = dict()
#for i in range(1,16):
#    d[i] = i**2
#print(d)

#Pro.08
#dic1 = {'a':100, 'b':200}
#dic2 = {'x':300, 'y':200}
#d = {}
#for i in (dic1, dic2):
#    d.update(i)
#print(d)

#Pro.09
#d = {'red':1, 'green':2, 'blue':3}
#for key, value in d.items():
#    print(key, '->', value)

#Pro.10
#d ={'data1':100, 'data2':-54, 'data3':247}
#print(sum(d.values()))