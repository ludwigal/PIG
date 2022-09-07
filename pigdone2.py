import random

def run():
    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    players=[]
    number_of_players = amount_of_players()
    c = random.randint(0, number_of_players-1)
    #currentspelare.spelare=c
    players = get_players(number_of_players,players)
    current = players[c]
    welcome_msg(win_points)
    status_msg(players)
    while avslut.state == False:
        take_turn_msg(current)
        roll_dice(current)
        check_for_gameend(current,aborted)
        totalpoints_calc(current)
        round_status_msg(players,current)
        current = update_spelare(current,players,number_of_players)

def round_status_msg(players,player):
    if player.inp == "n" or player.result == 1:
        print("Points: ")
        for player in players:
            print("\t" + player.name + " = " + str(player.totalPts) + " ")

def update_spelare(player,players,number_of_players):
        if player.inp == "n" or player.result == 1:
            turn(number_of_players)
            i=currentspelare.spelare
            return players[i]
        elif player.inp == "r":
            return player

def roll_dice(player):
    if player.inp == "r":
        player.result = random.randint(1, 6)
        poang(player)
        running_points_msg(player)
def check_for_gameend(current,aborted):
    if current.inp == "r":
        checkwin(current, aborted)
    elif current.inp == "n":
        pass
    else:
        aborted = True
        game_over_msg(current, aborted)
        avslut.state=True

def poang(player):
    if player.result > 1:
        player.roundPts = player.roundPts + player.result
    else:
        player.roundPts = 0


def totalpoints_calc(player):
    if player.result != 1 and player.inp == "n":
        player.totalPts = player.totalPts + player.roundPts
        player.roundPts = 0
    elif player.result == 1:
        player.roundPts = 0


def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")

def status_msg(the_players):
    print("Points: ")
    for player in the_players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")

def running_points_msg(player):
    if player.result > 1:
        print("Got ", player.result, " running total are ", player.roundPts)
    else:
        print("Got 1 lost it all!")

def take_turn_msg(player):
    print("Its " + player.name + "s turn")
    player.inp = input("Do you wanna roll, hold or quit?")


def turn(number_of_players):
    currentspelare.spelare = ((currentspelare.spelare + 1)%number_of_players)

def checkwin(player, aborted):
    if player.roundPts + player.totalPts > 19:
        game_over_msg(player, aborted)
        avslut.state = True

def game_over_msg(players, is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + players.name + " with "
              + str(players.totalPts + players.roundPts) + " points")

def amount_of_players():
    player_amount = int(input("Hur många spelare vill ni ha?"))
    return player_amount

def get_players(number_of_players,players):
    for i in range(number_of_players):
            players.append(Player(create_player((i+1))))
    return players

def create_player(i):
    return (input(f"Vad är spelare {i}'s namn? "))

class Player:

    def __init__(self, name=''):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round
        self.result = 0
        self.inp = None

class Avsluta:

    def __init__(self):
        self.state = False # Total points for all rounds
avslut = Avsluta()


class Current:

    def __init__(self):
        self.spelare = 0
currentspelare=Current()
if __name__ == "__main__":
    run()