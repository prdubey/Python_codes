# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 14:55:59 2022

@author: prdubey
"""

#Monthly payment by bisection method

balance = 334181
annualInterestRate = 0.2
month = 0
mplb = round(balance/12,2)
mpub = round((balance * (1+annualInterestRate/12)**12)/12,2)
mpc = round((mplb + mpub)/2,2)
og_balance = balance
smallest_bal = 0.01
cnt = 0
while (month <=12 and not(balance == 0)):
    cnt = cnt + 1
    if not(balance == 0) and month < 12:
        balance = float(round(balance - mpc,2))
        updated_balance = float(round(balance + (annualInterestRate/12.0) * balance,2))
        balance = updated_balance
        smallest_bal = balance
        #print(balance)
        month +=1
    elif balance > 0.3 and month == 12:
        mplb = mpc
        mpc = round((mplb + mpub)/2,2)
        balance = og_balance
        month = 0
        #print("GB:",mpc,mpub)
    elif balance < -0.3 and month == 12:
        mpub = mpc
        mpc = round((mplb + mpub)/2,2)
        balance = og_balance
        month = 0
        #print("LB:",mplb,mpc)
    else:
        balance = 0
print(cnt)  
print("Lowest Payment: ",mpc)