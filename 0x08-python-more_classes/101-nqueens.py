#!/usr/bin/python3
import sys
""" Python3 program to solve N Queen"""
 
N = 4
 
 
def nqueens(N):
     for i in N:
        for j in N:
            if N[i][j] >= 4:
                print("Q",end=" ")
     else:           
        if N is not int:
            print("N must be a number", end = " ")
        
        if nqueens(N) < 4:
                print("N must be at least 4", end = " ")
        if N != 4:
            print("Usage: nqueens N", end =" ")
    
        exit(1)

