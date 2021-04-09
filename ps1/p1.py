# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 20:18:02 2021

@author: Jonas
"""
s = 'ppzyia'
vowels = ["a", "e", "i", "o", "u"]
count = 0


for char in list(s):
    if char in vowels:
        count += 1

# print(f"Number of vowels: {count}") no f strings allowed :(
print("Number of vowels: " + str(count))

# problem2

s = list(s)
# count = s.count("bob") apparently they want it to count multiples
count_2 = 0

for item in range(len(s)):
    if "".join(s[item:item + 3]) == "bob":
        count_2 += 1


print("Number of times bob occurs is: " + str(count_2))


# problem 3
abc = "abcdefghijklmnopqrstuvwxyz"
# abc = list(abc)
s = "abcbcd"
cur = lng = s[0]
for c in s[1:] + ' ':
    if c < cur[-1]:
        if len(cur) > len(lng):
            lng = cur
        cur = ''
    cur += c

print('Longest substring in alphabetical order is:', lng)
