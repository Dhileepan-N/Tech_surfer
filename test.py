import re
from datetime import datetime
def func():
    acnt = 'AL ARAM USED CARS EXHB'
    chq = 'Al Aram Used Cars EXHB.'
    dict_idx = {}
    spc_char_list = ['-','.', ',', '/']
    acnt_list = list(acnt)
    chq_list = list(chq)
    e = ['a','b', ' ','c','l']
    for s in spc_char_list:
        for idx,val in enumerate(acnt_list):
            if s == val:
                dict_idx.update({idx : val})
                print(dict_idx)
    c = datetime.now()
    print(acnt_list)
    for a in dict_idx.keys():
        chq_list.insert(a , dict_idx.get(a))
    print(chq_list)
func()