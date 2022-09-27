# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:06:32 2022

@author: afdr9
"""
#Pro.01
#def length(str):
#    s = 0
#    for i in str:
#        s += 1
#    return s
#print(length('I am 18 years old'))

#Pro.02
#def count(string):
#    dic = {}
#    for i in string:
#        keys = dic.keys()
#        if i in keys:
#            dic[i] += 1
#        else:
#            dic[i] = 1
#    return dic
#print(count('google.com'))

#Pro.03
#def new(string):
#    if len(string) < 2:
#        return ''
#    return string[:2] + string[-2:]
#print(new('w3resource'))
#print(new('w3'))
#print(new('w'))

#Pro.04
#def new(string):
#    cha = string[0]
#    string = string.replace(cha,'$')
#    string = cha + string[1:]
#    return string
#print(new('restart'))

#Pro.05
#def mixup(a,b):
#    newa = b[:2] + a[2:]
#    newb = a[:2] + b[2:]
#    return newa + ' ' + newb
#print(mixup('abc','xyz'))

#Pro.06
#def add(string):
#    if len(string) >= 3:
#        if string[-3:] == 'ing':
#            string += 'ly'
#        else:
#            string += 'ing'
#    return string
#print(add('ab'))
#print(add('abc'))
#print(add('string'))

#Pro.07
#def not_poor(string):
#    snot = string.find('not')
#    spoor = string.find('poor')
#    if spoor > snot and snot > 0 and spoor > 0:
#        string = string.replace(string[snot:(spoor+4)], 'good')
#        return string
#    else:
#        return string
#print(not_poor('The lyrics is not that poor!'))
#print(not_poor('The lyrics is poor!'))
#
#Pro.08
#def longest(word_list):
#    new_list = []
#    for i in word_list:
#        new_list.append((len(i),i))
#    new_list.sort()
#    return new_list[-1][0], new_list[-1][1]
#result = longest(['PHP','Exercise','Backend'])
#print('Longest word: ', result[1])
#print('Length of the longest word: ',result[0])

#Pro.09
#def remove_string(string,n):
#    first = string[:n]
#    last = string[n+1:]
#    return first + last
#print(remove_string('Python',0))
#print(remove_string('Python',3))
#print(remove_string('Python', 5))

#Pro.10
#def change_string(string):
#    return string[-1:] + string[1:-1] + string[:1]
#print(change_string('abcd'))
#print(change_string('12345'))

        
    
    