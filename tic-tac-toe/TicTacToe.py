import random

def main():
    
    status = "no win"
    grid = list(range(9))
    for x in range(len(grid)):
        grid[x] = str(grid[x])
    #print (grid)
    player_turn = "X"
    turn_num = 1
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    difficulty = difficulty_selection()
    
    while turn_num < 10:
        game(grid)
        while True and player_turn == "X":
            placement = input("player %s, please enter a number from the grid above to place your letter." % player_turn)
            if placement.isdigit() == True:
                placement = int(placement)
                if placement >= 0 and placement < 10:
                    if str(grid[placement]).isdigit() == True:
                        grid[placement] = player_turn
                        break
            game(grid)
            print("please enter a valid digit from the grid above.")
        
        if player_turn == "O":
            
            play_best_move_chance = random.randint(1,100)
            #print(play_best_move_chance)
            if play_best_move_chance <= difficulty:
                cornerstest = corneropen(grid)
                win_move = check_win_move(grid, wins)
                #print (win_move)
                if grid[4] == '4':
                    grid[4] = "O"
                elif win_move[0] == True:
                    grid[win_move[1]] ="O"
                
                elif cornerstest[0] == True:
                    grid[cornerstest[1]] = "O"
                else:
                    edgesopen = edgetest(grid)
                    grid[edgesopen] = "O"
            else:
                random_move = play_random(grid)
                grid[random_move] = "O"
        
        game(grid)
    
        status = checkwinner(grid, wins)
        if status == "win":
            print("%s is the WINNER!" % player_turn)
            return 0
        else:
            player_turn = swapturns(player_turn)
        
        turn_num += 1

    print("Tie Game!")

def game(grid):
    print(grid[0:3])
    print(grid[3:6])
    print(grid[6:9])
    print("\n")

def checkwinner(grid, wins):
    for x in range(len(wins)):
        test1 = grid[wins[x][0]]
        test2 = grid[wins[x][1]]
        test3 = grid[wins[x][2]]
        if test1 == test2 and test2 == test3:
            return "win"
    return "no win"
    
def swapturns(player_turn):
    if player_turn == "X":
        player_turn = "O"
    else:
        player_turn = "X"
    return player_turn
    
def corneropen(grid):
    opencorners = []
    testcorners = [0, 2, 6, 8]
    for x in range(len(testcorners)):
        if str(grid[testcorners[x]]).isdigit() == True:
            opencorners.append(testcorners[x])
    if len(opencorners) > 0:
        rand = random.choice(opencorners)
        return [True, rand]
    else:
        return [False, False]

def edgetest(grid):
    openedges = []
    testedges = [1, 3, 5, 7]
    for x in range(len(testedges)):
        if str(grid[testedges[x]]).isdigit() == True:
            openedges.append(testedges[x])
    if len(openedges) > 0:
        rand = random.choice(openedges)
        return rand
    else:
        return False

def check_win_move(grid, wins):
    possible_wins = []
    winning_moves = []
    losing_moves = []
    for x in range(len(wins)):
        test1 = grid[wins[x][0]]
        test2 = grid[wins[x][1]]
        test3 = grid[wins[x][2]]
        if test1 == test2 or test2 == test3 or test1 == test3:
            possible_wins.append(wins[x])
    #print (possible_wins)
    #print (winning_moves)
    #print (losing_moves)
    if len(possible_wins) > 0:
        for x in range(len(possible_wins)):
            xcount = 0
            ocount = 0
            for y in range(len(possible_wins[x])):
                if grid[possible_wins[x][y]] == "X":
                    xcount += 1
                if grid[possible_wins[x][y]] == "O":
                    ocount += 1
            if xcount == 0:
                winning_moves.append(possible_wins[x])
            if ocount == 0:
                losing_moves.append(possible_wins[x])
        if len(winning_moves) > 0:
            #print (winning_moves[0])
            for x in range(len(winning_moves)):
                for y in range(len(winning_moves[x])):
                    #print(grid[winning_moves[x][y]])
                    if grid[winning_moves[x][y]].isdigit() == True:
                        move = winning_moves[x][y]
                        return [True, move]
        if len(losing_moves) > 0:
            #print (losing_moves[0])
            for x in range(len(losing_moves)):
                for y in range(len(losing_moves[x])):
                    #print(grid[losing_moves[x][y]])
                    if grid[losing_moves[x][y]].isdigit() == True:
                        move = losing_moves[x][y]
                        return [True, move]
        return [False, False]
    else:
        return [False, False]
    
def difficulty_selection():
    while True:
        difficulty_response = input("please select a difficulty level: EASY, MEDIUM, HARD, IMPOSSIBLE")
        difficulty_options={
            "EASY": 25,
            "MEDIUM": 50,
            "HARD": 75,
            "IMPOSSIBLE": 90
        }
        if difficulty_response in difficulty_options:
            return difficulty_options[difficulty_response]
        print("Invalid Choice")
    

def play_random(grid):
    open_spots = []
    for index, spot in enumerate(grid):
        if str(spot).isdigit() == True:
            open_spots.append(index)
    move = random.choice(open_spots)
    return move
    
if __name__ == '__main__':
    main()