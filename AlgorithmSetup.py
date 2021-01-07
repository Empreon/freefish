import chess

from PieceData import pieceDataBase

board = chess.Board("6k1/8/6K1/8/8/8/8/2R5 w - - 0 1")

# https:// www.geeksforgeeks.org / python - program - to - find - smallest - number - in -a - list /
def evaluation():
    # https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec
    if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
    if board.is_stalemate():
        return 0
    if board.is_insufficient_material():
        return 0

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

def keywithminval(d):
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(min(v))]

def minimaxMoveData(x):
    moveData = []
    for firstMove in x.legal_moves:
        moveData.append(firstMove)

    return moveData

def minimaxDeneme():
    y = len(minimaxMoveData(board))
    a = []
    b = minimaxMoveData(board)
    c = []
    for i in range(y):
        print(i)
        x = 0
        z = minimaxMoveData(board)
        board.push(z[i])
        if board.is_game_over():
            c.append(evaluation())
            x = x + 1
        for move in board.legal_moves:
            board.push(move)
            if board.is_game_over() and x == 0:
                c.append(evaluation())
                x = x + 1
            for move2 in board.legal_moves:
                board.push(move2)
                if board.is_game_over() and x == 0:
                    c.append(evaluation())
                    x = x + 1
                for move3 in board.legal_moves:
                    board.push(move3)
                    if board.is_game_over() and x == 0:
                        c.append(evaluation())
                        x = x + 1
                    for move4 in board.legal_moves:
                        board.push(move4)
                        if x == 0:
                            c.append(evaluation())
                        board.pop()
                    board.pop()
                board.pop()
            board.pop()
        board.pop()
        a.append(min(c))
        c.clear()

    baDict = dict(zip(b, a))
    goodMove = keywithmaxval(baDict)

    return goodMove