# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 13:14:10 2021

@author: Alvin Buana
"""


def answer(ok,hi):
    hi = list(map(int,hi))
    ok = list(map(int,ok))
    res = []
    health = 0
    for j in range (len(ok)):
        for i in range(len(ok[j])):
            if ok[i]+health <=0:
                if len(ok)-j == 0:
                    return health
                elif len(ok)>=1:
                    continue
            else:
               health += ok[i]
                    
            










hi = input()
hi = hi.split()
ok = []
yes = input()
ok = yes.split()
#ok.append(yes)
answer(ok,hi)