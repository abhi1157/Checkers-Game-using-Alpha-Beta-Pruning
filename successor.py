'''

ABHINAV GUPTA
2015B4A70602P

'''
from copy import deepcopy
from Initial_state import *
from general_func import *
from AlphaBeta import *

def allcapturemovespos(lis, x, y):
	moves = []
	serial = gridtoseries(x, y)
	lpp=adj2[serial]
	i=0
	while(i<len(lpp)):
		lp=dicti[lpp[i]]
		i=i+2
		if general_func.canMoveToPosition(lis, x, y,lp[0],lp[1]):
			templis = deepcopy(lis)
			general_func.doMovePosition(templis, x, y,lp[0],lp[1])
			childJumpMoves = 0
			if childJumpMoves == 0:
				moves.append([serial, gridtoseries(lp[0],lp[1])])
			else:
				for m in childJumpMoves:
					l = [serial]
					l.extend(m)
					moves.append(l)
	return moves

def allmovespos(lis, x, y):
	moves = []
	isCapture = False
	l = allcapturemovespos(lis, x, y)
	for m in l:
		moves.append(m)

	if len(moves) == 0:

		serial = gridtoseries(x,y)

		lp=adj[serial]
		for i in range(len(lp)):
			lpp=dicti[lp[i]]
			if general_func.canMoveToPosition(lis,x,y,lpp[0],lpp[1]) == True:
				moves.append([serial,gridtoseries(lpp[0],lpp[1])])
	else:
		isCapture = True

	return moves, isCapture


def successorf(lis, color):

	moves = []
	isType2 = general_func.isType2(lis, color)
	for piece in range(1,25):
		xy = dicti[piece]
		x = xy[0]
		y = xy[1]

		if lis[x-1][y-1] == color:

			l, isCapture = allmovespos(lis, x, y)

			if isType2 == isCapture:
				for m in l:
					moves.append(m)
	return moves
