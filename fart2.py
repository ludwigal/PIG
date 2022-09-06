import random

def run():
    win_points = 20  # Points to win (decrease if testing)
    aborted = False
    players=[]
    antspelare = antalspelare()
    c = random.randint(0, antspelare-1)
    currentspelare.spelare=c
    players = get_players(antspelare,players)
    current = players[c]
    welcome_msg(win_points)
    status_msg(players) 
    while avslut.state == False:
        inp = taketurnmsg(current)
        rolldice(current,inp)
        taturn(current,inp,aborted)
        totalpoang(current,inp)
        roundstatusmsg(inp,players,current)
        current = updatespelare(inp,current,players,antspelare)

def roundstatusmsg(inp,players,player):
    if inp == "n" or player.result == 1:
        print("Points: ")
        for player in players:
            print("\t" + player.name + " = " + str(player.totalPts) + " ")

def updatespelare(inp,player,players,antspelare):
        if inp == "n" or player.result == 1:
            turn(antspelare)
            i=currentspelare.spelare
            return players[i]
        elif inp == "r":
            return player

def rolldice(player,inp):
    if inp == "r":
        player.result = diceroll()
        poang(player)

def taturn(current, inp,aborted):
    if inp == "r":
        checkwin(current, aborted)
    elif inp == "n":
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
    round_msg(player)

def totalpoang(player,inp):
    if player.result != 1 and inp == "n":
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

def round_msg(player):
    if player.result > 1:
        print("Got ", player.result, " running total are ", player.roundPts)
    else:
        print("Got 1 lost it all!")

def taketurnmsg(player):
    print("Its " + player.name + "s turn")
    inp = input("Do you wanna roll, hold or quit?")
    return inp

def diceroll():
    result = random.randint(1, 6)
    return result

def turn(antspelare):
    currentspelare.spelare = ((currentspelare.spelare + 1)%antspelare)

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

def antalspelare():
    antspelare = int(input("Hur många spelare vill ni ha?"))
    return antspelare

def get_players(antspelare,players):
    for i in range(antspelare):
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
        self.current = None

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




