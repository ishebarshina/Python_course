# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:01:35 2021

@author: carmine
"""

# 6. Реализовать два небольших скрипта:

# б) итератор, повторяющий элементы некоторого списка, определенного заранее

from itertools import cycle

ini_list = [4, 3, 4, 5, 6, 7, 1, 2]
i = 0
for el in cycle(ini_list):
    if i > 10:
        break
    print(el)
    i += 1
