import cv2
from random import shuffle
import os
import sys
from pathlib import Path
from checkInput import check_input
import readImage as readImg
from makePieces import get_pieces
import drawPieces as drawP


if __name__ == "__main__":
    # initialization and read image
    check_input("puzzler.py")
    filename = sys.argv[1]
    fileTest = Path(filename)
    if not fileTest.is_file():
        print("Image file NOT found.")
        sys.exit(1)
    img, imgRow, imgCol, imgChn = readImg.read_image(filename, cv2.IMREAD_COLOR)

    # get pieces from image
    pList, pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total = get_pieces(img, imgRow, imgCol, imgChn)

    # randomize pieces
    shuffle(pList)

    # show and save result image
    filename = os.path.splitext(filename)[0] + "_puzzle.png"
    temp = drawP.combine_pieces(pSize_vertical, pSize_horizontal, pCnt_row, pCnt_column, pCnt_total, imgChn, pList)
    drawP.draw_image(temp, filename + " - Puzzle Image")
    cv2.imwrite(filename, temp)
