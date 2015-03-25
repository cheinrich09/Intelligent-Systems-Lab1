num_States = 0

#runs until one player loses. besides player, eval, and cutoff entry, can set whose turn is first and whether to print out the moves
def play(p1Knight1, p1Knight2, p2Knight1, p2Knight2, p1Eval, p2Eval, cutoff, turn, printout):
    while True:#break when someone loses
        if (turn == 1):
            move = best_move(p1Knight1, p1Knight2, p2Knight1, p2Knight2, p1Eval, p2Eval, cutoff)
            if (printout ==1):
                print "Player "+ repr(turn)+" to"
                print move
            p1Knight1 = move[0]
            p1Knight2 = move[1]
            turn = 2
            if (move == [[0,0],[0,0]]):
                break
        if (turn ==2):
            move = best_move(p2Knight1, p2Knight2, p1Knight1, p1Knight2, p2Eval, p1Eval, cutoff)
            if (printout ==1):
                print "Player "+ repr(turn)+" to"
                print move
            p2Knight1 = move[0]
            p2Knight2 = move[1]
            turn = 1
            if (move == [[0,0],[0,0]]):
                break
        else:
            turn = 1
    victory = "Player " + repr(turn) + " wins"
    return victory

#best move, enter in the knights as [x,y]
def best_move(pKnight1, pKnight2, oKnight1, oKnight2, pEval, oEval, cutoff):
    possible_moves=successors(pKnight1, pKnight2, oKnight1, oKnight2)
    current_best=[[0,0],[0,0]];
    if (len(possible_moves) == 0):
        return current_best
    alpha = float('-inf')
    beta = float('inf')
    for s in possible_moves:
        val = min_Value(oKnight1, oKnight2, s[0], s[1], oEval, pEval, alpha, beta, cutoff)
        #print val
        #if val > a, a = val
        if val > alpha:
            alpha = val
            current_best = s
            
        #if a>= B, return B
        #if alpha >= beta:
    global num_States
    num_States = num_States+ len(possible_moves)
    print repr(num_States) + " States Generated"
    num_States = 0
    return current_best

#pKnight = player knight, oKnight = opponent Knight
def max_Value(pKnight1, pKnight2, oKnight1, oKnight2, pEval, oEval, alpha, beta, cutoff):
    #if cutoff(state) cutoff after certain depth
    #print cutoff
    if (cutoff <= 0):
        if (pEval == 1):
            return pOptionOne(pKnight1, pKnight2)
        elif (pEval == 2):
            return pOptionTwo(pKnight1, pKnight2)
    possible_moves = successors(pKnight1, pKnight2, oKnight1, oKnight2)
    global num_States
    num_States = num_States + len(possible_moves);
    #for s in possible_moves:
     #   if s[0][0] < 1 or s[0][1] < 1 or s[1][0] < 1 or s[1][1] < 1 or s[0][0] != oKnight1[0] or s[0][0] != oKnight2[0] or s[1][0] != oKnight1[0] or s[1][0] != oKnight2[0]:
      #      possible_moves.remove(s) #remove any which are invalid
            #add posible to list of actual states
    #if list of actual states empty. return terminal
    if (len(possible_moves) == 0):
        return -1
        #return low negative number, so that min prioritizes while max avoids
    #return terminal
    #for s in successors(state)
    for s in possible_moves:
        #val = min(s,a,b)
        val = min_Value(oKnight1, oKnight2, s[0], s[1], oEval, pEval, alpha, beta, cutoff-1)
        #if val > a, a = val
        if val > alpha:
            alpha = val
        #if a>= B, return B
        if alpha >= beta:
            return beta
    return alpha

def min_Value(pKnight1, pKnight2, oKnight1, oKnight2, pEval, oEval, alpha, beta, cutoff):
    #if cutoff(state) cutoff after certain depth
    if (cutoff <= 0):
        if (pEval == 1):
            return pOptionOne(pKnight1, pKnight2)
        elif (pEval == 2):
            return pOptionTwo(pKnight1, pKnight2)
    possible_moves = successors(pKnight1, pKnight2, oKnight1, oKnight2)
    global num_States
    num_States = num_States + len(possible_moves);
    #print possible_moves
    #for s in possible_moves:
     #   if s[0][0] < 1 or s[0][1] < 1 or s[1][0] < 1 or s[1][1] < 1 or s[0][0] != oKnight1[0] or s[0][0] != oKnight2[0] or s[1][0] != oKnight1[0] or s[1][0] != oKnight2[0]:
      #      possible_moves.remove(s)#remove any which are invalid
            #add posible to list of actual states
    #if list of actual states empty. return terminal
    if (len(possible_moves) == 0):
        return 1
        #return high positive number, so that max value will be interested in it, will be avoided by the min above it
    #return terminal
    #for s in successors(state)
    for s in possible_moves:
        #val = max(s,a,b)
        val = max_Value(oKnight1, oKnight2, s[0], s[1], oEval, pEval, alpha, beta, cutoff-1)
        #if val < B, B = val
        if val < beta:
            beta = val
        #if val < B, B = val
        if beta <= alpha:
            return alpha
    return beta

#returns successors
def successors(pKnight1, pKnight2, oKnight1, oKnight2):
    possible = []
    if(pKnight1[0]-1 > 0 and pKnight1[1]-2 > 0 and emptySpace(pKnight1[0]-1, pKnight1[1]-2, pKnight2,oKnight1, oKnight2)):
        possible.append([[pKnight1[0]-1, pKnight1[1]-2], pKnight2])
    if(pKnight1[0]+1 > 0 and pKnight1[1]-2 > 0 and emptySpace(pKnight1[0]+1, pKnight1[1]-2, pKnight2, oKnight1, oKnight2)):   
        possible.append([[pKnight1[0]+1, pKnight1[1]-2], pKnight2])
    if(pKnight1[0]-2 > 0 and pKnight1[1]-1 > 0 and emptySpace(pKnight1[0]-2, pKnight1[1]-1, pKnight2, oKnight1, oKnight2)): 
        possible.append([[pKnight1[0]-2, pKnight1[1]-1], pKnight2])
    if(pKnight1[0]-2 > 0 and pKnight1[1]+1 > 0 and emptySpace(pKnight1[0]-2, pKnight1[1]+1, pKnight2, oKnight1, oKnight2)):
        possible.append([[pKnight1[0]-2, pKnight1[1]+1], pKnight2])
    if(pKnight2[0]-1 > 0 and pKnight2[1]-2 > 0 and emptySpace(pKnight2[0]-1, pKnight2[1]-2, pKnight1, oKnight1, oKnight2)): 
        possible.append([pKnight1, [pKnight2[0]-1, pKnight2[1]-2]])
    if(pKnight2[0]+1 > 0 and pKnight2[1]-2 > 0 and emptySpace(pKnight2[0]+1, pKnight2[1]-2, pKnight1, oKnight1, oKnight2)): 
        possible.append([pKnight1, [pKnight2[0]+1, pKnight2[1]-2]])
    if(pKnight2[0]-2 > 0 and pKnight2[1]-1 > 0 and emptySpace(pKnight2[0]-2, pKnight2[1]-1, pKnight1, oKnight1, oKnight2)): 
        possible.append([pKnight1, [pKnight2[0]-2, pKnight2[1]-1]])
    if(pKnight2[0]-2 > 0 and pKnight2[1]+1 > 0 and emptySpace(pKnight1[0]-2, pKnight1[1]+1, pKnight2, oKnight1, oKnight2)): 
        possible.append([pKnight1, [pKnight2[0]-2, pKnight2[1]+1]])
    return possible

#checks to see if space empty
def emptySpace(x, y, pKnight2,oKnight1, oKnight2):
    if(oKnight1[0] == x and oKnight1[1] == y):
        return False
    if(oKnight2[0] == x and oKnight2[1] == y):
        return False
    if(pKnight2[0] == x and pKnight2[1] == y):
        return False
    return True

#pruning option 1(evaluation function) distance to origin
def pOptionOne(pKnight1, pKnight2):
    import math
    k1 = math.sqrt(pow(pKnight1[0], 2)+ pow(pKnight1[1], 2))
    k2 = math.sqrt(pow(pKnight2[0], 2)+ pow(pKnight2[1], 2))
    #print k1
    #print k2
    if k1 > k2:
        return -k1 #returning Negative leads to it prefering the farthest one
    else:
        return -k2
    
#pruning option 2(evaluation function)  distance between knights  
def pOptionTwo(pKnight1, pKnight2):
    import math
    k = math.sqrt(pow((pKnight2[0]-pKnight1[0]), 2) +pow((pKnight2[1]-pKnight1[1]), 2))
    return k
