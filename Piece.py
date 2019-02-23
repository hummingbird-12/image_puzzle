import numpy as np


# Piece class, holds data of each piece
class Piece:
    def __init__(self, num, row, col, chn, start, data):
        self.pieceNum = num
        self.pieceRow = row
        self.pieceCol = col
        self.pieceChn = chn
        self.pieceStart = start
        self.pieceData = np.ndarray((row, col, chn), buffer=data, dtype=np.uint8)
