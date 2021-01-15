import chess
import chess.polyglot

from BoardEvaluation_1 import evaluation

# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

def keywithminval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(min(v))]

def bookMoves(board):
    book = []
    bookmove = chess.polyglot.MemoryMappedReader("kasparov.bin").weighted_choice(board).move
    book.append(bookmove)
    return book

# https://www.youtube.com/watch?v=l-hh51ncgDI
def minimaxDeneme(board, depth, alpha, beta, turn):
    if depth == 0 or board.is_game_over():
        return evaluation(board)
    if turn:
        maxValue = -9999
        for whiteMove in board.legal_moves:
            board.push(whiteMove)
            value = minimaxDeneme(board, depth - 1, alpha, beta, False)
            board.pop()
            maxValue = max(maxValue, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return maxValue
    else:
        minValue = 9999
        for blackMove in board.legal_moves:
            board.push(blackMove)
            value = minimaxDeneme(board, depth - 1, alpha, beta, True)
            board.pop()
            minValue = min(minValue, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return minValue

# https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec
def moveSelect(board, depth):
    try:
        bookMoveList = bookMoves(board)
        print("move from book")
        return bookMoveList[0]
    except:
        goodMove = chess.Move.null()
        bestValue = -9999
        alpha = -10000
        beta = 10000
        print("move from code")
        for codemove in board.legal_moves:
            board.push(codemove)
            boardValue = minimaxDeneme(board, depth - 1, alpha, beta, board.turn)
            if boardValue > bestValue:
                bestValue = boardValue
                goodMove = codemove
            if boardValue > alpha:
                alpha = boardValue
            board.pop()
        return goodMove

chessboard = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
