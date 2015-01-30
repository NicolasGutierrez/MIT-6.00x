# -*- coding: utf-8 -*-
'''
The goal of this code is to return the number of times 'bob' appears in a given string
'''
s = raw_input("Enter a string: ")
count = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        count += 1    
print count        