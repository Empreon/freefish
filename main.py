from Algorithm.MinMaxAlgorithm import moveSearch

import chess
import chess.polyglot

class ChessAI:
    def __init__(self, depth=3, book_path='OpeningBook/kasparov.bin'):
        self.depth = depth
        self.book = chess.polyglot.open_reader(book_path) if book_path else None

    def get_book_move(self, board):
        try:
            return self.book.weighted_choice(board).move
        except (IndexError, KeyError, AttributeError):
            return None

    def get_best_move(self, board):
        try:
            book_move_list = self.get_book_move(board)
            return book_move_list[0]
        except:
            depth = 7
            good_move = chess.Move.null()
            best_value = -99999
            alpha = -100000
            beta = 100000
            for move in board.legal_moves:
                board.push(move)
                board_value = -moveSearch(board, depth - 1, -alpha, -beta, board.turn)
                if board_value > best_value:
                    best_value = board_value
                    good_move = move
                if board_value > alpha:
                    alpha = board_value
                board.pop()
            return good_move


def display_board(board):
    print("\n" + board.unicode(borders=True, invert_color=True))
    print(f"FEN: {board.fen()}\n")


def main():
    engine = ChessAI(book_path='OpeningBook/kasparov.bin')

    while True:
        fen = input("Enter FEN or press Enter: ").strip()
        board = chess.Board(fen) if fen else chess.Board()

        display_board(board)

        if board.is_game_over():
            print("Game Over")
            continue

        best_move = engine.get_best_move(board)
        print(f"Best Move: {best_move.uci()}")

        board.push(best_move)
        print("\nNew Position:")
        display_board(board)

if __name__ == "__main__":
    main()
