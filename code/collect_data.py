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

def fetch_games():
    current_username = ''
    queue = set()
    queue.add(starting_username)
    #queue = deque([starting_username])
    usernames = set()

    header_info = get_api_header_info()

    header_user = header_info[0]
    header_email = header_info[1]

    while queue:

        current_username = queue.pop()

        url_games = chess_com_api + current_username + '/games/'
        url_profile = chess_com_api + current_username

        if current_username in usernames:
            continue

        usernames.add(current_username)

        timestamp_data = requests.get(url_profile, headers = {'User-Agent': header_user, "email": header_email})
        timestamp_data = timestamp_data.json()

        joined_timestamp = int(timestamp_data['joined'])
        last_online_timestamp = int(timestamp_data['last_online'])

        start_year = int(get_timestamp_year(joined_timestamp))
        start_month = int(get_timestamp_month(joined_timestamp))

        end_year = int(get_timestamp_year(last_online_timestamp))
        end_month = int(get_timestamp_month(last_online_timestamp))

        while not start_year == end_year or start_month <= end_month:
             
            if start_month < 10:
                url_games_current_date = url_games + str(start_year) + '/0' + str(start_month)
            else:
                url_games_current_date = url_games + str(start_year) + '/' + str(start_month)

            print(url_games_current_date)

            response = requests.get(url_games_current_date, headers = {'User-Agent': header_user, "email": header_email})
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


def get_timestamp_month(timestamp):
    dt = datetime.utcfromtimestamp(timestamp)
    month = int(dt.strftime('%m'))
    return month

def get_timestamp_year(timestamp):
    dt = datetime.utcfromtimestamp(timestamp)
    year = int(dt.strftime('%Y'))
    return year

def get_api_header_info():
    header_info = []
    with open('C:\Repos\chessdata\code\header.txt', 'r') as file:
        lines = file.readlines()

    header_info.append(lines[0].strip())
    header_info.append(lines[1].strip())

    return header_info

fetch_games()