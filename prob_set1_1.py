# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:05:08 2022

@author: prdubey
"""
"""
#problem set 1
#s = input("Enter a string:")
s = "azcbobobegghakl"
count = 0
for l in s:
    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        count = count + 1
    else:
        None

print ("Number of vowels:", count)

#problem set 2
s= 'bobbob'
cnt = 0
b_arr = []
for l in s:
    if l == 'b' and len(b_arr) == 0:
        b_arr.append(l)
    elif l == 'b' and len(b_arr) == 2:
        b_arr = []
        b_arr.append(l)
        cnt = cnt + 1
    elif l == 'o' and len(b_arr) == 1:
        b_arr.append(l)
    elif l == 'b' and len(b_arr) == 1:
        b_arr[0] = l
    else:
        b_arr = []

print("Number of times bob occurs is:",cnt)
"""
#problemt set 3
s = 'abcdefghijklmnopqrstuvwxyz'
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ss_arr =[]
final_ss_arr = []
cnt = 0
for l in s:
    cnt += 1
    for al in alphabets:
        if l == al and len(ss_arr) == 0:
            ss_arr.append(l)
            p_val = alphabets.index(al)
        elif l ==  al and len(ss_arr) > 0 and  p_val <= alphabets.index(l):
            ss_arr.append(l)
            p_val = alphabets.index(al)
            if cnt == len(s) and len(ss_arr) > len(final_ss_arr):
                final_ss_arr = ss_arr
        elif l == al and len(ss_arr) > 0 and p_val > alphabets.index(l):
            p_val = alphabets.index(al)
            if len(ss_arr) > len(final_ss_arr):
                final_ss_arr = ss_arr
            ss_arr = []
            ss_arr.append(l)

print("Longest substring in alphabetical order is: ",''.join(map(str,final_ss_arr)))

            
            

    
    

        