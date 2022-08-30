# /*
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29
#  *
#  */
import random
gamerunning=True
def run():

    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    # Hard coded players, replace *last* of all with ... (see below)
    players = [Player("Olle"), Player("Fia")]
    # players = getPlayers()    # ... this (method to read in all players)
    current = players[0]  # TODO Set random player to start
    welcome_msg(win_points)
    while gamerunning:
        status_msg(players)
        taketurnmsg(current,aborted)
        if kollavinst(current):
            break
        current = turn(current,players)

def kollavinst(player):
    if player.roundPts + player.totalPts > 5 :
        return kollavinst


        # TODO Game logic, using small step, functional decomposition


def poang(player,result):
    if result > 1:
        player.totalPts = player.totalPts + player.roundPts
        player.roundPts=0
    else: player.roundPts=0


class Player:

    def __init__(self, name=''):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round


# ---- Game logic methods --------------
# TODO
#


# ---- IO Methods --------------
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
        print("Got ", result ," running total are ", current_player.roundPts)
    else:
        print("Got 1 lost it all!")

def taketurnmsg(player,aborted):
    print("Its " + player.name + "s turn")
    inp = input("Do you wanna roll or hold?")
    taketurn(player,inp,aborted)

def taketurn(player,inp,aborted):

    if inp == "r":
        result = random.randint(1,6)
        player.roundPts=player.roundPts + result
        if checkwin(player,aborted):
            pass
        else:
            round_msg(result, player)
            if result > 1:
                inp2 = input("Do you wanna roll again?")
                inp2 = inp2.lower()
                if inp2 == "yes":
                    taketurn(player,inp,aborted)
            else: pass
            poang(player, result)


def turn(spelare,players):
    if spelare == players[0]:
        return players[1]
    else:
        return players[0]

def checkwin(player,aborted):
    if player.roundPts + player.totalPts > 5 :
        game_over_msg(player,aborted)
        return checkwin

def game_over_msg(player, is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + player.name + " with "
              + str(player.totalPts + player.roundPts) + " points")

def get_player_choice(player):
    input("Player is " + player.name + " > ")


def get_players():
    # TODO
    pass




# ----- Testing -----------------
# Here you run your tests i.e. call your game logic methods
# to see that they really work (IO methods not tested here)
def test():
    # This is hard coded test data
    # An array of (no name) Players (probably don't need any name to test)
    test_players = [Player(), Player(), Player()]
    # TODO Use for testing of logical methods (i.e. non-IO methods)


if __name__ == "__main__":
    run()
