import json
from functions import calcular_novo_rating

with open('data.json', encoding='utf-8') as playersdata:
    players = json.load(playersdata)

gamedata = open('Partidas.txt', 'r', encoding='utf-8')

def makeBackup(players):
    with open('backup.json', 'w', encoding='utf-8') as backupdata:
        json.dump(players, backupdata, indent=4, ensure_ascii=False)
    backupdata.close()

def searchByName(players, playerName) :
    for player in players:
        if player['name'] == playerName:
            return player
    newplayer = {}
    newplayer['name'] = playerName
    newplayer['rating'] = '950'
    newplayer['wins'] = '0'
    newplayer['losses'] = '0'
    players.append(newplayer)
    print("Novo player adicionado")
    return player



def sortPlayersByName(players):
    players.sort(key=lambda x: x['name'])
    return players

def executeGame(players, player1name, player2name, result, gameType):
    player1 = searchByName(players, player1name)
    player2 = searchByName(players, player2name)
    rating1 = int(player1['rating'])
    rating2 = int(player2['rating'])

    result1, result2 = calcular_novo_rating(rating1, rating2, result, gameType)
    player1['rating'] = result1
    player2['rating'] = result2
    player1['wins'] = str(int(player1['wins']) + 1)
    player2['losses'] = str(int(player2['losses']) + 1)

def updatePlayers(players):
    with open('data.json', 'w', encoding='utf-8') as playersdataupload:
        json.dump(players, playersdataupload, indent=4, ensure_ascii=False)

def executeAllGames(players):
    while True:
        p1name = gamedata.readline().strip()
        p2name = gamedata.readline().strip()
        result_line = gamedata.readline().strip()
        gameType_line = gamedata.readline().strip()
        gamedata.readline()

        if not p1name or not p2name or not result_line or not gameType_line:
            break

        result = int(result_line.split()[0])
        gameType = int(gameType_line.split()[0])
        executeGame(players, p1name, p2name, result, gameType)

makeBackup(players)
executeAllGames(players)
sortPlayersByName(players)
updatePlayers(players)
playersdata.close()