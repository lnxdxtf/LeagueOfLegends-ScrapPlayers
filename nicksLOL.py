from os import putenv
from numpy.lib.npyio import load
import pyautogui 
from pytesseract import pytesseract
import os
import time

class lolClientScrap():
    def __init__(self):
        tesseractPath = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        pytesseract.tesseract_cmd = tesseractPath
        
    def takeScreen(self):
        os.system('cls')
        print("Procurando: ")
        while True:
            screenCheck = pyautogui.locateOnScreen('chatChampionSelect.png', confidence = 0.4)
            if screenCheck:
                self.img = pyautogui.screenshot(region=(screenCheck.left,screenCheck.top,378,200))
                return self.recognitionNicks()

    def recognitionNicks(self):
         
        dados = pytesseract.image_to_string( self.img ).replace("\n","").replace("entrou no sagulo", ", ").replace("entrou no saguao",", ").replace("entrou no saguso",", ").replace("‘",", ").replace("entrou no saguéo",", ").replace("entrou no sagu3o",", ").replace("entrou no sagu8o",", ").replace("entrou no sagudo",", ")
        
        return dados


        #print(pytesseract.image_to_string( Image.open('chatChampionSelect.png')))
