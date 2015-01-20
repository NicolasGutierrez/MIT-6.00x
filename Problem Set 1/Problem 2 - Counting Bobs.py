# -*- coding: utf-8 -*-
s = 'bobiudsfdsyobobobfdsaklgadvcxkd'
n = 0
count = 0
for n in range(len(s)):
    z = s[0+n:3+n]
    n += 1
    if z == 'bob':
        count += 1
print count        