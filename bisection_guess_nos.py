# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 17:11:41 2022

@author: prdubey
"""

#bisection method

print("Please think of a number between 0 and 100!")

print("Is your secret number 50?")
usr_ans = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
while not(usr_ans == 'h' or usr_ans == 'l' or usr_ans == 'c'):
    print(("Sorry, I did not understand your input"))
    print("Is your secret number 50?")
    usr_ans = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    
    
med = 50
usr_num = 0
min_num = 0
max_num = 100
tag = ''
prev_med = 0
while not(usr_ans == 'c'):
    if usr_ans == 'h':
        if tag == 'l':
            max_num = med
            min_num = prev_med
            prev_med = med 
            med = (min_num + max_num)//2
        else:
            prev_med = med
            med = (min_num + med)//2
            max_num = med
        print("Is your secret number",med, "?")
        usr_ans = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
        while not(usr_ans == 'h' or usr_ans == 'l' or usr_ans == 'c'):
            print(("Sorry, I did not understand your input"))
            print("Is your secret number", med, "?")
            usr_ans = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))

        usr_num = med 
        tag = 'h'
    elif usr_ans == 'l':
        if tag == 'h':
            min_num = med
            max_num = prev_med
            prev_med = med 
            med = (min_num + max_num)//2
        else:
            prev_med = med
            med = (med + max_num)//2
            min_num = med
        print("Is your secret number",med, "?")
        usr_ans = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
        while not(usr_ans == 'h' or usr_ans == 'l' or usr_ans == 'c'):
            print(("Sorry, I did not understand your input"))
            print("Is your secret number", med, "?")
            usr_ans = (input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
        
        usr_num = med
        tag = 'l'
    else:
        usr_num = med 
        
usr_num = med

print("Game over. Your secret number was:", usr_num)
    
    