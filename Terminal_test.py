'''

ABHINAV GUPTA
2015B4A70602P

'''
from copy import deepcopy
from Initial_state import *
from general_func import *
from successor import *
terminal_states=dict()
def max_col(i):
    if(i==0 or i==4):
        return 4
    if(i==1 or i==3):
        return 5
    if(i==2):
        return 6

def hash_state(lis):
    str1=""
    for i in range(5):
        col=max_col(i)
        for j in range(col):
            str1=str1+""+str(lis[i][j])
    return str1

def Terminal_test(lis):
    str1=hash_state(lis)
    if str1 in terminal_states:
        return True
    count1=general_func.countt(lis,1)
    count2=general_func.countt(lis,2)
    if count1==0 or count2==0:
        terminal_states[str1]=lis
        return True
    x1=successorf(lis,1)
    #x2=successorf(lis,2)
    '''if len(x1)==0 and len(x2)==0:
        terminal_states[str1] = lis
        return True'''
    if len(x1)==0:
        terminal_states[str1] = lis
        return True
    return False
