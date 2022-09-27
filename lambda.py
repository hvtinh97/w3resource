# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:28:09 2022

@author: afdr9
"""

#Pro.01
#r = lambda a: a+115
#print(r(10))
#r = lambda x,y : x*y
#print(r(12,4))

#Pro.02
#def compute(n):
#    return lambda x:x*n
#result = compute(2)
#print('Double the number of 15: ',result(15))

#Pro.03
#given = [('English',88),('Science',90),('Math',97),('Social sciences',82)]
#given.sort(key = lambda x:x[1])
#print('Sorting the list of tuples: ',given)

#Pro.04
#given = [{'make':'Nokia','model':216,'color':'Black'},{'make':'Mi Max','model':'2','color':'Gold'},{'make':'Samsung','model':7,'color':'Blue'}]
#new = sorted(given, key = lambda x:x['color'])
#print('\nSorting the lsit of dictionaries:')
#print(new)

#Pro.05
#given = [1,2,3,4,5,6,7,8,9,10]
#even_given = list(filter(lambda x:x%2 == 0, given))
#print(even_given)
#odd_given = list(filter(lambda x:x%2 != 0, given))
#print(odd_given)

#Pro.06
#given = [1,2,3,4,5,6,7,8,9,10]
#square_given = list(map(lambda x:x**2,given))
#print('\nSquare every number of the given list:')
#print(square_given)
#cube_given = list(map(lambda x:x**3,given))
#print(cube_given)

#Pro.07
#starts_with = lambda x: True if x.startswith('P') else False
#print(starts_with('Python'))

#Pro.08
#import datetime as dt
#now = dt.datetime.now()
#print(now)
#year = lambda x:x.year
#month = lambda x:x.month
#day = lambda x:x.day
#t = lambda x:x.time()
#print(year(now))
#print(month(now))
#print(day(now))
#print(t(now))

#Pro.09
#given = lambda q:q.replace('.','',1).isdigit()
#print(given('26587'))
#print(given('4.2365'))
#print(given('-12547'))
#print(given('00'))
#print(given('A001'))
#print(given('001'))
#print('\nPrint checking numbers:')
#new_given = lambda r: given(r[1:]) if r[0] == '-' else given(r)
#print(new_given('-16.4'))
#print(new_given('-24587.11'))

#Pro.10
#from functools import reduce
#fibonacci = lambda n : reduce(lambda x,_: x+[x[-1]+x[-2]], range(n-2),[0,1])
#print('Fibonacci series upto 2:')
#print(fibonacci(2))















