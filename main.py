'''

ABHINAV GUPTA
2015B4A70602P

'''
import math
import time
from Initial_state import *
from general_func import *
from Terminal_test import *
from minimax import *

'''

EACH STATE IS DENOTED BY ARRAYOFARRAYLIST HERE AI'S COLOR IS DENOTED BY 1 AND HUMAN'S COLOR IS DENOTED BY 2 YOU CAN PERFORM MOVES BY JUST ENTERING THE RIGHT GRID LOCATION OFSOURCE AND DESTINATION

BUT PLEASE CHECK THAT MOVE YOU ARE ENTERING IS RIGHT MOVE JUST MENTION SOURCE AND DESTINATION- TYPE 1 OR TYPE 2 WILL BE DECIDED AUTOMATICALLY SO NO NEED TO MENTION THAT
SAMPLE (IMPORTANT)
****    enter your move 3 4 3 3
****    will move '2'(your color) from 3rd row and 4th coloumn to 3rd row and 3rd coloumn
****    starting from 1
It will ask at every move that whether you want to end the game or not -Ans NO if you want to continue

if you will leave the game in between then there is no gurantee that AI will win**
I have taken depth of minimax to be 10 for speed purposes instead of complete output


*In sample test case it will just show some output enter 1 when asked to sample testcase
*if you want to play actual game using  alpha beta enter 2 when asked
*if you want to play actual game using  minimax enter 3 when asked


I have used some heuristic like if capture move is possible do that move and some other also you can see that in AlphaBeta,py  inside equalMoves
this way I can make alpha beta to work for depth=8 instead of 5 and yet it is very fast
'''
print("your color is denoted by  2 so you can move only 2 to different position")
t=int(input("Please enter integer from 1 to 3 ----1 is for sample test case and 2 is for alphabbeta and 3 is for minimax"))
start = time.clock()
if(t==1):
    print("initial state")
    lis=[[1,1,0,2],[2,1,0,0,2],[1,1,2,1,2,1],[2,1,2,2,0],[1,2,1,2]]
    printB(lis)
    print("start")
    print("------------------")
    print("player1")
    printB(general_func.play(lis)[0])
    print("------------------")
    lis=[[1,1,0,2],[2,1,1,2,2],[1,1,0,0,2,1],[2,0,0,2,0],[1,2,1,2]]
    print("player2")
    print ("coins remaining:", "2", "=", countt(lis, 2))
    print ("1", "=", countt(lis,1))
    printB(lis)
    print("------------------")
    print("player1")
    printB(general_func.play(lis)[0])
    print("------------------")
    lis=[[1,1,0,2],[2,1,1,2,2],[1,1,0,1,0,0],[0,2,0,2,0],[1,2,1,2]]
    print("player2")
    print ("coins remaining:", "2", "=", countt(lis, 2))
    print ("1", "=", countt(lis,1))
    printB(lis)
    print("------------------")
    print("player1")
    printB(general_func.play(lis)[0])
    print("------------------")
    lis=[[1,1,0,2],[2,1,1,2,0],[1,1,1,1,0,2],[0,0,0,2,0],[0,2,1,2]]
    print("player2")
    print ("coins remaining:", "2", "=", countt(lis, 2))
    print ("1", "=", countt(lis,1))
    printB(lis)
    print("------------------")
    print("player1")
    printB(general_func.play(lis)[0])
    print("------------------")
    lis=[[1,1,0,2],[2,1,2,0,1],[1,1,1,0,0,2],[0,0,0,0,0],[0,2,1,2]]
    print("player2")
    print ("coins remaining:", "2", "=", countt(lis, 2))
    print ("1", "=", countt(lis,1))
    printB(lis)
    print("------------------")
    print("player1")
    printB(general_func.play(lis)[0])
    print("------------------")
    lis=[[1,1,0,2],[2,0,0,1,1],[1,1,1,0,0,2],[0,0,0,0,2],[0,2,1,0]]
    print("player2")
    print ("coins remaining:", "2", "=", countt(lis, 2))
    print ("1", "=", countt(lis,1))
    printB(lis)
    print("------------------")
    print("player1")
    printB(general_func.play(lis)[0])
    print("------------------")





if(t==2):
    print("initial state")
    lis=initial_state_generator()
    #lis=[[1,2,2,1],[1,2,1,2,2],[1,2,2,1,0,1],[1,1,2,0,1],[2,0,0,2]]
    printB(lis)
    while(True):
        print("------------------")
        option=input("do you want to end game yes or no")
        if(option=="yes" or Terminal_test(lis)==True):
            print("end result")
            print ("coins remaining:", "2", "=", countt(lis, 2))
            print ("1", "=", countt(lis,1))

            if(countt(lis, 2)<=countt(lis,1)):
                print("player (AI) Wins")
                break
            else:
                print("player (human) Wins")
                break
        print("player human(color=2)")
        option=input("enter your move")
        li=option.split()
        doMovePosition(lis, int(li[0]), int(li[1]), int(li[2]), int(li[3]))
        print ("coins remaining:", "2", "=", countt(lis, 2))
        print ("1", "=", countt(lis,1))
        printB(lis)
        print("------------------")

        if(countt(lis, 2)==0):
            print("player (AI) wins")
            break
        if(countt(lis,1)==0):
            print("player (Human) wins")
            break
        print("player AI(color=1)")
        printB(general_func.play(lis)[0])
        if(countt(lis, 2)==0):
            print("player (AI) wins")
            break
        if(countt(lis,1)==0):
            print("player (Human) wins")
            break


if(t==3):
    print("initial state")
    lis=initial_state_generator()
    #lis=[[1,2,2,1],[1,2,1,2,2],[1,2,2,1,0,1],[1,1,2,0,1],[2,0,0,2]]
    printB(lis)
    while(True):
        print("------------------")
        option=input("do you want to end game yes or no")
        if(option=="yes" or Terminal_test(lis)==True):
            print("end result")
            print ("coins remaining:", "2", "=", countt(lis, 2))
            print ("1", "=", countt(lis,1))

            if(countt(lis, 2)<=countt(lis,1)):
                print("player (AI) Wins")
                break
            else:
                print("player (human) Wins")
                break
        print("player human(color=2)")
        option=input("enter your move")
        li=option.split()
        doMovePosition(lis, int(li[0]), int(li[1]), int(li[2]), int(li[3]))
        print ("coins remaining:", "2", "=", countt(lis, 2))
        print ("1", "=", countt(lis,1))
        printB(lis)
        print("------------------")

        if(countt(lis, 2)==0):
            print("player (AI) wins")
            break
        if(countt(lis,1)==0):
            print("player (Human) wins")
            break
        print("player AI(color=1)")
        printB(general_func.playminimax(lis)[0])
        if(countt(lis, 2)==0):
            print("player (AI) wins")
            break
        if(countt(lis,1)==0):
            print("player (Human) wins")
            break
totaltime = time.clock() - start
print("total time =",totaltime)
#print("no of nodes generated = ",count)
print("memory allocated to one node = space used by list of list representation = ",576," bytes")
#print("nodes generated per micro second not taking into time taken by human = ",nodesgen/totaltime)

#*------------------END----------------------*
