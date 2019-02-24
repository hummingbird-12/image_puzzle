import cv2
import os
import sys
from pathlib import Path
import readImage as readImg
from makePieces import get_pieces
import drawPieces as drawP
import Piece


if __name__ == "__main__":
    filename = input("Enter image file name: ")
    fileTest = Path(filename)
    if not fileTest.is_file():
        print("Image file NOT found.")
        sys.exit(1)
    img, imgRow, imgCol, imgChn = readImg.read_image(filename, cv2.IMREAD_COLOR)

    pList, pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total = get_pieces(img, imgRow, imgCol, imgChn)

    for i in range(pCnt_total):
        for j in range(i + 1, pCnt_total):
            Piece.calculate_difference(pList[i], pList[j], i, j)

    startPiece = pList[0]
    for piece in pList:
        Piece.find_neighbors(piece)
        if piece.neighbors[0] == piece.neighbors[3] is None:
            startPiece = piece

    temp = [startPiece for x in range(pCnt_total)]
    for i in range(pCnt_total):
        if i % pCnt_row < pCnt_row - 1:
            temp[i + 1] = pList[temp[i].neighbors[1]]
        if i / pCnt_row < pCnt_column - 1:
            temp[i + pCnt_row] = pList[temp[i].neighbors[2]]

    filename = os.path.splitext(filename)[0] + "_solve.png"
    temp = drawP.combine_pieces(pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total, imgChn, temp)
    drawP.draw_image(temp, filename + " - Solved Image")
    cv2.imwrite(filename, temp)
