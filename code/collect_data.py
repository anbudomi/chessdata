import json
import requests
from collections import deque
from datetime import datetime

# APIs

#chess.com api
chess_com_api = 'https://api.chess.com/pub/player/'
GamesString = 'games/'
starting_username = 'Hikaru'
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
    queue = set()
    queue.add(starting_username)
    #queue = deque([starting_username])
    usernames = set()

    while queue:

        start_year = 0
        end_year = 2024

        start_month = 0
        end_month = 6

        #current_username = queue.popleft()
        current_username = queue.pop()

        url_games = chess_com_api + current_username + '/games/'
        url_profile = chess_com_api + current_username

        if current_username in usernames:
            continue

        #visited.add(current_username)
        usernames.add(current_username)

        joined_timestamp = get_date_timestamp(url_profile)

        start_year = int(get_joined_year(joined_timestamp))
        start_month = int(get_joined_month(joined_timestamp))

        while not start_year == end_year or start_month <= end_month:
             
            if start_month < 10:
                url_games_current_date = url_games + str(start_year) + '/0' + str(start_month)
            else:
                url_games_current_date = url_games + str(start_year) + '/' + str(start_month)

            print(url_games_current_date)

            response = requests.get(url_games_current_date, headers = {'User-Agent': 'username: ChessMaid, email: domkeychess@gmail.com'})
            game_data = response.json()
            game_data = game_data['games']

            if not game_data == '[]':
                for i in range (0, len(game_data)):
                    current_opponent = ''
                    player_white = game_data[i]['white']['username']

                    if player_white == current_username:
                        current_opponent = game_data[i]['black']['username']
                    else:
                        current_opponent = player_white

                    if current_opponent not in usernames and current_opponent not in queue:
                        queue.add(current_opponent)
                    
            if start_month < 12:
                start_month = start_month + 1
            else:
                start_month = 1
                start_year = start_year + 1

            print(len(queue))


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

#test_fetch_games()
fetch_games()