# Rock, Paper, Scissors Game


def rps():
    player_one = input("[R]ock, [P]aper, or [S]cissors? ")
    print("Player two's turn.")
    player_two = input("[R]ock, [P]aper, or [S]cissors? ")
    player_one = player_one.upper()
    player_two = player_two.upper()

    if player_one == player_two : print("It's a tie! You both chose {}.".format(player_one))
    elif (player_one == 'R' and player_two == 'P') or (player_one == 'S' and player_two == 'R') or (player_one == 'P' and player_two == 'S'):
        print("{} vs {}. Player two wins! ".format(player_one,player_two))
    elif (player_one == 'P' and player_two == 'R') or (player_one == 'R' and player_two == 'S') or (player_one == 'S' and player_two == 'P'):
        print("{} vs {}. Player one wins! ".format(player_one,player_two))
    again = input("Play again? Y/n ")
    if again.upper == 'Y':
        rps()

rps()
