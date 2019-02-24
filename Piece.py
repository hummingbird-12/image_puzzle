import numpy as np
import math


# Piece class, holds data of each piece
class Piece:
    def __init__(self, num, s_vert, s_horz, chn, start, data, total):
        self.pieceNum = num
        self.size_vertical = s_vert
        self.size_horizontal = s_horz
        self.pieceChn = chn
        self.pieceStart = start
        self.pieceData = np.ndarray((s_vert, s_horz, chn), buffer=data, dtype=np.uint8)
        self.pieceTotal = total

        mid_vert = math.floor(s_vert / 2)
        mid_horz = math.floor(s_horz / 2)

        self.pxUp = self.pieceData[0][mid_horz]
        self.pxRight = self.pieceData[mid_vert][s_horz - 1]
        self.pxDown = self.pieceData[s_vert - 1][mid_horz]
        self.pxLeft = self.pieceData[mid_vert][0]

        self.pxUpRight = self.pieceData[0][s_horz - 1]
        self.pxDownRight = self.pieceData[s_vert - 1][s_horz - 1]
        self.pxDownLeft = self.pieceData[s_vert - 1][0]
        self.pxUpLeft = self.pieceData[0][0]

        self.similarity = []
        for i in range(total):
            self.similarity.append(None)

        self.neighbors = [None for x in range(4)]


# calculate difference of pixels' each channel value
def pixel_difference(px1, px2):
    diff = 0
    for i in range(len(px1)):
        for j in range(len(px1[i])):
            diff += abs(int(px1[i][j]) - int(px2[i][j]))
    return diff


# calculate difference between pieces
def calculate_difference(piece1: Piece, piece2: Piece, index1, index2):
    vertical_12 = pixel_difference(
        (piece1.pxDownLeft, piece1.pxDown, piece1.pxDownRight),
        (piece2.pxUpLeft, piece2.pxUp, piece2.pxUpRight))
    vertical_21 = pixel_difference(
        (piece2.pxDownLeft, piece2.pxDown, piece2.pxDownRight),
        (piece1.pxUpLeft, piece1.pxUp, piece1.pxUpRight))
    horizontal_12 = pixel_difference(
        (piece1.pxUpRight, piece1.pxRight, piece1.pxDownRight),
        (piece2.pxUpLeft, piece2.pxLeft, piece2.pxDownLeft))
    horizontal_21 = pixel_difference(
        (piece2.pxUpRight, piece2.pxRight, piece2.pxDownRight),
        (piece1.pxUpLeft, piece1.pxLeft, piece1.pxDownLeft))

    temp1 = [vertical_21, horizontal_12, vertical_12, horizontal_21]
    temp2 = [vertical_12, horizontal_21, vertical_21, horizontal_12]

    for i in range(len(temp1)):
        temp1[i] = (temp1[i], i)
        temp2[i] = (temp2[i], i)

    piece1.similarity[index2] = sorted(temp1)
    piece2.similarity[index1] = sorted(temp2)


# search for neighbors
def find_neighbors(piece: Piece):
    candidates = [None for x in range(4)]
    for i in range(len(piece.similarity)):
        if piece.similarity[i] is None:
            continue
        temp = piece.similarity[i][0]
        if candidates[temp[1]] is None or candidates[temp[1]][1][0] > temp[0]:
            candidates[temp[1]] = (i, temp)

    for entry in candidates:
        if entry is not None and entry[1][0] <= 150:
            piece.neighbors[entry[1][1]] = entry[0]
