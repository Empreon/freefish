# Freefish

A terminal-based chess AI implementing minimax algorithm with alpha-beta pruning and custom evaluation functions.

## Features
**Core Algorithms**
- Minimax decision-making with alpha-beta pruning optimization
- Piece-square table evaluation using custom .npz data files
- Opening book integration (Kasparov's preferred openings)

**Terminal Interface**
- FEN notation input/output
- ASCII board visualization
- Best move recommendation system

## Requirements
- Python 3.9+
- numpy
- python-chess

## Installation
```
git clone https://github.com/Empreon/Freefish.git
pip install -r requirements.txt
```

## Usage
1. Run the engine:
2. Input FEN notation when prompted:
3. Receive AI analysis:
- Best move in algebraic notation
- Resulting FEN position
- ASCII board visualization

## Customization
**NPZ Generator**
- Modify piece-square tables using `NPZGenerator.py`

**Opening Book**
- Replace `kasparov.bin` with alternative opening books
- Ensure binary opening books are in `/OpeningBooks` directory

## Project History
Originally developed in 2021 as a learning project for:
- Game theory algorithms
- Chess AI fundamentals
- Python optimization techniques

