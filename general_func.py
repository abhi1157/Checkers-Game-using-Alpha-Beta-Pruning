'''

ABHINAV GUPTA
2015B4A70602P

'''
import sys
import time
from Initial_state import *
from copy import deepcopy
from AlphaBeta import *
from minimax import *

def oppositecol(color):

	if color == 1:
		return 2
	elif color == 2:
		return 1
	else:
		return 0

def isType2pos(lis, x, y):

	ser=gridtoseries(x,y)
	lpp=adj2[ser]

	i=0
	while (i<len(lpp)):
		lp=dicti[lpp[i]]
		i=i+2
		#print(lp[0],lp[1])
		if canMoveToPosition(lis, x, y,lp[0],lp[1]) == True:
			return True



	return False

def isType2(lis, color):

	for coin in range(1,25):
		xy = dicti[coin]
		x = xy[0]
		y = xy[1]

		if lis[x-1][y-1] == color:
			if isType2pos(lis, x, y) == True:
				return True

	return False

def doMovePosition(lis, x1, y1, x2, y2):

	isCapture = False

	lis[x2-1][y2-1] = lis[x1-1][y1-1]
	lis[x1-1][y1-1] = 0

	if (abs(x1-x2)==2 or (abs(y1-y2) == 2 and abs(x1-x2)== 0)):
		z1=gridtoseries(x1,y1)
		z2=gridtoseries(x2,y2)
		lp=adj2[z1]
		if(lp.__contains__(z2)):
			z1=lp[lp.index(z2)+1][z2]
		z=dicti[z1]
		lis[int((x1+x2)/2)-1][z[1]-1] =0
		isCapture = True



	return isCapture

def doMove(lis, move):

	xy = dicti[move[0]]
	x1 = xy[0]
	y1 = xy[1]

	for i in range(1, len(move)):
		xy = dicti[move[i]]
		x2 = xy[0]
		y2 = xy[1]

		_ = doMovePosition(lis, x1, y1, x2, y2)

		x1 = x2
		y1 = y2

def canMoveToPosition(lis, x1, y1, x2, y2):

	z1=gridtoseries(x1,y1)
	z2=gridtoseries(x2,y2)
	if(z1>24 or z1<1):
		return False
	if(z2>24 or z2<1):
		return False
	color = lis[x1-1][y1-1]
	if color == 0:
		return False
	if lis[x2-1][y2-1] != 0:
		return False
	x1_x2 = abs(x1-x2)
	y1_y2 = abs(y1-y2)
	if(x1_x2==0):
		if(y1_y2>2 or y1_y2==0):
			return False
	if(x1_x2>2):
		return False
	flag=0

	li=adj[z1]
	for i in range(len(li)):
		lp=dicti[li[i]]
		if(lp[0]==x2 and lp[1]==y2):
			flag=1

	li=adj2[z1]
	i=0
	while(i<len(li)):
		lp=dicti[li[i]]
		i=i+2
		if(lp[0]==x2 and lp[1]==y2):
			flag=1

	if(flag==0):
		return false
	if x1_x2 == 2 or (x1_x2==0 and y1_y2==2):
		z1=gridtoseries(x1,y1)
		z2=gridtoseries(x2,y2)
		lp=adj2[z1]
		if(lp.__contains__(z2)):
			z=lp[lp.index(z2)+1]

		z=dicti[z[z2]]
		if lis[int((x1+x2)/2)-1][z[1]-1]!= 2:
			return False
	return True

def isValidMove(lis, move, color):


	if len(move) < 2:
		return False;


	xy = dicti[move[0]]
	x1 = xy[0]
	y1 = xy[1]

	if lis[x1-1][y1-1]!= color:
		return False

	isCaptureMove = isType2(lis, color)


	templis = deepcopy(lis)

	for i in range(1, len(move)):
		xy =dicti[move[i]]
		x2 = xy[0]
		y2 = xy[1]

		if canMoveToPosition(templis, x1, y1, x2, y2) == False:
			return False


		if isCaptureMove != doMovePosition(templis, x1, y1, x2, y2):
			return False


		x1 = x2
		y1 = y2

	if isCaptureMove == True:
		if isType2pos(templis, x1, y1) == True:
			return False

	return True

def AnyMove(lis,color):

	for coin in range(1,25):
		xy = dicti[coin]
		x = xy[0]
		y = xy[1]


		if lis[x-1][y-1] == color:
			lp=adj[coin]
			for i in range(len(lp)):
				lpp=dicti[lp[i]]
				if canMoveToPosition(lis, x, y,lpp[0],lpp[1]) == True:
					return True

	if isType2(lis, color) == True:
		return True

	return False

def countt(lis, color):


	count = 0


	for coin in range(1, 25):
		xy = dicti[coin]
		x = xy[0]
		y = xy[1]


		if lis[x-1][y-1] == color:
			count = count + 1

	return count


def play(lis):



	currentColor = 1
	nextColor = 2
	movesRemaining = 1

	while AnyMove(lis, currentColor) == True:

		templis = deepcopy(lis)

		alphbetae = alphbeta(templis, currentColor, movesRemaining)

		doMove(lis, alphbetae)


		(currentColor, nextColor) = (nextColor, currentColor)

		print ("coins remaining:", currentColor, "=", countt(lis, currentColor))
		print (nextColor, "=", countt(lis, nextColor))


		movesRemaining = movesRemaining - 1
		if movesRemaining == 0:
			return (lis, countt(lis, 1), countt(lis, 2))

	return (lis, countt(lis, 1), countt(lis, 2))
def printB(lis):
	print(" "," ",lis[0][0]," ",lis[0][1]," ",lis[0][2]," ",lis[0][3]," ")
	print(" ",lis[1][0]," ",lis[1][1]," ",lis[1][2]," ",lis[1][3]," ",lis[1][4]," ")
	print(lis[2][0]," ",lis[2][1]," ",lis[2][2]," ",lis[2][3],"",lis[2][4]," ",lis[2][5]," ")
	print(" ",lis[3][0]," ",lis[3][1]," ",lis[3][2]," ",lis[3][3]," ",lis[3][4]," ")
	print(" "," ",lis[4][0]," ",lis[4][1]," ",lis[4][2]," ",lis[4][3]," ",)



def playminimax(lis):

	currentColor = 1
	nextColor = 2
	movesRemaining = 1

	while AnyMove(lis, currentColor) == True:

		templis = deepcopy(lis)

		minimaxe = minimax(templis, currentColor, movesRemaining)

		doMove(lis, minimaxe)


		(currentColor, nextColor) = (nextColor, currentColor)

		print ("coins remaining:", currentColor, "=", countt(lis, currentColor))
		print (nextColor, "=", countt(lis, nextColor))


		movesRemaining = movesRemaining - 1
		if movesRemaining == 0:
			return (lis, countt(lis, 1), countt(lis, 2))

	return (lis, countt(lis, 1), countt(lis, 2))
