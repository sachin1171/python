# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:11:01 2021

@author: usach
"""


a = [12,12.3,"sachin",3 + 4j,True]
b = [34,34.4,"likith",3 + 5j,False]
e = [1,2,3]
c= a+b+e
c
#b.	
import collections
print("Original List : ",c)
ctr = collections.Counter(c)
print("Frequency of the elements in the List : ",ctr)
#c.	
c.reverse()
c





a ={1,2,3,4,5,6,7,8,9,10}
b ={5,6,7,8,9,10,11,12,13,14,15}
a
b
print(set(a).intersection(b))
print(a|b)
a.remove(7)
a
b.remove(11)
b



covid_cases = {"goa":23,"kerala":2222,"ap":2345,"ts":345,"delhi":2334}
covid_cases
covid_cases.keys()
covid_cases['america']=65
covid_cases
