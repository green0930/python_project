import random


def play():
    user = input("What is your choice? "'r' for rock, \
     'p' for paper, 's' for scissors") \
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'tie'
    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'


def is_win(player, opponent):
    # return true if player wins
    if(player == 'r' and opponent == 's') \ or
    (player == 's' and oppenent == 'p') \
        or (player == 'p' and oppenent == 'r')
    return True


print(play)
