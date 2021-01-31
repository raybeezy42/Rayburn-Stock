#!/bin/usr/python3

d = str(input("Enter stock ticker symbol: "))
p = {'AMC': '20', 'GME': '400', 'ICON': '2', 'CATB': '4', 'NVAX': '220', 'AVIR': '73', 'STRT': '53', 'SLV': '25', 'ACTC': '23', 'NNOX': '75'}
if d in p:
    print (d)
    print(p[d])
else:
    print('Ticker symbol not found')
