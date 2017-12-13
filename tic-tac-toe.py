import os


# funkcja czyszcząca ekran
def clear():
    os.system('cls')

def play():

    finish = 0
    mark_O = ''
    mark_X = ''
    count = 0
    checked = {'A1': 0, 'A2': 0, 'A3': 0, 'B1': 0, 'B2': 0, 'B3': 0, 'C1': 0, 'C2': 0, 'C3': 0}

    L_ABC = {'A': '   A   ', 'B': '    B   ', 'C': '    C   '}
    L_123 = {'1': '1', '2': '2', '3': '3'}
    board1 = {'A1_1': '       |', 'B1_1': '       |', 'C1_1': '        ', 'A1_2': '       |', 'B1_2': '       |',
              'C1_2': '        ', 'A1_3': '_______|', 'B1_3': '_______|', 'C1_3': '_______'}
    board2 = {'A2_1': '       |', 'B2_1': '       |', 'C2_1': '        ', 'A2_2': '       |', 'B2_2': '       |',
              'C2_2': '        ', 'A2_3': '_______|', 'B2_3': '_______|', 'C2_3': '_______'}
    board3 = {'A3_1': '       |', 'B3_1': '       |', 'C3_1': '        ', 'A3_2': '       |', 'B3_2': '       |',
              'C3_2': '        ', 'A3_3': '       |', 'B3_3': '       |', 'C3_3': '       '}




    # funkcja rysująca tablicę
    def print_board():
        print(' ' + L_ABC['A'] + L_ABC['B'] + L_ABC['C'])
        print(' ' + board1['A1_1'] + board1['B1_1'] + board1['C1_1'] + '\n' + L_123['1'] + board1['A1_2'] + board1[
            'B1_2'] +
              board1['C1_2'] + '\n' + ' ' + board1['A1_3'] + board1['B1_3'] + board1['C1_3'])
        print(' ' + board2['A2_1'] + board2['B2_1'] + board2['C2_1'] + '\n' + L_123['2'] + board2['A2_2'] + board2[
            'B2_2'] +
              board2['C2_2'] + '\n' + ' ' + board2['A2_3'] + board2['B2_3'] + board2['C2_3'])
        print(' ' + board3['A3_1'] + board3['B3_1'] + board3['C3_1'] + '\n' + L_123['3'] + board3['A3_2'] + board3[
            'B3_2'] +
              board3['C3_2'] + '\n' + ' ' + board3['A3_3'] + board3['B3_3'] + board3['C3_3'])

    # funkcja wprowadzająca znaki do tablicy od gracza O
    def modify_board_O():
        if mark_O == 'A1':
            board1['A1_2'] = '   O   |'
            checked['A1'] = 1
        elif mark_O == 'B1':
            board1['B1_2'] = '   O   |'
            checked['B1'] = 1
        elif mark_O == 'C1':
            board1['C1_2'] = '   O   '
            checked['C1'] = 1
        elif mark_O == 'A2':
            board2['A2_2'] = '   O   |'
            checked['A2'] = 1
        elif mark_O == 'B2':
            board2['B2_2'] = '   O   |'
            checked['B2'] = 1
        elif mark_O == 'C2':
            board2['C2_2'] = '   O   '
            checked['C2'] = 1
        elif mark_O == 'A3':
            board3['A3_2'] = '   O   |'
            checked['A3'] = 1
        elif mark_O == 'B3':
            board3['B3_2'] = '   O   |'
            checked['B3'] = 1
        elif mark_O == 'C3':
            board3['C3_2'] = '   O   '
            checked['C3'] = 1

    # funkcja wprowadzająca znaki do tablicy od gracza X
    def modify_board_X():
        if mark_X == 'A1':
            board1['A1_2'] = '   X   |'
            checked['A1'] = 1
        elif mark_X == 'B1':
            board1['B1_2'] = '   X   |'
            checked['B1'] = 1
        elif mark_X == 'C1':
            board1['C1_2'] = '   X   '
            checked['C1'] = 1
        elif mark_X == 'A2':
            board2['A2_2'] = '   X   |'
            checked['A2'] = 1
        elif mark_X == 'B2':
            board2['B2_2'] = '   X   |'
            checked['B2'] = 1
        elif mark_X == 'C2':
            board2['C2_2'] = '   X   '
            checked['C2'] = 1
        elif mark_X == 'A3':
            board3['A3_2'] = '   X   |'
            checked['A3'] = 1
        elif mark_X == 'B3':
            board3['B3_2'] = '   X   |'
            checked['B3'] = 1
        elif mark_X == 'C3':
            board3['C3_2'] = '   X   '
            checked['C3'] = 1

    clear()

    print_board()

    while (finish != 1):
        print('Player O, insert value: ')
        mark_O = str(input()).upper()
        while mark_O != 'A1'and mark_O != 'A2' and mark_O != 'A3' and mark_O != 'B1' and mark_O != 'B2' and mark_O != 'B3' and mark_O != 'C1' and mark_O != 'C2' and mark_O != 'C3':
            print('Wrong value, insert again: ')
            mark_O = str(input()).upper()
        while checked[mark_O] == 1:
            print('Wrong, value is already checked!')
            mark_O = str(input()).upper()
        modify_board_O()
        clear()
        print_board()
        count += 1

        if (board1['A1_2'] == '   O   |' and board1['B1_2'] == '   O   |' and board1['C1_2'] == '   O   ')\
        or (board2['A2_2'] == '   O   |' and board2['B2_2'] == '   O   |' and board2['C2_2'] == '   O   ')\
        or (board3['A3_2'] == '   O   |' and board3['B3_2'] == '   O   |' and board3['C3_2'] == '   O   ')\
        or (board1['A1_2'] == '   O   |' and board2['A2_2'] == '   O   |' and board3['A3_2'] == '   O   |')\
        or (board1['B1_2'] == '   O   |' and board2['B2_2'] == '   O   |' and board3['B3_2'] == '   O   |')\
        or (board1['C1_2'] == '   O   ' and board2['C2_2'] == '   O   ' and board3['C3_2'] == '   O   ')\
        or (board1['A1_2'] == '   O   |' and board2['B2_2'] == '   O   |' and board3['C3_2'] == '   O   ')\
        or (board1['C1_2'] == '   O   ' and board2['B2_2'] == '   O   |' and board3['A3_2'] == '   O   |'):
            print('PLAYER O WIN!!!')
            finish = 1
            break
        # licznik sprawdzający ile znaków zostało narysowanych na tablicy
        if count == 9 and finish == 0:
            print('Play is END but nobody wins!')
            break

        print('Player X, insert value: ')
        mark_X = input().upper()
        while mark_X != 'A1'and mark_X != 'A2' and mark_X != 'A3' and mark_X != 'B1' and mark_X != 'B2' and mark_X != 'B3' and mark_X != 'C1' and mark_X != 'C2' and mark_X != 'C3':
            print('Wrong value, insert again: ')
            mark_X = str(input()).upper()
        while checked[mark_X] == 1:
            print('Wrong, value is already checked!')
            mark_X = str(input()).upper()
        modify_board_X()
        clear()
        print_board()
        count += 1
        if (board1['A1_2'] == '   X   |' and board1['B1_2'] == '   X   |' and board1['C1_2'] == '   X   ')\
        or (board2['A2_2'] == '   X   |' and board2['B2_2'] == '   X   |' and board2['C2_2'] == '   X   ')\
        or (board3['A3_2'] == '   X   |' and board3['B3_2'] == '   X   |' and board3['C3_2'] == '   X   ')\
        or (board1['A1_2'] == '   X   |' and board2['A2_2'] == '   X   |' and board3['A3_2'] == '   X   |')\
        or (board1['B1_2'] == '   X   |' and board2['B2_2'] == '   X   |' and board3['B3_2'] == '   X   |')\
        or (board1['C1_2'] == '   X   ' and board2['C2_2'] == '   X   ' and board3['C3_2'] == '   X   ')\
        or (board1['A1_2'] == '   X   |' and board2['B2_2'] == '   X   |' and board3['C3_2'] == '   X   ')\
        or (board1['C1_2'] == '   X   ' and board2['B2_2'] == '   X   |' and board3['A3_2'] == '   X   |'):
            print('PLAYER X WIN!!!')
            finish = 1
            break
        if count == 9 and finish == 0 :
            print('Play is END but nobody wins!')
            break



print('HI! WELCOME IN TIC TAC TOE PLAY!')

play()

print('Finish? - 0, New Game - 1:')
check = int(input())
while check == 1:
    clear()
    play()
    print('Finish? - 0, New Game - 1:')
    check = int(input())







