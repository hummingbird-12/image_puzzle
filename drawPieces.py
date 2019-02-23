import cv2
import numpy as np
import math


def combine_pieces(pdim, prow, pcol, pcnt, imgchn, plist):
    # get pieces together in a single image
    temp = np.zeros((pdim * prow, pdim * pcol, imgchn), dtype=np.uint8)
    for pIt in range(pcnt):
        start_row = pdim * math.floor(pIt / prow)
        start_col = pdim * (pIt % pcol)
        temp[start_row:start_row + pdim, start_col:start_col + pdim] = plist[pIt].pieceData[:pdim, :pdim]
    return temp


def draw_image(temp):
    # show result puzzle image
    cv2.imshow("Puzzle Image", temp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
