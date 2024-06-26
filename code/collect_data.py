import json
import requests
from collections import deque
from datetime import datetime

# APIs

#chess.com api
chess_com_api = 'https://api.chess.com/pub/player/'
GamesString = 'games/'
starting_username = 'hikaru'
#api is a string that will have to get modified for each players profile
#to access games the api string will need to have the following format:
#'https://api.chess.com/pub/player/games/yyyy/mm'


#The following code is just for figuring out the chess.com API and playing around

def test_fetch_games():
    
    #url = chess_com_api + 'hikaru/games/2023/10'
    url = chess_com_api + 'hikaru/'
    print(url)
    
    response = requests.get(url, headers = {'User-Agent': 'username: ChessMaid, email: domkeychess@gmail.com'})
    print(response)

    GameData = response.json()
    #print(GameData['games'])
    print(GameData['joined'])

    #GameData = GameData['games']

    #for i in range(0, len(GameData)):
        #user = GameData[i]['white']['username']
        #print(user)


def fetch_games():
    current_username = ''
    
    visited = set()
    queue = deque([starting_username])
    usernames = set()

    while queue:

        start_year = 0
        end_year = 2024

        start_month = 0
        end_month = 6

        current_username = queue.popleft()

        url_games = chess_com_api + current_username + 'games/'
        url_profile = chess_com_api + current_username

        if current_username in visited:
            continue

        visited.add(current_username)
        usernames.add(current_username)

        joined_timestamp = get_date_timestamp(url_profile)

        start_year = get_joined_year(joined_timestamp)
        start_month = get_joined_month(joined_timestamp)

        while start_year <= end_year and start_month <= end_month:
             



             

def get_joined_month(timestamp):
    dt = datetime.utcfromtimestamp(timestamp)
    month = int(dt.strftime('%m'))
    return month

def get_joined_year(timestamp):
    dt = datetime.utcfromtimestamp(timestamp)
    year = int(dt.strftime('%Y'))
    return year

def get_date_timestamp(url):
        response = requests.get(url, headers = {'User-Agent': 'username: ChessMaid, email: domkeychess@gmail.com'})
        temp_timestamp = response.json()
        temp_timestamp = int(temp_timestamp['joined'])
        return temp_timestamp

test_fetch_games()
#fetch_games()