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

import chess, chess.svg
from IPython.display import SVG, display
#import chess, chess.uci, chess.svg

class Value :
    #is_def = False   #static!!
    #val = 0
    def __init__(self):
        self.val=0
        self.is_def=False
        self.depth=0
        self.mate_seq = []
        
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
obj_board.clear_board()



obj_board.set_piece_at(square=chess.F8, 
  piece=chess.Piece(chess.KING, chess.BLACK ))
obj_board.set_piece_at(square=chess.D6, 
  piece=chess.Piece(chess.KING, chess.WHITE ))

obj_board.set_piece_at(square=chess.D2, #D7=check E7=checkmate D6=next move mate
  piece=chess.Piece(chess.QUEEN, chess.WHITE ))

display(SVG(chess.svg.board(b)))

'''
obj_board.set_piece_at(square=chess.H8, 
piece=chess.Piece(chess.KING, chess.BLACK ))

obj_board.set_piece_at(square=chess.G6, 
piece=chess.Piece(chess.KING, chess.WHITE ))


obj_board.set_piece_at(square=chess.A6, #D7 check E7 checkmate
 piece=chess.Piece(chess.PAWN, chess.WHITE ))




#obj_board.set_piece_at(square=chess.A8, 
#                       piece=chess.Piece(chess.KING, chess.BLACK ))
obj_board.set_piece_at(square=chess.D8, 
                       piece=chess.Piece(chess.KING, chess.BLACK ))
obj_board.set_piece_at(square=chess.D6, 
                       piece=chess.Piece(chess.KING, chess.WHITE ))

obj_board.set_piece_at(square=chess.C5, #D7=check E7=checkmate D6=next move mate
                       piece=chess.Piece(chess.QUEEN, chess.WHITE ))
#obj_board.set_piece_at(square=chess.A6, #D7 check E7 checkmate
#                       piece=chess.Piece(chess.ROOK, chess.WHITE ))

#obj_board.set_piece_at(square=chess.A7, #D7 check E7 checkmate
#                       piece=chess.Piece(chess.PAWN, chess.WHITE ))
'''
# display(SVG(chess.svg.board(b)))
#b.turn = chess.BLACK
#b.set_castling_fen() 
b.castling_rights = 0

if not b.is_valid():
    print( "invalid board")

q_calls=0

def find_mate(bb=chess.Board(), depth=0 ): #bb=chess.Board()
   
    global q_calls    
    global v
    q_calls += 1
    
   # print( "q_calls=", q_calls )
   # global b
   # bb = b
    #bb = chess.Board() 
    b = bb
    #b = bb
    #display(SVG(chess.svg.board(b)))
    print( "depth=", depth, " turn=", b.turn )  #, end=' '
       #как заставить дожидаться нажатия клавиши? как вообще остановить процесс?
    lm = list(b.legal_moves)
   # print( lm )
    #lm = b.legal_moves
    #print( lm )
    #for move in lm:
    #    print(move, "#" in (b.san(move)))
    ## print(str(b.san(i)))
    
    if b.is_checkmate(): #функцию надо вызывать только один раз, ввести лок. перем
        print( "checkmate" )
    elif b.is_check():
        print( "check" )
    #else:
    #    print( "no check")
   #print( "status =", b.status()) #0 if valid
    
    #mate_seq = chess.Move[]
    moves_with_mate = []
    #c=int()
    #c=0

   # depth=0
    qmates=0
    dd=depth

    vv = Value()
  #  mate_depth=0
    for i,move in enumerate(lm):
        #print( " " + move.uci(), " N", q_calls, end='')
        b.push(move)
        if b.is_checkmate():
            qmates += 1
            moves_with_mate.append(move)
            #print( "#", end='')
            
            vv.is_def = True
            #if( turn ):
            vv.val = 1000
            #else:
            #    vv.val = -1000
            vv.depth=depth
            vv.mate_seq = [(move.uci(), not b.turn)] + [None] * (depth)
            
            #break  #относится не к for??  почему при втором вызове уже не заходит?
          #  mate_depth = depth
        #почему не позволяет вставить многострочный комментарий?
        elif depth<4:
            deeper_vv=find_mate(b, depth=dd+1)
            #deeper_vv.val *= -1
            if(q_calls == 34):
                print("DEBUG ", vv.val, " ", vv.is_def, "D: ",
                      deeper_vv.val, " ", deeper_vv.is_def)
                #input()
            if( deeper_vv.is_def ):
                if( deeper_vv.val>vv.val or i == 0): #or i==0
                    vv = deeper_vv
                    vv.mate_seq[-depth-1] = (move.uci(), not b.turn)
            else:
                if(not vv.is_def or vv.is_def and vv.val < 0): 
                    vv = Value()
                    qmates = 0
                    moves_with_mate = []
                    
        b.pop()
        #if( vv.is_def ):
        #    break

   # display(SVG(chess.svg.board(b)))
    print("qmates =", qmates) 
   
    #if moves_with_mate:  # ==  if qmates>0:
    #  print( "", moves_with_mate[0], "  qmates = ", qmates )  
    #else:
    #  pass # print ( "no mate available" )
    
    #print( 1>0 and 2>3 )
   # print( "depth % 2 =", depth % 2 )
    if depth > 0 and vv.is_def:
        vv.val =-vv.val
        
    return vv
#end def find_mate

v=Value()  
print( " moves ",  b.legal_moves )
x=5  
v=find_mate(b,depth=0)
print( "\n Value defined", v.is_def, " value=", v.val )
print( " sequence: ", list(reversed(v.mate_seq)) )
#find_mate(b,depth=0)
#find_mate(b,1)  #посылает 0
#find_mate(b,depth=1) #посылает 1
#find_mate(b,depth=x+1) #посылает 6

print( "q_calls=", q_calls )


''' 
        elif depth<1:
             b.turn = not b.turn
             find_mate(b,depth+1)
             b.turn = not b.turn
'''


























