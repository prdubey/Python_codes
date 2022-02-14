# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 14:52:34 2022

@author: prdubey
"""

#Find binary value

dec_nos = 9863
rem = 0
qot = 0
bin_nos = []
while not(dec_nos == 0):
    qot = dec_nos // 2
    rem = dec_nos % 2
    bin_nos.append(rem)
    dec_nos = qot

#print(''.join(map(str,bin_nos[::-1])))

#Find fractional binary value
whl_nos = 0
frac_nos = 0.8967
delta = 0.01
cnt = 0
del_whl = frac_nos
diff = 1
while not(abs(diff) < delta) and cnt < 20:
    whl_nos =  del_whl * 2
    #print("delta_whl:", del_whl)
    cnt +=1
    #diff = whl_nos - del_whl
    del_whl = whl_nos
    #print("Diff is:",diff)
    splt_nos = str(del_whl).split('.')
    splt_nos = splt_nos[0]
    splt_nos = int(splt_nos)
    #splt_nos = int(splt_nos)
    splt_nos = 1 -(del_whl - splt_nos)
    print(del_whl)
    if splt_nos < 0.01:
        print(splt_nos)
        print(del_whl)
    #print(whl_nos)
print(cnt)
del_whl = str(del_whl).split('.')
del_whl = int(del_whl[0])
del_whl = del_whl + 1    
#splt_frac = str(frac_nos).split('.')
#whl_nos = splt_frac[1]
#whl_nos = int(whl_nos) * 2**len(whl_nos)
#print(whl_nos)
dec_nos = del_whl
while not(dec_nos == 0):
    qot = dec_nos // 2
    #if qot > 0:
    #    cnt +=1 
    rem = dec_nos % 2
    bin_nos.append(rem)
    dec_nos = qot
#print(cnt)
bin_out = (''.join(map(str,bin_nos[::-1])))
bin_out = '0.' + bin_out[0:(cnt)]
print(bin_out)