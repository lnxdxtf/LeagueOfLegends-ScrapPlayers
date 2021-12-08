import os
from playersSCRAP import scrapApp
from nicksLOL import lolClientScrap

os.system("cls")

#aviso sobre o tesseract, pode ser que o tesseract não extraia o nickname name 100% correto
#tire como comentário o players abaixo, para utilizar o tesseract

app2 = lolClientScrap()
players = app2.takeScreen() 


#caso queira inserior manualmente o nick dos players:

# players = str(input("Digite o nome dos players: "))
# players = players.replace("entrou no saguão",", ").replace("\n"," ")

print("Players/nick: \n", players)
if players:
    app = scrapApp()
    app.getPlayers(players)



