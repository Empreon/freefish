import chess
import chess.polyglot

import random

from src.AI.Algorithm.NegamaxAlgorithm import moveSearch
from src.AI.Convert.FenConverter import fenConverter
from src.AI.Evaluate.BoardEvaluation import evaluation


class AI(object):

    def __init__(self, board):

        self.board = board
        x = board.legal_moves

    def f_legalmoves(self):
        return self.board.legal_moves

    def f_evaluate(self):
        return evaluation(self.board)

    def f_fenconvert(self, whiteDataList, blackDataList, whiteCastleData, blackCastleData, moveTurn):
        return fenConverter(whiteDataList, blackDataList, whiteCastleData, blackCastleData, moveTurn)

    def f_move_random(self):
        move_num = self.board.legal_moves.count()
        list_num = random.randint(0, move_num)
        random_movelist = []
        for move in self.board.legal_moves:
            random_movelist.append(move)
        return random_movelist[list_num]

    def f_bookmoves_custom(self):
        book = []
        bookmove = chess.polyglot.MemoryMappedReader(
            "C:\\Users\\hp\\Desktop\\Utku\\Python\\FreeFish\\src\\AI\\OpeningBook\\kasparov.bin").weighted_choice(self.board).move
        book.append(bookmove)
        return book

    def f_move_lvl_1(self):
        depth = 1
        goodMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in self.board.legal_moves:
            self.board.push(move)
            boardValue = -moveSearch(self.board, depth - 1, -alpha, -beta, self.board.turn)
            if boardValue > bestValue:
                bestValue = boardValue
                goodMove = move
            if boardValue > alpha:
                alpha = boardValue
            self.board.pop()
        return goodMove

    def f_move_lvl_3(self):
        depth = 3
        goodMove = chess.Move.null()
        bestValue = -99999
        alpha = -100000
        beta = 100000
        for move in self.board.legal_moves:
            self.board.push(move)
            boardValue = -moveSearch(self.board, depth - 1, -alpha, -beta, self.board.turn)
            if boardValue > bestValue:
                bestValue = boardValue
                goodMove = move
            if boardValue > alpha:
                alpha = boardValue
            self.board.pop()
        return goodMove

    def f_move_lvl_5(self):
        try:
            bookMoveList = self.f_bookmoves_custom()
            return bookMoveList[0]
        except:
            depth = 5
            goodMove = chess.Move.null()
            bestValue = -99999
            alpha = -100000
            beta = 100000
            for move in self.board.legal_moves:
                self.board.push(move)
                boardValue = -moveSearch(self.board, depth - 1, -alpha, -beta, self.board.turn)
                if boardValue > bestValue:
                    bestValue = boardValue
                    goodMove = move
                if boardValue > alpha:
                    alpha = boardValue
                self.board.pop()
            return goodMove

    def f_move_lvl_7(self):
        try:
            bookMoveList = self.f_bookmoves_custom()
            return bookMoveList[0]
        except:
            depth = 7
            goodMove = chess.Move.null()
            bestValue = -99999
            alpha = -100000
            beta = 100000
            for move in self.board.legal_moves:
                self.board.push(move)
                boardValue = -moveSearch(self.board, depth - 1, -alpha, -beta, self.board.turn)
                if boardValue > bestValue:
                    bestValue = boardValue
                    goodMove = move
                if boardValue > alpha:
                    alpha = boardValue
                self.board.pop()
            return goodMove