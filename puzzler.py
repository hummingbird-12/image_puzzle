import cv2
import numpy as np
import math
from random import shuffle
import readImage as readImg
import Piece as Pc
import drawPieces as drawP


# filename = input("Enter image file name: ")
filename = "lenna.png"
img, imgRow, imgCol, imgChn = readImg.read_image(filename, cv2.IMREAD_COLOR)

# piece information
pCnt_column = int(input("Pieces in a column: "))
pCnt_row = int(input("Pieces in a row: "))
pCnt_total = pCnt_row * pCnt_column
pSize_vertical = math.ceil(imgCol / pCnt_column)
pSize_horizontal = math.ceil(imgRow / pCnt_row)
pList = []

# creation of pieces
for pIt in range(pCnt_total):
    temp = np.zeros((pSize_vertical, pSize_horizontal, imgChn), dtype=np.uint8)
    startRow = pSize_vertical * math.floor(pIt / pCnt_row)
    startCol = pSize_horizontal * (pIt % pCnt_row)
    # temp[:] = img[startRow:startRow + pDim, startCol:startCol + pDim]
    for i in range(startRow, startRow + pSize_vertical):
        if i >= imgRow:
            break
        for j in range(startCol, startCol + pSize_horizontal):
            if j >= imgCol:
                continue
            temp[i - startRow][j - startCol] = img[i][j]
    pList.append(Pc.Piece(pIt, pSize_vertical, pSize_horizontal, imgChn, (startRow, startCol), temp))

shuffle(pList)  # randomize pieces

temp = drawP.combine_pieces(pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total, imgChn, pList)
drawP.draw_image(temp)
cv2.imwrite("lenna_puzzle.png", temp)
