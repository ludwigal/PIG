import random

def run():
    c = random.randint(0, 1)
    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    players = get_players()
    current = players[c]
    welcome_msg(win_points)
    status_msg(players)
    while not aborted:
        inp = taketurnmsg(current)
        result = rolldice(current,inp)
        aborted = taturn(current,inp,aborted)
        totalpoang(current,result,inp)
        roundstatusmsg(inp,result,players)
        current = updatespelare(inp,current,players,result)

def roundstatusmsg(inp,result,players):
    if inp == "n" or result == 1:
        print("Points: ")
        for player in players:
            print("\t" + player.name + " = " + str(player.totalPts) + " ")

def updatespelare(inp,current,players,result):
        if inp == "n" or result == 1:
            current=turn(current, players)
            return current
        elif inp == "r":
            return current

def rolldice(current,inp):
    if inp == "r":
        result = diceroll()
        poang(current, result)
        return result

def taturn(current, inp,aborted):
    if inp == "r":
        aborted = checkwin(current, aborted)
        return aborted
    elif inp == "n":
        pass
    else:
        aborted = True
        game_over_msg(current, aborted)
        return aborted

def poang(player, result):
    if result > 1:
        player.roundPts = player.roundPts + result
    else:
        player.roundPts = 0
    round_msg(result, player)

def totalpoang(player, result,inp):
    if result != 1 and inp == "n":
        player.totalPts = player.totalPts + player.roundPts
        player.roundPts = 0
    elif result == 1:
        player.roundPts = 0

class Player:

    def __init__(self, name=''):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round

def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")

def status_msg(the_players):
    print("Points: ")
    for player in the_players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")

def round_msg(result, current_player):
    if result > 1:
        print("Got ", result, " running total are ", current_player.roundPts)
    else:
        print("Got 1 lost it all!")

def taketurnmsg(player):
    print("Its " + player.name + "s turn")
    inp = input("Do you wanna roll, hold or quit?")
    return inp

def diceroll():
    result = random.randint(2, 6)
    return result

def turn(spelare, players):
    if spelare == players[0]:
        spelare = players[1]
    else:
        spelare = players[0]
    return spelare

def checkwin(player, aborted):
    if player.roundPts + player.totalPts > 19:
        game_over_msg(player, aborted)
        aborted = True
        return aborted

def game_over_msg(players, is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + players.name + " with "
              + str(players.totalPts + players.roundPts) + " points")

def get_players():
    players = [Player(name=input("Välj spelare 1s namn")), Player(name=input("Välj spelare 2s namn"))]
    return players

if __name__ == "__main__":
    run()