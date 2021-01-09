import chess
import chess.polyglot

from BoardEvaluation_1 import evaluation

board = chess.Board("2k5/8/3K4/8/8/8/8/7R w - - 0 1")

def minimaxMoveData(x):
    moveData = []
    for firstMove in x.legal_moves:
        moveData.append(firstMove)

    return moveData

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

def keywithminval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(min(v))]

def moveDeneme(move, list):
    board.push(move)
    if board.is_game_over():
        list.append(evaluation(board))

def minimaxDeneme():
    a = []
    b = minimaxMoveData(board)
    c = []
    for move0 in board.legal_moves:
        moveDeneme(move0, c)
        if not board.is_game_over():
            for move1 in board.legal_moves:
                moveDeneme(move1, c)
                if not board.is_game_over():
                    for move2 in board.legal_moves:
                        moveDeneme(move2, c)
                        if not board.is_game_over():
                            for move3 in board.legal_moves:
                                moveDeneme(move3, c)
                                if not board.is_game_over():
                                    for move4 in board.legal_moves:
                                        board.push(move4)
                                        c.append(evaluation(board))
                                        board.pop()
                                board.pop()
                        board.pop()
                board.pop()
        board.pop()

        a.append(min(c))
        c.clear()

    baDict = dict(zip(b, a))

    return baDict

def bookMove():
    book = []
    move = chess.polyglot.MemoryMappedReader("kasparov.bin").weighted_choice(board).move
    book.append(move)

    return book


def moveSelect():
    try:
        bookMoveList = bookMove()
        return bookMoveList[0]
    except:
        print("move from algorithm")
        maxMove = keywithmaxval(minimaxDeneme())
        return maxMove
