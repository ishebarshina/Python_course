# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:01:35 2021

@author: carmine
"""

# 6. Реализовать два небольших скрипта:

# а) итератор, генерирующий целые числа, начиная с указанного

from itertools import count


x = int(input("Enter start number: "))

for i in count(x):
    if i > 10:
        break
    else:
        print(i)
