import random

board_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def update_board(l):
    board_list = l
    board = """
   %s   |   %s   |   %s
-----------------------
   %s   |   %s   |   %s
-----------------------
   %s   |   %s   |   %s""" % (tuple(board_list))
    return board


board = update_board(board_list)


def player_turn(marker):
    temp_list = []
    num = 1
    for item in board_list:
        if item == " ":
            temp_list.append(num)
        else:
            temp_list.append(item)
        num = num + 1
    temp_board = update_board(temp_list)
    print(temp_board)
    while 1:
        try:
            spot = input("Gdzie chciałbyś postawić znak? ")
            while temp_list[int(spot) - 1] in ["X", "O"] or spot not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                spot = raw_input("Gdzie chciałbyś postawić znak? ")
        except IndexError:
            continue
        break
    spot = int(spot) - 1
    board_list[spot] = marker
    return update_board(board_list)


def comp_turn():
    possible_comp_moves = []
    blah = see_if_win("computer_turn")
    if blah == None:  # No way for the computer to win
        for index in range(len(board_list)):
            if board_list[index] == " ":
                possible_comp_moves.append(index)  # adds the index for each possible move
        move_index = random.choice(possible_comp_moves)  # randomly chooses a possible move
        board_list[move_index] = comp_marker
        return update_board(board_list)
    else:
        return update_board(blah)


def see_if_win(mode="normal"):
    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7
    i = 8
    winlist = [(a, b, c), (d, e, f), (g, h, i), (a, d, g,), (b, e, h), (c, f, i), (a, e, i), (g, e, c)]
    if mode == "normal":
        for win_type in winlist:
            if board_list[win_type[0]] == board_list[win_type[1]] == board_list[win_type[2]]:
                if board_list[win_type[0]] in ["X", "O"]:
                    return board_list[win_type[0]]
    elif mode == "computer_turn":
        for win_type in winlist:
            if (board_list[win_type[0]] == board_list[win_type[1]]) and board_list[win_type[2]] == " " and board_list[
                win_type[0]] == comp_marker:
                board_list[win_type[2]] = comp_marker
                return board_list
            elif (board_list[win_type[0]] == board_list[win_type[2]]) and board_list[win_type[1]] == " " and board_list[
                win_type[0]] == comp_marker:
                board_list[win_type[1]] = comp_marker
                return board_list
            elif (board_list[win_type[1]] == board_list[win_type[2]]) and board_list[win_type[0]] == " " and board_list[
                win_type[1]] == comp_marker:
                board_list[win_type[0]] = comp_marker
                return board_list
        for win_type in winlist:
            if (board_list[win_type[0]] == board_list[win_type[1]]) and board_list[win_type[2]] == " " and board_list[
                win_type[0]] == marker:
                board_list[win_type[2]] = comp_marker
                return board_list
            elif (board_list[win_type[0]] == board_list[win_type[2]]) and board_list[win_type[1]] == " " and board_list[
                win_type[0]] == marker:
                board_list[win_type[1]] = comp_marker
                return board_list
            elif (board_list[win_type[1]] == board_list[win_type[2]]) and board_list[win_type[0]] == " " and board_list[
                win_type[1]] == marker:
                board_list[win_type[0]] = comp_marker
                return board_list
        return None


# PLAYER TURN
# board = player_turn("X")
def get_marker():
    marker = input("Chciałbyś mieć X lub O?: ")
    while marker not in ["X", "O", "x", "o"]:
        marker = input("Chciałbyś mieć X lub O?: ")
    print("Jesteś", marker.upper())
    if marker == "O":
        comp_marker = "X"
    else:
        comp_marker = "O"
    return marker, comp_marker


# Create an empty board
board = update_board(board_list)
# Menu to choose game type:
# PVP = player vs player
# PVC = player vs computer
menu = \
    '''Game modes
    (1) - Player vs. Player
    (2) - Player vs. Computer'''
print(menu)
game = input("Wybierz numer z menu: ")
if game == "1":
    game = "PVP"
elif game == "2":
    game = "PVC"
# Part of the loops; keep playing while no one has won
win = None
if game == "PVP":
    again = 1
    while again == 1:
        marker, comp_marker = get_marker()
        turn = "player"
        while win == None:
            if " " not in board_list:
                break
            if turn == "player":
                board = player_turn(marker)
                turn = "computer"
            elif turn == "computer":
                board = player_turn(comp_marker)
                turn = "player"
            win = see_if_win()
        print(board)
        if win != None:
            print("%s won!" % (win))
        else:
            print("Nie ma więcej ruchów. REMIS!")
        while again not in ["y", "n"]:
            again = input("Chciałbyś zagrać jeszcze raz? (y/n) ").lower()
        if again == "y":
            again = 1
            board_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            board = update_board(board_list)
elif game == "PVC":
    again = 1
    while again == 1:
        marker, comp_marker = get_marker()
        turn = "player"
        while win == None:
            if " " not in board_list:
                break
            if turn == "player":
                board = player_turn(marker)
                turn = "computer"
            elif turn == "computer":
                board = comp_turn()
                turn = "player"
            win = see_if_win()
        print(board)
        if win != None:
            print("%s wygrał!" % (win))
        else:
            print("Nie ma więcej ruchów. REMIS!")
        while again not in ["y", "n"]:
            again = input("Chciałbyś zagrać jeszcze raz? (y/n) ").lower()
        if again == "y":
            again = 1
            board_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
            board = update_board(board_list)
print("<Mam nadzieję, że dobrze się bawiłeś/aś grając w kółko i krzyżyk>.")