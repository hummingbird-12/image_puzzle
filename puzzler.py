import cv2
from random import shuffle
import readImage as readImg
from makePieces import get_pieces
import drawPieces as drawP


if __name__ == "__main__":
    # filename = input("Enter image file name: ")
    filename = "lenna.png"
    img, imgRow, imgCol, imgChn = readImg.read_image(filename, cv2.IMREAD_COLOR)

    pList, pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total = get_pieces(img, imgRow, imgCol, imgChn)

    shuffle(pList)  # randomize pieces

    temp = drawP.combine_pieces(pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total, imgChn, pList)
    drawP.draw_image(temp)
    cv2.imwrite("lenna_puzzle.png", temp)
