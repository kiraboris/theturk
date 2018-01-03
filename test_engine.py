# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:06:01 2018

@author: Сергей
"""

"""Functions:
    go()
    position()
    etc. from website: о чем думает, как оценивает позицию...
"""
'''
x=5
y=6

if x>y:
  print( x )
else:
    print( y )

print ("Hello world!")
'''
import chess, chess.svg
from IPython.display import SVG, display
#import chess, chess.uci, chess.svg

class Engine :
    def __init__(self, impl):
        self.__impl = impl
        
    def go(self,movetime=1000, async_callback=None):
        self.__impl.go(movetime, async_callback)
    
    def position(self,board):    #send position to...
        self.__impl.position(board)    
    def evaluate(self,board):
        self.__impl.position(board)  
#------

class EngineImpl:
    def go(self,movetime=1000, async_callback=None):
        print("Go!")
    def position(self,board):    #send position to...
        print("Pose..")
    def evaluate(self,board):
       print("Val..")  
   
#------


'''
set position    KQ vs K

что есть?
flag isCheck?
flag isPrevMoveCheck?
move_history  

pos_value = 0
'''

obj_engine = Engine(EngineImpl())
pos_value = 0

#obj_engine.position(0)
#make default board
obj_board = chess.Board()
b = obj_board

#obj_board._set_piece_at

obj_board.clear_board()


#obj_board.set_piece_at()

#obj_board.set_piece_at(square=chess.A8, 
#                       piece=chess.Piece(chess.KING, chess.BLACK ))


obj_board.set_piece_at(square=chess.E8, 
                       piece=chess.Piece(chess.KING, chess.BLACK ))
obj_board.set_piece_at(square=chess.E6, 
                       piece=chess.Piece(chess.KING, chess.WHITE ))

#obj_board.set_piece_at(square=chess.D6, #D7 check E7 checkmate
 #                      piece=chess.Piece(chess.QUEEN, chess.WHITE ))
#obj_board.set_piece_at(square=chess.A6, #D7 check E7 checkmate
#                       piece=chess.Piece(chess.ROOK, chess.WHITE ))

obj_board.set_piece_at(square=chess.A7, #D7 check E7 checkmate
                       piece=chess.Piece(chess.PAWN, chess.WHITE ))

'''
obj_board.set_piece_at(square=chess.E8,
                        piece_type=chess.KING, color=chess.BLACK )

'''
# display(SVG(chess.svg.board(b)))

#b.turn = chess.BLACK
#b.set_castling_fen() 
b.castling_rights = 0

if not b.is_valid():
    print( "invalid board")
    
lm = list(b.legal_moves)
#lm = b.legal_moves
#print( lm )
#for move in lm:
#    print(move, "#" in (b.san(move)))
## print(str(b.san(i)))

if b.is_checkmate():
    print( "checkmate" )
elif b.is_check():
    print( "check" )
else:
    print( "no check")
print( "status =", b.status())

#mate_seq = chess.Move[]

#c=int()
#c=0
moves_with_mate = []
depth=0
qmates=0
mate_depth=0
for i,move in enumerate(lm):
    b.push(move)
    if b.is_checkmate():
        moves_with_mate.append(move)
        qmates += 1
        mate_depth = depth
    b.pop()

if moves_with_mate:  # ==  if qmates>0:
  print( "your move is ", moves_with_mate[0], "qmates = ", qmates )  
else:
  print ( "no mate available" )































