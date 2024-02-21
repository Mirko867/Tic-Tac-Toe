import pandas as pd
data = {
    "column": [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        }

tris_table = pd.DataFrame(data)
diagonal1 = tris_table['column'][0][0]+tris_table['column'][1][1]+tris_table['column'][2][2]
diagonal2 = tris_table['column'][0][2]+tris_table['column'][1][1]+tris_table['column'][2][0]
column1 = tris_table['column'][0][0]+tris_table['column'][1][0]+tris_table['column'][2][0]
column2 = tris_table['column'][0][1]+tris_table['column'][1][1]+tris_table['column'][2][1]
column3 = tris_table['column'][0][2]+tris_table['column'][1][2]+tris_table['column'][2][2]

global tie_status

tie_status = False
winner_status = False

def check_winner(table, x, y, c1, c2, c3):
    if c1 != 3 and c1 != 15 and c2 != 3 and c2 != 15 and c3 != 3 and c3 != 15:
        for n in range(0,3):
            print(sum(table['column'][n]))
            if sum(table['column'][n]) == 3:
                return "A"
            elif  sum(table['column'][n]) == 15:
                return "B"
            else:
                if x == 3:
                    return "A"
                elif y == 3:
                    return "A"
                elif x == 15:
                    return "B"
                elif y == 15:
                    return "B"
                else:
                    return "C"
    else:
        if c1 == 3:
            return "A"
        elif c2 == 3:
            return "A"
        elif c3 == 3:
            return "A"
        elif c1 == 15:
            return "B"
        elif c2 == 15:
            return "B"
        elif c3 == 15:
            return "B"
        else:
            return "C"

def check_tie(table):
    if 0 not in table['column'][0] and 0 not in table['column'][1] and 0 not in table['column'][2]:
        return True
    else:
        return False


while tie_status == False and winner_status == False:
    print(tris_table)
    # winner = check_winner(table=tris_table, x=diagonal1, y=diagonal2, c1 = column1, c2 = column2, c3 =column3)
    # if winner != "A" and winner != "B":
    #     if check_tie(table=tris_table) == False:
    input_colum_player1 = int(input("Which column Player 1?"))
    input_row_player1 = int(input("Which row Player 1?"))
    tris_table['column'][input_row_player1][input_colum_player1] = 1
    print(tris_table)
    diagonal1 = tris_table[ 'column' ][ 0 ][ 0 ] + tris_table[ 'column' ][ 1 ][ 1 ] + \
                tris_table[ 'column' ][ 2 ][ 2 ]
    diagonal2 = tris_table[ 'column' ][ 0 ][ 2 ] + tris_table[ 'column' ][ 1 ][ 1 ] + \
                tris_table[ 'column' ][ 2 ][ 0 ]
    column1 = tris_table[ 'column' ][ 0 ][ 0 ] + tris_table[ 'column' ][ 1 ][ 0 ] + tris_table[ 'column' ][ 2 ][
        0 ]
    column2 = tris_table[ 'column' ][ 0 ][ 1 ] + tris_table[ 'column' ][ 1 ][ 1 ] + tris_table[ 'column' ][ 2 ][
        1 ]
    column3 = tris_table[ 'column' ][ 0 ][ 2 ] + tris_table[ 'column' ][ 1 ][ 2 ] + tris_table[ 'column' ][ 2 ][
        2 ]
    winner = check_winner(table=tris_table, x=diagonal1, y=diagonal2, c1 = column1, c2 = column2, c3 =column3)
    if winner == "A":
        print("Player A won!")
        winner_status = True
        break
    elif winner == "B":
        print("Player B won!")
        winner_status = True
        break
    else:
        tie_status = check_tie(table=tris_table)
        if tie_status == True:
            print("It is a tie")
            break
        else:
            pass

    input_colum_player2 = int(input("Which column Player 2?"))
    input_row_player2 = int(input("Which row Player 2?"))
    tris_table['column'][ input_row_player2 ][ input_colum_player2 ] = 5
    print(tris_table)
    diagonal1 = tris_table[ 'column' ][ 0 ][ 0 ] + tris_table[ 'column' ][ 1 ][ 1 ] + \
                tris_table[ 'column' ][ 2 ][ 2 ]
    diagonal2 = tris_table[ 'column' ][ 0 ][ 2 ] + tris_table[ 'column' ][ 1 ][ 1 ] + \
                tris_table[ 'column' ][ 2 ][ 0 ]
    column1 = tris_table[ 'column' ][ 0 ][ 0 ] + tris_table[ 'column' ][ 1 ][ 0 ] + tris_table[ 'column' ][ 2 ][
        0 ]
    column2 = tris_table[ 'column' ][ 0 ][ 1 ] + tris_table[ 'column' ][ 1 ][ 1 ] + tris_table[ 'column' ][ 2 ][
        1 ]
    column3 = tris_table[ 'column' ][ 0 ][ 2 ] + tris_table[ 'column' ][ 1 ][ 2 ] + tris_table[ 'column' ][ 2 ][
        2 ]
    winner = check_winner(table=tris_table, x=diagonal1, y=diagonal2, c1 = column1, c2 = column2, c3 =column3)
    if winner == "A":
        print("Player A won!")
        winner_status = True
    elif winner == "B":
        print("Player B won!")
        winner_status = True
    else:
        tie_status = check_tie(table=tris_table)
        if tie_status == True:
            print("it is a tie")
            break
        else:
            pass