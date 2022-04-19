# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:24:04 2022

@author: prdubey
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    def countOfEleInList(L):
        L_dict = {}
        L_copy = list(set(L[:]))
        for char in L_copy:
            L_dict[char] = L.count(char)
        return L_dict
        
    L1_dict = {}
    L2_dict = {}
    #Base case : empty lists
    if L1 == [] and L2 == []:
        return (None, None, None)
    #Non permutable
    elif not (len(L1) == len(L2)):
        return False
    #Permutable
    else:
        L1_dict = countOfEleInList(L1)
        L2_dict = countOfEleInList(L2)
        if L1_dict == L2_dict:
            L1_keys = L1_dict.keys()
            L1_max_val = max(L1_dict.values())
            for keys in L1_keys:
                if L1_dict[keys] == L1_max_val:
                    Max_key = keys
            return (Max_key, L1_max_val, type(Max_key))
        else:
            return False
            
            
L1 = [1,2,4]
L2 = [1,3,2]
print(is_list_permutation(L1, L2))
        