
import chess 
import chess.svg

from StringIO import StringIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



def draw(str_svg):
    file_like = StringIO(bytes(str_svg))
    pic = mpimg.imread(file_like, format="svg")
    plt.imshow(pic)



b = chess.Board()

svg = chess.svg.board(b)

draw(svg)
