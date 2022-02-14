# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 10:03:15 2019

@author: prdubey
"""
def display(list1):
    print(f"                                ")
    print(f" {list1[0]}   |  {list1[1]} |  {list1[2]} ")
    print(f" ------------------")
    print(f" {list1[3]}   |  {list1[4]} |  {list1[5]} ")
    print(f" ------------------")
    print(f" {list1[6]}   |  {list1[7]} |  {list1[8]} ")
    
 
def usr_loc_check(loc,list1):
    if int(loc) > 8:
        print('Location out of bounds. It should be less than 9 and greater than or equal to 0')
        return False
    else:
        str1 = list1[int(loc)]
        if str1 == 'X' or  str1 == 'O':
            print('Location already occupied.')
            return False
        else:
            return True
 
#Input collison for users               
def usr_inp_check(usr1,usr2):
    return usr1 == usr2

def win_check(list1,usr_sel,start,end,incr):
    count = 0
    for i in range(int(start),int(end),int(incr)):
        if list1[i] == usr_sel:
            count += 1
        else:
            pass
    return count == 3

def final_winner(list1,usr_sel):
        if win_check(list1,usr_sel,0,3,1):
            return True
        elif win_check(list1,usr_sel,3,6,1):
            return True
        elif win_check(list1,usr_sel,6,9,1):
            return True
        elif win_check(list1,usr_sel,0,9,4):
            return True
        elif win_check(list1,usr_sel,1,8,3):
            return True
        elif win_check(list1,usr_sel,2,9,3):
            return True
        elif win_check(list1,usr_sel,2,7,2):
            return True
        elif win_check(list1,usr_sel,0,7,3):
            return True
        else:
            return False

def play_again(play_again):
    return play_again == 'True'

list1 =[0,1,2,3,4,5,6,7,8]
display(list1)
usr2_sel = ''
loc_count = 0
play = True
while play:

    usr1_inp = input("Usr1 Input: ")
    while True:
        if usr_inp_check(usr1_inp,usr2_sel):
            print('Enter different input')
            usr1_inp = input("Enter again Usr1:")
        else:
            usr1_sel = usr1_inp
            break
    usr1_loc = input("Enter location: ")
    while True:
        if usr_loc_check(usr1_loc,list1) == False:
            usr1_loc = input("Enter location again: ")
        else:
            list1[int(usr1_loc)] = usr1_inp
            display(list1)
            loc_count += 1
            print(loc_count)
            break
    
    if loc_count < 9:
        usr2_inp = input("Usr2 Input: ")
        while True:
            if usr_inp_check(usr2_inp,usr1_sel):
                print('Enter different input')
                usr2_inp = input("Enter again Usr2:")
            else:
                usr2_sel = usr2_inp
            break
        usr2_loc = input("Enter location: ")
        while True:
            if loc_count < 9:
                if usr_loc_check(usr2_loc,list1) == False:
                    usr2_loc = input("Enter location again: ")
                else:
                    list1[int(usr2_loc)] = usr2_inp
                    display(list1)
                    loc_count += 1
                    print(loc_count)
                    break
        else:
            pass
        

    if loc_count <= 9:
        if final_winner(list1,usr1_sel):
            print("Winner is USR1")
            playagain = input("For Playing again enter 'True':")
            #break
        elif final_winner(list1,usr2_sel):
            print("Winner is USR2")
            playagain = input("For Playing again enter 'True':")
            #break
        else:
            if loc_count == 9:
                print("TIE!!!")
                playagain = input("For Playing again enter 'True':")
            else:
                pass
    else:
        play = play_again(playagain)

else:
    print("Play Stopped")


    
    
     

