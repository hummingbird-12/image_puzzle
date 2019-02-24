import numpy as np
import math
import sys
from Piece import Piece


def get_pieces(img, img_row, img_col, img_chn):
    # piece information
    cnt_column = int(sys.argv[2])   # cnt_column = int(input("Pieces in a column: "))
    cnt_row = int(sys.argv[3])      # cnt_row = int(input("Pieces in a row: "))
    cnt_total = cnt_row * cnt_column
    size_horizontal = math.ceil(img_col / cnt_row)
    size_vertical = math.ceil(img_row / cnt_column)
    p_list = []

    # creation of pieces
    for pIt in range(cnt_total):
        temp = np.zeros((size_vertical, size_horizontal, img_chn), dtype=np.uint8)
        start_row = size_vertical * math.floor(pIt / cnt_row)
        start_col = size_horizontal * (pIt % cnt_row)
        for i in range(start_row, start_row + size_vertical):
            if i >= img_row:
                break
            for j in range(start_col, start_col + size_horizontal):
                if j >= img_col:
                    continue
                temp[i - start_row][j - start_col] = img[i][j]
        p_list.append(Piece(pIt, size_vertical, size_horizontal, img_chn, (start_row, start_col), temp, cnt_total))
    return p_list, size_vertical, size_horizontal, cnt_row, cnt_column, cnt_total
