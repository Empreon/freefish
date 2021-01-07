import chess
from PieceData import pieceDataBase

board = chess.Board('8/8/1pk2p2/p2p2pp/P2Pp3/1PP1K1P1/5P1P/8 w - - 0 1')

moveData = []
moveValueData = []
z = []


# https:// www.geeksforgeeks.org / python - program - to - find - smallest - number - in -a - list /
def evaluation():
    # https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec
    wp = len(board.pieces(chess.PAWN, chess.WHITE))
    bp = len(board.pieces(chess.PAWN, chess.BLACK))
    wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
    bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
    wb = len(board.pieces(chess.BISHOP, chess.WHITE))
    bb = len(board.pieces(chess.BISHOP, chess.BLACK))
    wr = len(board.pieces(chess.ROOK, chess.WHITE))
    br = len(board.pieces(chess.ROOK, chess.BLACK))
    wq = len(board.pieces(chess.QUEEN, chess.WHITE))
    bq = len(board.pieces(chess.QUEEN, chess.BLACK))

    material = pieceDataBase.pawnValue * (wp - bp) + \
               pieceDataBase.kingValue * (wn - bn) + \
               pieceDataBase.bishopValue * (wb - bb) + \
               pieceDataBase.rookValue * (wr - br) + \
               pieceDataBase.queenValue * (wq - bq)

    if board.turn:
        return material
    else:
        return -material


# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
def keywithmaxval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def minimaxDeneme():
    for firstMove in board.legal_moves:
        board.push(firstMove)
        moveData.append(firstMove)
        for secondMove in board.legal_moves:
            board.push(secondMove)
            if board.is_game_over():
                z.append(-9999)
                board.pop()
            else:
                z.append(evaluation())
                board.pop()
        if board.is_game_over():
            moveValueData.append(9999)
            board.pop()
        else:
            board.pop()
            moveValueData.append(min(z))

    moveDict = dict(zip(moveData, moveValueData))
    bestMove = keywithmaxval(moveDict)
    print(moveDict)
    print(bestMove)

    return bestMove
