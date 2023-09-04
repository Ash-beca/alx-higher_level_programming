#!/usr/bin/python3
import sys
""" Python3 program to solve N Queen"""
 
N = 4
 
 
def nqueens(N):
     for i in range(N):
        for j in range(N):
            if N[i][j] == 1:
                print(N[i][j],end=" ")
        print()

def backtrack(row, num, col, pd, nd):
    """ Recursive function. """
    global board
    if row == num:  
        print(nqueens()) 
        return

    for i in range(num):
        if i in col or (row + i) in pd or (row - i) in nd:
            continue

        """adding new row combination"""
        col.add(i)
        pd.add(row + i)
        nd.add(row - i)
    
        board[row][i] = 1

        backtrack(row + 1, num, col, pd, nd)
        """ 
        backtracking happens when a queen can't be placed in any empty column 
        when a previous queen is moved hence it need to be resetted to 0, below code
        will indicate that board is updated to 0 to indicate that a queen
        is no longer in that position 
        
        """
        col.remove(i)
        pd.remove(row + i)
        nd.remove(row - i)
        
        board[row][i] = 0


def solve_n_queens(n):
    """ Solve N Queens. """
    col = set()
    pd = set()
    nd = set()

    """call backtrack to place our queens"""
    backtrack(0, n, col, pd, nd)


           
if N is not int:
            print("N must be a number", end = " ")
            sys.exit(1)
else:
    if nqueens(N) < 4:
                print("N must be at least 4", end = " ")
                sys.exit(1)
    if N != 4:
            print("Usage: nqueens N", end =" ")
            sys.exit(1)
    
