'''

ABHINAV GUPTA
2015B4A70602P

'''
import time
from copy import deepcopy
from Initial_state import *
from general_func import *
from successor import *
from Terminal_test import *
def minimax(lis, color,movesRemaining):
    moves = successorf(lis, color)
    print("moveslength", len(moves))
    if len(moves) == 1:
        return moves[0]
    opcol = general_func.oppositecol(color)
    depth=9
    equalMoves = []

    best = None
    for move in moves:
        newlis = deepcopy(lis)
        general_func.doMove(newlis,move)
        moveVal = MIN_VALUE(newlis, color, depth,opcol)
        if best == None or (moveVal!=None and moveVal > best):
            bestMove = move
            best = moveVal
            equalMoves = []
            equalMoves.append(move)
        elif moveVal == best:
            equalMoves.append(move)

    if len(equalMoves) > 1:
        for move in equalMoves:
            l = len(move)
            xy = dicti[move[l-1]]
            x = xy[0]
            y = xy[1]
            xy2 = dicti[move[0]]
            x2 = xy2[0]
            y2 = xy2[1]
            li=adj[move[l-1]]
            if(abs(x2-x)==1 or (abs(x2-x)==0 and abs(y2-y)==1)):
                count=0
                for i in range(len(li)):
                    d=dicti[li[i]]
                    if(lis[d[0]-1][d[1]-1]==2):
                        count=count+1
                if(count==0):
                        return move

        for move in equalMoves:
            l = len(move)
            xy = dicti[move[l-1]]
            x = xy[0]
            y = xy[1]
            li=adj[move[l-1]]
            for i in range(len(li)):
                d=dicti[li[i]]
                if(x==1 or x==5 or (x==3 and (y==1 or y==6)) or y==1 or ((x==2 or x==4) and (y==1 or y==5))):
                    return move
    return bestMove



def MAX_VALUE(lis,color,depth,opcol):
    if depth > 1 and Terminal_test(lis)==False :
        depth -= 1
        opti = None
        moves = successorf(lis, color)
        for move in moves:
            nextlis = deepcopy(lis)
            general_func.doMove(nextlis,move)
            value = MIN_VALUE(nextlis, color, depth, opcol)
            if opti==None or (value!=None and value > opti):
                opti = value

        return opti
    else:
            utility=Utility(lis,color,opcol)
            return utility

def MIN_VALUE(lis,color,depth,opcol):
    if depth > 1 and Terminal_test(lis)==False :
        depth -= 1
        opti = None
        moves = successorf(lis, opcol)
        for move in moves:
            nextlis = deepcopy(lis)
            general_func.doMove(nextlis,move)
            value = MAX_VALUE(nextlis, color, depth,opcol)
            if opti == None or  (value!=None and value < opti):
                opti = value


        return opti
    else:
            utility=Utility(lis,color,opcol)
            return utility


def Utility(lis,color,opcol):
    value = 0
    for coin in range(1, 25):
        xy = dicti[coin]
        x = xy[0]
        y = xy[1]
        if lis[x-1][y-1] == color:
            value += 2
        elif lis[x-1][y-1] == opcol:
            value -= 2

    return value
