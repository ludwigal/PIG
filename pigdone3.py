import random

def run():
    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    players=[]
    number_of_players = amount_of_players()
    player_holder.number = random.randint(0, number_of_players-1)
    players = get_players(number_of_players,players)
    player_holder.currentplayer = players[player_holder.number]
    welcome_msg(win_points)
    status_msg(players)
    while avslut.state == False:
        gamerunning(players,aborted,number_of_players)



def gamerunning(players,aborted,number_of_players):
        take_turn_msg()
        roll_dice()
        check_for_gameend(aborted)
        totalpoints_calc()
        round_status_msg(players)
        update_spelare(players,number_of_players)



def round_status_msg(players):
    if player_holder.currentplayer.inp == "n" or player_holder.currentplayer.result == 1:
        print("Points: ")
        for player in players:
            print("\t" + player.name + " = " + str(player.totalPts) + " ")

def update_spelare(players,number_of_players):
        if player_holder.currentplayer.inp == "n" or player_holder.currentplayer.result == 1:
            turn(number_of_players,players)


def roll_dice():
    if player_holder.currentplayer.inp == "r":
        player_holder.currentplayer.result = random.randint(1, 6)
        poang()
        running_points_msg()

def check_for_gameend(aborted):
    if player_holder.currentplayer.inp == "r":
        checkwin(aborted)
    elif player_holder.currentplayer.inp == "n":
        pass
    else:
        aborted = True
        game_over_msg(aborted)
        avslut.state=True

def poang():
    if player_holder.currentplayer.result > 1:
        player_holder.currentplayer.roundPts = player_holder.currentplayer.roundPts + player_holder.currentplayer.result
    else:
        player_holder.currentplayer.roundPts = 0


def totalpoints_calc():
    if player_holder.currentplayer.result != 1 and player_holder.currentplayer.inp == "n":
        player_holder.currentplayer.totalPts = player_holder.currentplayer.totalPts + player_holder.currentplayer.roundPts
        player_holder.currentplayer.roundPts = 0
    elif player_holder.currentplayer.result == 1:
        player_holder.currentplayer.roundPts = 0


def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")

def status_msg(the_players):
    print("Points: ")
    for player in the_players:
        print("\t" + player.name + " = " + str(player.totalPts) + " ")

def running_points_msg():
    if player_holder.currentplayer.result > 1:
        print("Got ", player_holder.currentplayer.result, " running total are ", player_holder.currentplayer.roundPts)
    else:
        print("Got 1 lost it all!")

def take_turn_msg():
    print("Its " + player_holder.currentplayer.name + "s turn")
    player_holder.currentplayer.inp = input("Do you wanna roll, hold or quit?")


def turn(number_of_players,players):
    player_holder.number = ((player_holder.number + 1)%number_of_players)
    player_holder.currentplayer = players[player_holder.number]

def checkwin(aborted):
    if player_holder.currentplayer.roundPts + player_holder.currentplayer.totalPts > 19:
        game_over_msg(aborted)
        avslut.state = True

def game_over_msg(is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + player_holder.currentplayer.name + " with "
              + str(player_holder.currentplayer.totalPts + player_holder.currentplayer.roundPts) + " points")

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
        self.number = 0
        self.currentplayer = None
player_holder=Current()

if __name__ == "__main__":
    run()