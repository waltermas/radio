#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import  QApplication,  QSystemTrayIcon,  QAction,  QMenu
#from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import vlc
from functools import partial
import requests
from bs4 import BeautifulSoup


p = vlc.MediaPlayer("http://fmvida.radio.rosario3.com:8000/fmvida.mp3")

class Example(QSystemTrayIcon):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):               
        icono = QIcon()
        #icono.addFile('/home/waltermasb/MEGAsync/gits/radio/radio.png',  QSize(56, 56))
        icono.addFile('radio.png')
        self.setIcon(icono)
        menuradios = QMenu()

        pagina = requests.get('https://docs.google.com/spreadsheets/d/1rQncpm7tJJpHXBn1YicCYCAh0sUegDS308NZoqUqtw4/pubhtml')
        soup = BeautifulSoup(pagina.text, 'html.parser')
        table_body = soup.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows[2:]:
            cols = row.find_all('td')
            radioAction = QAction(cols[1].text.strip(),  self)
            radioAction.triggered.connect(partial(self.tocarradio, cols[2].text.strip()))
            menuradios.addAction(radioAction)
             
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.salir)

        menuradios.addAction(exitAction)
        self.setContextMenu(menuradios)
  
        self.show()
        
    def salir(self):
        QApplication.quit()
        
    def play(self):
        p.play()
        
    def tocarradio(self,  frecuencia):
        #print(frecuencia)
        global p
        p.stop()
        p = vlc.MediaPlayer(frecuencia)
        p.play()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
