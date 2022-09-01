# /*
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29
#  *
#  */
import random
def run():
    c=random.randint(0,1)
    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    vinst = False
    players = get_players()
    current = players[c]  # TODO Set random player to start

    welcome_msg(win_points)
    while not aborted:
        status_msg(players)
        inp = taketurnmsg(current)
        aborted = taketurn(current, inp, aborted, vinst)
        current = turn(current,players)



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

def taketurnmsg(player):
    print("Its " + player.name + "s turn")
    inp = input("Do you wanna roll, hold or quit?")
    return inp




def taketurn(player,inp,aborted,vinst):

    if inp == "r":
        result = random.randint(2,5)
        player.roundPts=player.roundPts + result
        vinst2 = checkwin(player,aborted,vinst)
        if vinst2 == True:
            aborted = True
            return aborted
        else:
            round_msg(result, player)
            if result > 1:
                inp2 = input("Do you wanna roll, hold or quit?")
                inp2 = inp2.lower()
                if inp2 == "r":
                    aborted = taketurn(player,inp,aborted,vinst)
                    return aborted
                elif inp2 == "n":
                    pass
                else:
                    aborted = True
                    game_over_msg(player,aborted)
                    return aborted
            else: pass
            poang(player, result)
    elif inp == "n":
        pass
    else:
        aborted = True
        game_over_msg(player,aborted)
        return aborted


def turn(spelare,players):
    if spelare == players[0]:
        return players[1]
    else:
        return players[0]

def checkwin(player,aborted,vinst):
    if player.roundPts + player.totalPts > 5 :
        game_over_msg(player,aborted)
        vinst = True
        return vinst

def game_over_msg(players, is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + players.name + " with "
              + str(players.totalPts + players.roundPts) + " points")

def get_player_choice(player):
    input("Player is " + player.name + " > ")


def get_players():
    players = [Player(name=input("Välj spelare 1s namn")), Player(name=input("Välj spelare 2s namn"))]
    return players




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