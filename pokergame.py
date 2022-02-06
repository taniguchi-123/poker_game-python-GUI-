# -*- coding: utf-8 -*-
"""
Created on Dec 4  2021
@author: taniguchi
"""

import card_check 
import random,time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QCheckBox,QVBoxLayout,QHBoxLayout,
    QAction, QApplication,QLabel,QWidget,QPushButton)  
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Main(QMainWindow):

    global card   #used inside of other method 
    card =[["S",1],["S",2],["S",3],["S",4],["S",5],["S",6],
           ["S",7],["S",8],["S",9],["S",10],["S",11],["S",12,],["S",13,],
           ["H",1],["H",2],["H",3],["H",4],["H",5],["H",6],
           ["H",7],["H",8],["H",9],["H",10],["H",11],["H",12,],["H",13,],
           ["C",1],["C",2],["C",3],["C",4],["C",5],["C",6],
           ["C",7],["C",8],["C",9],["C",10],["C",11],["C",12,],["C",13,],
           ["D",1],["D",2],["D",3],["D",4],["D",5],["D",6],
           ["D",7],["D",8],["D",9],["D",10],["D",11],["D",12,],["D",13,]]
    
    
    def __init__(self):
        super().__init__()
        
        #make instance for sub class
        self.check = card_check.CardCheck()
        self.data = []                       
        
        #program_title
        self.setWindowTitle('Poker Game')
        self.programTitle = QLabel('Poker Game',self)        
        self.programTitle.setStyleSheet("font: 30pt Cambria")
        
        #overall layout
        layout = QVBoxLayout()
        self.setStyleSheet("background-color:white")        
        card_layout = QtWidgets.QHBoxLayout()
        checkbox_layout = QtWidgets.QHBoxLayout()
        bt1_layout = QtWidgets.QGridLayout()
        bt1_layout.setContentsMargins(0,0,0,20)
        bt2_layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.programTitle)
        layout.addLayout(card_layout)
        layout.addLayout(checkbox_layout)
        layout.addLayout(bt1_layout)
        layout.addLayout(bt2_layout)
        self.setGeometry(500, 100, 330, 200)
        
        
        # card diplay (# card order on display is #1 #2 #3 #4 #5)
        self.card1 = QtWidgets.QLabel('card1')
        self.card2 = QtWidgets.QLabel('card2')
        self.card3 = QtWidgets.QLabel('card3')
        self.card4 = QtWidgets.QLabel('card4')
        self.card5 = QtWidgets.QLabel('card5')
        self.card1.setPixmap(QPixmap("card/cover.bmp"))
        self.card2.setPixmap(QPixmap("card/cover.bmp"))
        self.card3.setPixmap(QPixmap("card/cover.bmp"))
        self.card4.setPixmap(QPixmap("card/cover.bmp"))
        self.card5.setPixmap(QPixmap("card/cover.bmp"))
        
        card_layout.addWidget(self.card1)
        card_layout.addWidget(self.card2)
        card_layout.addWidget(self.card3)
        card_layout.addWidget(self.card4)
        card_layout.addWidget(self.card5)
        
        # checkbox for card replacement.
        self.cb1 = QtWidgets.QCheckBox("change")
        self.cb2 = QtWidgets.QCheckBox("change")
        self.cb3 = QtWidgets.QCheckBox("change")
        self.cb4 = QtWidgets.QCheckBox("change")
        self.cb5 = QtWidgets.QCheckBox("change")
        self.cb1.stateChanged.connect(self.checkBoxChangedAction1)
        self.cb2.stateChanged.connect(self.checkBoxChangedAction2)
        self.cb3.stateChanged.connect(self.checkBoxChangedAction3)
        self.cb4.stateChanged.connect(self.checkBoxChangedAction4)
        self.cb5.stateChanged.connect(self.checkBoxChangedAction5)
        checkbox_layout.addWidget(self.cb1)
        checkbox_layout.addWidget(self.cb2)
        checkbox_layout.addWidget(self.cb3)
        checkbox_layout.addWidget(self.cb4)
        checkbox_layout.addWidget(self.cb5)
        
        #initialise checkbox  #list for checkbox signal status
        self.check_box_list = [False,False,False,False,False] 

        # Pushbutton for card replacement.        
        change_bt = QPushButton("card change")
        change_bt.setStyleSheet("background-color:lightgreen")        
        bt1_layout.addWidget(change_bt,0,0)
        change_bt.clicked.connect(self.replace_card)
        
        # Pushbutton for card replacement.        
        start_bt = QPushButton("New Game")
        start_bt.setStyleSheet("background-color:lightblue")        
        bt1_layout.addWidget(start_bt,2,0)
        start_bt.clicked.connect(self.game_start)
        
        #message_layout
        self.messageShow = QTextEdit()
        self.messageShow.setStyleSheet("font: 10pt")        
        bt1_layout.addWidget(self.messageShow,0,1,3,3)
        
        
        #overall layout        
        self.container = QWidget()
        self.container.setLayout(layout)
        self.setCentralWidget(self.container)       
        self.show()
        
        
    def game_start(self):
        self.messageShow.setText('')                     
        self.data = []                       
        x = random.sample(card, 5)  #pick up 5 different cards 
        for i in range(5):
            self.data.append(x[i-1])
        self.card_dislay()

    def card_dislay(self):
        folder = 'card' 
        card_info = []
        for i in range(5):
            mark = self.data[i][0]
            number = self.data[i][1]
            card_info.append(str(mark)+str(number))
                            
        # card diplay 
        self.card1.setPixmap(QPixmap(str(folder)+"/"+str(card_info[0])+".bmp"))
        self.card2.setPixmap(QPixmap(str(folder)+"/"+str(card_info[1])+".bmp"))
        self.card3.setPixmap(QPixmap(str(folder)+"/"+str(card_info[2])+".bmp"))
        self.card4.setPixmap(QPixmap(str(folder)+"/"+str(card_info[3])+".bmp"))
        self.card5.setPixmap(QPixmap(str(folder)+"/"+str(card_info[4])+".bmp"))
        
        
    #check_box operation
    def checkBoxChangedAction1(self, state):
        self.flag = (state == QtCore.Qt.Checked)
        self.check_box_list[0] = self.flag
        
    def checkBoxChangedAction2(self, state):
        self.flag = (state == QtCore.Qt.Checked)
        self.check_box_list[1] = self.flag
        
    def checkBoxChangedAction3(self, state):
        self.flag = (state == QtCore.Qt.Checked)
        self.check_box_list[2] = self.flag
        
    def checkBoxChangedAction4(self, state):
        self.flag = (state == QtCore.Qt.Checked)
        self.check_box_list[3] = self.flag
        
    def checkBoxChangedAction5(self, state):
        self.flag = (state == QtCore.Qt.Checked)
        self.check_box_list[4] = self.flag
        
    def checkBoxclear(self):
        self.cb1.setChecked(False)
        self.cb2.setChecked(False)
        self.cb3.setChecked(False)    
        self.cb4.setChecked(False)
        self.cb5.setChecked(False)   
        
                
    #def replace_card(data):
    def replace_card(self,data):
        if (self.data):      #start operation after data is input
            #reset the color of message area
            self.messageShow.setStyleSheet("background-color:white")
            #count qty of True flag in check_box
            change_card_qty = 0    
            for element in range(5):
                if self.check_box_list[element] == True:
                    change_card_qty = change_card_qty + 1
            
            #delete element in data[] if check_box flag is "True"
            for j in reversed(range(1,6)):
                if self.check_box_list[j-1] == True:
                    del self.data[j-1]
                    new_card = random.sample(card, 1)
                    self.data.insert(j-1,new_card[0])
            time.sleep(1)
            self.card_dislay()
            res = self.check.card_check(self.data)  
            self.messageShow.setText(res)
            if  res != '' :
                self.congratulation()                     
            self.checkBoxclear()
        
    def congratulation(self):
        self.messageShow.setStyleSheet("font: 20pt Cambria; background-color:#CCFFFF")
        
        
        
if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mw = Main()
    sys.exit(app.exec_())


