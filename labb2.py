import random
def run():
    c=random.randint(0,1)
    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    vinst = False
    players = get_players()
    current = players[c]
    result = 0
    welcome_msg(win_points)
    while not aborted:
        status_msg(players)
        inp = taketurnmsg(current)
        aborted = taketurn(current, inp, aborted, vinst,result)
        current = turn(current,players)

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

def checkwin_and_taketurn(player,aborted,vinst,inp):
    result = diceroll(player)
    vinst2 = checkwin(player, aborted)
    if vinst2 == True:
        aborted = True
        return aborted
    else:
        round_msg(result, player)
        aborted = roll_or_pass(player,aborted,inp,vinst,result)
        return aborted

def roll_or_pass(player,aborted,inp,vinst,result):
        if result > 1:
            aborted = reroll(player, aborted, inp, vinst, result)
            return aborted
        else:
            pass
        poang(player, result)

def taketurn(player,inp,aborted,vinst,result):

    if inp == "r":
        aborted = checkwin_and_taketurn(player,aborted,vinst,inp)
        return aborted
    elif inp == "n":
        poang(player, result)
        pass
    else:
        aborted = True
        game_over_msg(player,aborted)
        return aborted


def diceroll(player):
    result = random.randint(1, 6)
    player.roundPts = player.roundPts + result
    return result

def reroll(player,aborted,inp,vinst,result):
    inp2 = input("Do you wanna roll, hold or quit?")
    inp2 = inp2.lower()
    if inp2 == "r":
        aborted = taketurn(player, inp, aborted, vinst,result)
        return aborted
    elif inp2 == "n":
        poang(player,result)
        pass
    else:
        aborted = True
        game_over_msg(player, aborted)
        return aborted

def turn(spelare,players):
    if spelare == players[0]:
        return players[1]
    else:
        return players[0]

def checkwin(player,aborted):
    if player.roundPts + player.totalPts > 19 :
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
    players = [Player(name=input("V??lj spelare 1s namn")), Player(name=input("V??lj spelare 2s namn"))]
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