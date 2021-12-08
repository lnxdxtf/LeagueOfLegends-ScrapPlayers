from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import error, path
import time


main_folder = path.join(path.expanduser("~"), r"AppData\Local\Mozilla Firefox\firefox.exe")
options = Options()

#options.headless = True
options.binary_location = main_folder

class scrapApp():
    def __init__(self):
        self.driver = webdriver.Firefox(options=options,executable_path=r"geckodriver.exe")

    def getPlayers(self, players):
        self.driver.get("https://br.op.gg")
        time.sleep(2)
        playersBox = self.driver.find_element_by_xpath('//*[@id="searchUserName"]')
        playersBox.clear()
        playersBox.send_keys(players)
        playersBox.send_keys(Keys.RETURN)
        self.getInfoPlayers()
        time.sleep(2)
        return self.getInfoPlayers()

    def getInfoPlayers(self):
        time.sleep(5)
        infoPlayers = {}
        summoners_divs = self.driver.find_elements_by_class_name("summoner-summary")
        for summoner in summoners_divs:
            try:
                summoner_name = summoner.find_element_by_tag_name("a").text
                summoner_position = summoner.find_element_by_class_name("most-position")
                summoner_position = summoner_position.find_element_by_tag_name("i").get_property("className")  
                summoner_position = summoner_position.split("--")[1]
                summoner_winrate = summoner.find_element_by_class_name("winratio").text
               
            except:
                summoner_position = None
                summoner_winrate = None
                print("|Nick: ",summoner_name ,"|Lane: ", str(summoner_position),"|Winrate: ", summoner_winrate, "|STATUS: OUT OF DATE ")
                infoPlayers[f'Player: {summoner_name}'] = {
                                                            "Status": "OUT OF DATE",
                                                            "Lane": summoner_position,
                                                            "WinRate": summoner_winrate
                                                                }
            else:
                print("|Nick: ",summoner_name ,"|Lane: ", str(summoner_position),"|Winrate: ", summoner_winrate)
                infoPlayers[f'Player: {summoner_name}'] = {
                                                            "Status": "UPDATED"
                                                            "Lane": summoner_position,
                                                            "WinRate": summoner_winrate
                                                                }
            

        self.driver.quit()
        print(infoPlayers)
        return infoPlayers




        

