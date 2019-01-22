'''

ABHINAV GUPTA
2015B4A70602P

'''
import math
import time
import random
## dictinary
dicti={}
for i in range(1,5):
    dicti[i]=[1,i]
for i in range(1,6):
    dicti[i+4]=[2,i]
for i in range(1,7):
    dicti[i+9]=[3,i]
for i in range(1,6):
    dicti[i+15]=[4,i]
for i in range(1,5):
    dicti[i+20]=[5,i]
# dictionary end
#adjacency list
adj={}
adj[1]=[2,5,6]
adj[2]=[1,3,6,7]
adj[3]=[2,4,7,8]
adj[4]=[3,8,9]
adj[5]=[1,6,10,11]
k=0
for i in range(6,9):
    adj[i]=[1+k,2+k,i-1,i+1,11+k,12+k]
    k=k+1
adj[9]=[4,8,14,15]
adj[10]=[5,11,15]
k=0
for i in range(11,15):
    adj[i]=[5+k,6+k,i-1,i+1,16+k,17+k]
    k=k+1
adj[15]=[9,14,20]
adj[16]=[10,11,17,21]
k=0
for i in range(17,20):
    adj[i]=[11+k,12+k,i-1,i+1,21+k,22+k]
    k=k+1
adj[20]=[14,15,19,24]
adj[21]=[16,17,21]
adj[22]=[17,18,20,22]
adj[23]=[18,19,21,23]
adj[24]=[19,20,22]
# adjfor2
adj2={}
adj2[1]=[10,{10:5},12,{12:6},3,{3:2}]
adj2[2]=[4,{4:3},11,{11:6},13,{13:7}]
adj2[3]=[1,{1:2},12,{12:7},14,{14:8}]
adj2[4]=[2,{2:3},13,{13:8},15,{15:9}]
adj2[5]=[7,{7:6},17,{17:11}]
adj2[6]=[8,{8:7},18,{18:12},16,{16:11}]
adj2[7]=[5,{5:6},9,{9:8},17,{17:12},19,{19:13}]
adj2[8]=[6,{6:7},18,{18:13},20,{20:14}]
adj2[9]=[7,{7:8},19,{19:14}]
adj2[10]=[1,{1:5},21,{21:16},12,{12:11}]
adj2[11]=[13,{13:12},2,{2:6},22,{22:17}]
adj2[12]=[10,{10:11},14,{14:13},1,{1:6},21,{21:17},3,{3:7},23,{23:18}]
adj2[13]=[2,{2:7},4,{4:8},11,{11:12},15,{15:14},22,{22:18},24,{24:19}]
adj2[14]=[12,{12:13},3,{3:8},23,{23:19}]
adj2[15]=[13,{13:14},4,{4:9},24,{24:20}]
adj2[16]=[18,{18:17},6,{6:11}]
adj2[17]=[19,{19:18},5,{5:11},7,{7:12}]
adj2[18]=[16,{16:17},20,{20:19},6,{6:12},8,{8:13}]
adj2[19]=[17,{17:18},7,{7:13},9,{9:14}]
adj2[20]=[18,{18:19},8,{8:14}]
adj2[21]=[23,{23:22},10,{10:16},12,{12:17}]
adj2[22]=[24,{24:23},11,{11:17},13,{13:18}]
adj2[23]=[21,{21:22},12,{12:18},14,{14:19}]
adj2[24]=[22,{22:23},13,{13:19},15,{15:20}]

def gridtoseries(x,y):
    if(x==1):
        return y
    if(x==2):
        return y+4
    if(x==3):
        return y+9
    if(x==4):
        return y+15
    if(x==5):
        return y+20


def randm(player,listt):
    global dicti
    global listb
    while(True):
        ran_no=random.randint(1,24)
        li=dicti[ran_no]
        if(listt[li[0]-1][li[1]-1]==0):
            listt[li[0]-1][li[1]-1]=player
            break

def initial_state_generator():
    listt=[[0,0,0,0],[0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0],[0,0,0,0]]
    global dicti
    global listb
    for i in range(0,10):
        randm(1,listt)
    for i in range(0,10):
        randm(2,listt)

    return listt
