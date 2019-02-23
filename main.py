import cv2
import numpy as np
import math
from random import shuffle
import Piece as Pc
import drawPieces as drawP


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
    # temp[:] = img[startRow:startRow + pDim, startCol:startCol + pDim]
    for i in range(startRow, startRow + pDim):
        if i >= imgRow:
            break
        for j in range(startCol, startCol + pDim):
            if j >= imgCol:
                continue
            temp[i - startRow][j - startCol] = img[i][j]
    pList.append(Pc.Piece(pIt, pDim, pDim, imgChn, (startRow, startCol), temp))

shuffle(pList)  # randomize pieces

temp = drawP.combine_pieces(pDim, pRow, pCol, pCnt, imgChn, pList)
drawP.draw_image(temp)
