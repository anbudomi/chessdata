
import sqlite3
import json
import requests
from collections import deque

# APIs

#chess.com api
chess_com_api = 'https://api.chess.com/pub/player/'
GamesString = 'games/'
CurrentUsername = ''
#api is a string that will have to get modified for each players profile
#to access games the api string will need to have the following format:
#'https://api.chess.com/pub/player/games/yyyy/mm'
#Note: its easiest to start with the current date and then go back until you can't find games (for a year)


#The following code is going to be a test for the JSON data

def fetch_games():
    
    url = chess_com_api + 'hikaru/games/2023/10'
    
    print(url)
    
    response = requests.get(url)
    GameData = response.json()
    
    print(GameData)
    

fetch_games()