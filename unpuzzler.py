import cv2
from random import shuffle
import readImage as readImg
from makePieces import get_pieces
import drawPieces as drawP
import Piece


if __name__ == "__main__":
    # filename = input("Enter image file name: ")
    filename = "lenna.png"
    img, imgRow, imgCol, imgChn = readImg.read_image(filename, cv2.IMREAD_COLOR)

    pList, pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total = get_pieces(img, imgRow, imgCol, imgChn)

    for i in range(pCnt_total):
        for j in range(i + 1, pCnt_total):
            Piece.calculate_difference(pList[i], pList[j], i, j)



    temp = drawP.combine_pieces(pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total, imgChn, pList)
    drawP.draw_image(temp)
    cv2.imwrite("lenna_puzzle.png", temp)
