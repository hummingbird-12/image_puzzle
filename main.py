import cv2
import numpy as np
import math
from random import shuffle

class Piece:
    pieceNum = -1
    pieceRow = 0
    pieceCol = 0
    pieceChn = 0
    pieceStart = (0, 0)
    pieceData = None

    def __init__(self, num, row, col, chn, start, data):
        self.pieceNum = num
        self.pieceRow = row
        self.pieceCol = col
        self.pieceChn = chn
        self.pieceStart = start
        self.pieceData = np.ndarray((row, col, chn), buffer=data, dtype=np.uint8)
        #print(len(self.pieceData), len(self.pieceData[0]), len(self.pieceData[0][0]))
        #cv2.imshow("piece{}".format(num), self.pieceData)
        #cv2.waitKey(0)


img = cv2.imread('lenna.png', cv2.IMREAD_COLOR)

imgRow = len(img)
imgCol = len(img[0])
imgChn = len(img[0][0])

# pDim = int(input("Enter size of puzzle: "))
pDim = 256
pRow = math.ceil(imgRow / pDim)
pCol = math.ceil(imgCol / pDim)
pCnt = pRow * pCol
pList = []

for pIt in range(pCnt):
    temp = np.zeros((pDim, pDim, imgChn), dtype=np.uint8)
    #print(len(temp), len(temp[0]), len(temp[0][0]))
    startRow = pDim * math.floor(pIt / pRow)
    startCol = pDim * (pIt % pCol)
    #print(startRow, startCol)
    for i in range(startRow, startRow + pDim):
        for j in range(startCol, startCol + pDim):
            temp[i - startRow][j - startCol] = img[i][j]
    pList.append(Piece(pIt, pDim, pDim, imgChn, (startRow, startCol), temp))

shuffle(pList)
for piece in pList:
    cv2.imshow("piece{}".format(piece.pieceNum), piece.pieceData)
cv2.waitKey(0)
cv2.destroyAllWindows()
