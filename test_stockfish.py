# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 20:09:59 2018

@author: Kirill
"""
import sys
import chess, chess.uci, chess.svg
from PyQt5 import QtCore, QtWidgets, QtSvg 

#init engine 
obj_engine = chess.uci.popen_engine("stockfish")
obj_engine.uci()
print(obj_engine.author)

#make default board
obj_board = chess.Board()

# simple playout
def play_move(callback):
    return obj_engine.go(movetime=2000, async_callback=callback)

# create demo chess window
class DemoWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.svg_widget = QtSvg.QSvgWidget()
        self.setCentralWidget(self.svg_widget)
        
        # start game
        play_move(self.continue_game)
        
    def continue_game(self, command):
       
        if command:
            move, ponder = command.result()
           
            obj_board.push(move)
            obj_engine.position(obj_board)
        
            if(obj_board.is_game_over()):
                return
            else:   
                # redraw board
                str_svg_board = chess.svg.board(obj_board)
                obj_temp = QtCore.QByteArray.fromRawData(
                        bytes(str_svg_board, "ascii"))
                self.svg_widget.load(obj_temp)
                
                # continue game
                play_move(self.continue_game)
           
           
# run demo qt application
obj_app = QtWidgets.QApplication(sys.argv)
obj_window = DemoWindow()
obj_window.show()
sys.exit(obj_app.exec_())