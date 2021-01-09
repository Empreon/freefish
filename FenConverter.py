def fenConverter():
    # Pieces Locations
    whitePiecesData = input(print("Enter the white pieces data..."))
    blackPiecesData = input(print("Enter the black pieces data..."))

    # Castle Data
    whiteCastleData = input(print("If white has a castle, enter 1. If not, enter 0."))
    blackCastleData = input(print("If black has a castle, enter 1. If not, enter 0."))

    # Move Turn
    moveTurn = input(print("If its white turn, enter 1. If not, enter 0"))

    # List
    whiteDataList = list(whitePiecesData.split(" "))
    blackDataList = list(blackPiecesData.split(" "))

    # Board & Pieces Original Notation
    boardVerticalNotation = ["a", "b", "c", "d", "e", "f", "g", "h"]
    boardHorizontalNotation = ["1", "2", "3", "4", "5", "6", "7", "8"]
    chessOriginalNotation = ["K", "Q", "R", "B", "N", ""]

    # Values
    differentPieceNumber = len(chessOriginalNotation)
    numberVerticalLine = len(boardVerticalNotation)
    numberHorizontalLine = len(boardHorizontalNotation)

    # Pieces Fen Notation
    whiteFenNotation = {"K": "K", "Q": "Q", "R": "R", "B": "B", "N": "N", "": "P"}
    blackFenNotation = {"K": "k", "Q": "q", "R": "r", "B": "b", "N": "n", "": "p"}

    # Fen Data List
    boardDataList = []

    # Fen, Space Calculater
    def fenSpaceCalculater():
        spaceNumber = 0
        while "Space" in boardDataList:
            boardDataList.remove("Space")
            spaceNumber = spaceNumber + 1
        if spaceNumber != 0:
            spaceNumberStr = str(spaceNumber)
            boardDataList.append(spaceNumberStr)
        else:
            return

    # Fen, Notation Writer
    def fenNotationWriter(x):
        pieceFindNumber = 0
        for pieceType in range(differentPieceNumber):
            pieceKind = chessOriginalNotation[pieceType]
            whitePieceKind = whiteFenNotation[pieceKind]
            blackPieceKind = blackFenNotation[pieceKind]
            if pieceKind + x in whiteDataList:
                fenSpaceCalculater()
                boardDataList.append(whitePieceKind)
                pieceFindNumber = pieceFindNumber + 1
            if pieceKind + x in blackDataList:
                fenSpaceCalculater()
                boardDataList.append(blackPieceKind)
                pieceFindNumber = pieceFindNumber + 1
        if pieceFindNumber == 0:
            boardDataList.append("Space")

    # Fen, Notation Write
    for horizontalLine in range(numberHorizontalLine):
        horizontalLineNumber = numberHorizontalLine - horizontalLine
        horizontalLineNumberStr = str(horizontalLineNumber)
        for verticalLine in range(numberVerticalLine):
            verticalLineLetter = boardVerticalNotation[verticalLine]
            fenNotationWriter(verticalLineLetter + horizontalLineNumberStr)
        fenSpaceCalculater()
        if horizontalLine != 7:
            boardDataList.append("/")

    # Fen, Move Turn Write
    if moveTurn[0] == "1":
        boardDataList.append(" w")
    if moveTurn[0] == "0":
        boardDataList.append(" b")
    else:
        pass

    # Fen, Castle Data Write
    if whiteCastleData[0] == "1":
        boardDataList.append(" KQ")
    if blackCastleData[0] == "1" and whiteCastleData[0] == "0":
        boardDataList.append(" kq")
    if blackCastleData[0] == "1" and whiteCastleData[0] == "1":
        boardDataList.append("kq")
    if whiteCastleData[0] == "0" and blackCastleData[0] == "0":
        boardDataList.append(" -")
    else:
        pass

    # List to String
    # https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
    boardFenNotation = ''.join(str(fenData) for fenData in boardDataList)

    return boardFenNotation
