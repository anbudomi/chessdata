
import sqlite3
import requests
from collections import deque

# APIs

#chess.com api
chess_com_api = 'https://api.chess.com/pub/player/'
#api is a string that will have to get modified for each players profile


#lichess api
#idk yet



#The following code is going to be a test for the JSON

def fetch_games():
    
    url = chess_com_api + 'gmhikaru/games'
    
    print(url)
    
    response = response.json()
    
    print(response)
    

fetch_games()