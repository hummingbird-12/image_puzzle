import cv2
import numpy as np
import os
import sys
from pathlib import Path
from checkInput import check_input
import readImage as readImg
from makePieces import get_pieces
import drawPieces as drawP
import Piece


if __name__ == "__main__":
    check_input("unpuzzler.py")
    filename = sys.argv[1]      # filename = input("Enter image file name: ")
    fileTest = Path(filename)
    if not fileTest.is_file():
        print("Image file NOT found.")
        sys.exit(1)
    img, imgRow, imgCol, imgChn = readImg.read_image(filename, cv2.IMREAD_COLOR)

    pList, pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total = get_pieces(img, imgRow, imgCol, imgChn)

    for i in range(pCnt_total):
        for j in range(i + 1, pCnt_total):
            if i == j:
                continue
            Piece.piece_difference(pList[i], pList[j])

    startPiece = pList[0]
    for piece in pList:
        Piece.find_neighbors(piece)
        if piece.neighbors[0] == piece.neighbors[3] is None:
            startPiece = piece

    black = np.zeros((pSize_vertical, pSize_horizontal, imgChn), dtype=np.uint8)
    blackPiece = Piece.Piece(-1, pSize_vertical, pSize_horizontal, imgChn, (0, 0), black, pCnt_total)
    temp = [blackPiece for x in range(pCnt_total)]
    temp[0] = startPiece
    for i in range(pCnt_total):
        if i % pCnt_row < pCnt_row - 1 and temp[i].neighbors[1] is not None:
            temp[i + 1] = pList[temp[i].neighbors[1]]
        if i / pCnt_row < pCnt_column - 1 and temp[i].neighbors[2] is not None:
            temp[i + pCnt_row] = pList[temp[i].neighbors[2]]

    filename = os.path.splitext(filename)[0] + "_solve.png"
    temp = drawP.combine_pieces(pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total, imgChn, temp)
    drawP.draw_image(temp, filename + " - Solved Image")
    cv2.imwrite(filename, temp)
