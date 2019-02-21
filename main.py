import cv2
import numpy as np
import math
from random import shuffle


# Piece class, holds data of each piece
class Piece:
    def __init__(self, num, row, col, chn, start, data):
        self.pieceNum = num
        self.pieceRow = row
        self.pieceCol = col
        self.pieceChn = chn
        self.pieceStart = start
        self.pieceData = np.ndarray((row, col, chn), buffer=data, dtype=np.uint8)


# image information
img = cv2.imread('lenna.png', cv2.IMREAD_COLOR)
imgRow = len(img)
imgCol = len(img[0])
imgChn = len(img[0][0])

# piece information
pDim = int(input("Enter size of puzzle: "))
pRow = math.ceil(imgRow / pDim)
pCol = math.ceil(imgCol / pDim)
pCnt = pRow * pCol
pList = []

# creation of pieces
for pIt in range(pCnt):
    temp = np.zeros((pDim, pDim, imgChn), dtype=np.uint8)
    startRow = pDim * math.floor(pIt / pRow)
    startCol = pDim * (pIt % pCol)
    for i in range(startRow, startRow + pDim):
        if i >= imgRow:
            break
        for j in range(startCol, startCol + pDim):
            if j >= imgCol:
                continue
            temp[i - startRow][j - startCol] = img[i][j]
    pList.append(Piece(pIt, pDim, pDim, imgChn, (startRow, startCol), temp))

shuffle(pList)  # randomize pieces

# get pieces together in a single image
temp = np.zeros((pDim * pRow, pDim * pCol, imgChn), dtype=np.uint8)
for pIt in range(pCnt):
    startRow = pDim * math.floor(pIt / pRow)
    startCol = pDim * (pIt % pCol)
    for i in range(startRow, startRow + pDim):
        for j in range(startCol, startCol + pDim):
            temp[i][j] = pList[pIt].pieceData[i - startRow][j - startCol]

# show result puzzle image
cv2.imshow("Puzzle Image", temp)
cv2.waitKey(0)
cv2.destroyAllWindows()
