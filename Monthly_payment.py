# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 11:14:12 2022

@author: prdubey
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 0
updated_balance = 0
while (month <= 12):
    #print(month,updated_balance)
    if month == 12:
        print("Remaining balance: ",updated_balance)
        break
    else:
        balance = float(round(balance - balance * monthlyPaymentRate,2))
        updated_balance = float(round(balance + (annualInterestRate/12.0) * balance,2))
        balance = updated_balance
        #print(balance)
        month +=1

month = 0
balance = 334181
minmonbal = 0
o_balance = balance
cnt = 0
if balance % 12 > 0 :
    minmonbal = balance // 12
    minmonbal = ((minmonbal // 10) * 10 + 10)
while (month <= 12 and balance > 0):
    #print(month,minmonbal,balance)
    cnt = cnt + 1
    if balance > 0 and month < 12:
        balance = float(round(balance - minmonbal,2))
        updated_balance = float(round(balance + (annualInterestRate/12.0) * balance,2))
        balance = updated_balance
        #print(balance)
        month +=1
    else:
        #print(month,minmonbal,balance)
        month = 0
        minmonbal = minmonbal + 10
        balance = o_balance
print("Lowest Payment: ", minmonbal)
print(cnt)
        