# Image Puzzle Maker and Solver
_______________________________


## Description
Makes puzzle from an image and tries to solve it using OpenCV and numpy data types.
* puzzle.py: converts given images into puzzle of given dimension of pieces
* unpuzzle.py: solves given puzzle image consisting of given dimension of pieces

## Requirements
* Python3
* OpenCV
* numpy

## Instructions

### Puzzling Image
```bash
[usage]:      python3 puzzler.py file_name pieces_vertically pieces_horizontally
[example]:  $ python3 puzzler.py lenna.png 4 3
```
*puzzler.py* will make a puzzle of dimension ***pieces_vertically* X *pieces_horizontally*** from given ***file_name***.
Result image is stored as ***filename*_puzzle.png**. 

The example command will create a 4 X 3 pieces puzzle of *lenna.png*.

### Unpuzzling Image
```bash
[usage]:      python3 unpuzzler.py file_name pieces_vertically pieces_horizontally
[example]:  $ python3 unpuzzler.py lenna_puzzle.png 4 3
```
*unpuzzler.py* will solve a puzzle of dimension ***pieces_vertically* X *pieces_horizontally*** from given ***file_name***.
Result image is stored as ***filename*_solve.png**.

The example command will attempt to solve a 4 X 3 pieces puzzle of *lenna_puzzle.png*.

### Advanced

If unpuzzling does not rearrange pieces correctly, play around with threshold values *PIXEL_DIFFERENCE_THRESHOLD* and *DIFFERENCE_RATE_THRESHOLD* in *Piece.py*. 