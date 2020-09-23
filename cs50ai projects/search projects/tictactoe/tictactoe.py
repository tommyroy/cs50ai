import math
import copy

"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    num_o = 0
    num_x = 0

    for row in board:
        for cell in row:
            if cell == X:
                num_x += 1
            elif cell == O:
                num_o += 1

    if num_x > num_o:
        return O
    elif num_o == num_x and not terminal(board):
        return X
    else:
        return None

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    res = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                res.add((i, j))

    return res

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if terminal(board):
        raise ValueError("The game is over")
    elif action not in actions(board):
        raise ValueError("Different action not allowed")
    else:
        val_player = player(board)
        co_board = copy.deepcopy(board)
        (i, j) = action
        co_board[i][j] = val_player

    return co_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[1][0] == board[1][1] == board[1][2] != None:
        if board[1][0] == X:
            return X
        else:
            return O
    elif board[2][0] == board[2][1] == board[2][2] != None:
        if board[2][0] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][0] == board[2][0] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][1] == board[1][1] == board[2][1] != None:
        if board[0][1] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][2] == board[2][2] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    elif board[0][0] == board[1][1] == board[2][2] != None:
        if board[0][0] == X:
            return X
        else:
            return O
    elif board[0][2] == board[1][1] == board[2][0] != None:
        if board[0][2] == X:
            return X
        else:
            return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #check if anyone won

    if winner(board) != None:
        return True

    #find if all cells are filled
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maxValue(board):
        if terminal(board):
            return utility(board)
        v = float("-inf")
        for action in actions(board):
            v = max(v, minValue(result(board, action)))

        return v

    def minValue(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v, maxValue(result(board, action)))

        return v

    p = player(board)

    if board == [[EMPTY] * 3] * 3:
        return (0, 0)

    if p == X:
        v = -math.inf
        ret_action = None
        for action in actions(board):
            minValueAction = minValue(result(board, action))
            if minValueAction > v:
                v = minValueAction
                ret_action = action

    if p == O:
        v = math.inf
        ret_action = None
        for action in actions(board):
            maxValueAction = maxValue(result(board, action))
            if maxValueAction < v:
                v = maxValueAction
                ret_action = action

    return ret_action

