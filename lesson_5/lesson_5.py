# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:03:12 2021

@author: sheba
"""

# %%

# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f1 = open("text1.txt", 'w')

while True:
    line = str(input('New line: '))
    if line:
        f1.write(line + '\n')
    else:
        print('End of file')
        f1.close()
        break

# %%

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f2 = open("text2.txt", "r")

lines = f2.readlines()
num_lines = len(lines)
num_words = [len(line.split()) for line in lines]
print(f"Number of lines: {num_lines}")
print(f"Number of words in each line: {num_words}")
f2.close()

# %%

# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# import codecs
f3 = open("text3.txt", "r", "utf_8_sig")
lines = f3.readlines()
empl_list = [line.split()[0] for line in lines
             if float(line.split()[1]) < 20000]
sal_list = [float(line.split()[1]) for line in lines]
f3.close()
print(f"Сотрудники: {empl_list}")
print(f"Средний доход: {round(sum(sal_list) / len(sal_list), 2)}")

# %%

# 4. Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские числительные должны
# заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

dict_num = {1: "Один",
            2: "Два",
            3: "Три",
            4: "Четыре",
            5: "Пять"}
f4_1 = open("text4_1.txt", "r")
f4_2 = open("text4_2.txt", "w")
lines_4_1 = f4_1.readlines()
lines_4_2 = [line.split() for line in lines_4_1]
for x in range(len(lines_4_2)):
    lines_4_2[x][0] = dict_num[int(lines_4_2[x][-1])]
lines_4_2 = [' '.join(line) + '\n' for line in lines_4_2]
f4_2.writelines(lines_4_2)
f4_1.close()
f4_2.close()

# %%

# 5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать сумму
# чисел в файле и выводить ее на экран.

list_5 = [1, 2.3, 4.5, 6.7]
str_list_5 = [str(i) for i in list_5]
f5 = open("text5.txt", "w")
f5.writelines(' '.join(str_list_5))
f5.close()
f5 = open("text5.txt", "r")
str_list_5_1 = f5.read()
list_5_1 = [float(i) for i in str_list_5_1.split(' ')]
print(f"Sum = {sum(list_5_1)}")

# %%

# 6. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# import codecs
import re
f6 = open("text6.txt", "r", encoding="UTF-8")
str_6 = f6.readlines()
list_names = [elem.split(':')[0] for elem in str_6]
list_hours = [list(map(lambda x: int(x), re.findall(r'\d+', elem)))
              for elem in str_6]
dict_6 = {list_names[i]: sum(list_hours[i]) for i in range(len(list_names))}
f6.close()
print(dict_6)

# %%

