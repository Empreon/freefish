import numpy as np

# https: // www.chessprogramming.org / Simplified_Evaluation_Function
P = np.array( [0, 0, 0, 0, 0, 0, 0, 0,
               50, 50, 50, 50, 50, 50, 50, 50,
               10, 10, 20, 30, 30, 20, 10, 10,
               5, 5, 10, 25, 25, 10, 5, 5,
               -20, -20, 0, 20, 20, 0, -20, -20,
               -15, -15, -10, 0, 0, -10, -15, -15,
               5, 10, 10, -20, -20, 10, 10, 5,
               0, 0, 0, 0, 0, 0, 0, 0])

N = np.array( [-50, -40, -30, -30, -30, -30, -40, -50,
               -40, -20, 0, 0, 0, 0, -20, -40,
               -30, 0, 10, 15, 15, 10, 0, -30,
               -30, 5, 15, 20, 20, 15, 5, -30,
               -30, 0, 15, 20, 20, 15, 0, -30,
               -30, 5, 10, 15, 15, 10, 5, -30,
               -40, -20, 0, 5, 5, 0, -20, -40,
               -50, -40, -30, -30, -30, -30, -40, -50, ])

B = np.array( [-20, -10, -10, -10, -10, -10, -10, -20,
               -10, 0, 0, 0, 0, 0, 0, -10,
               -10, 0, 5, 10, 10, 5, 0, -10,
               -10, 5, 5, 10, 10, 5, 5, -10,
               -10, 0, 10, 10, 10, 10, 0, -10,
               -10, 10, 10, 10, 10, 10, 10, -10,
               -10, 5, 0, 0, 0, 0, 5, -10,
               -20, -10, -10, -10, -10, -10, -10, -20, ])

R = np.array( [0, 0, 0, 0, 0, 0, 0, 0,
               5, 10, 10, 10, 10, 10, 10, 5,
               -5, 0, 0, 0, 0, 0, 0, -5,
               -5, 0, 0, 0, 0, 0, 0, -5,
               -5, 0, 0, 0, 0, 0, 0, -5,
               -5, 0, 0, 0, 0, 0, 0, -5,
               -5, 0, 0, 0, 0, 0, 0, -5,
               0, 0, 0, 5, 5, 0, 0, 0])

Q = np.array( [-20, -10, -10, -5, -5, -10, -10, -20,
               -10, 0, 0, 0, 0, 0, 0, -10,
               -10, 0, 5, 5, 5, 5, 0, -10,
               -5, 0, 5, 5, 5, 5, 0, -5,
               0, 0, 5, 5, 5, 5, 0, -5,
               -10, 5, 5, 5, 5, 5, 0, -10,
               -10, 0, 5, 0, 0, 0, 0, -10,
               -20, -10, -10, -5, -5, -10, -10, -20])

K = np.array( [-30, -40, -40, -50, -50, -40, -40, -30,
               -30, -40, -40, -50, -50, -40, -40, -30,
               -30, -40, -40, -50, -50, -40, -40, -30,
               -30, -40, -40, -50, -50, -40, -40, -30,
               -20, -30, -30, -40, -40, -30, -30, -20,
               -10, -20, -20, -20, -20, -20, -20, -10,
               20, 20, 0, 0, 0, 0, 20, 20,
               20, 30, 10, 0, 0, 10, 30, 20])

if __name__ == "__main__":
    np.savez_compressed('piece_sq_tables.npz', P=P, N=N, B=B, R=R, Q=Q, K=K)