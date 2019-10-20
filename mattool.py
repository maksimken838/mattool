from math import *
from os import system, name

class Matrix:
    def __init__(self, strings, rows, matrix):
        self.strings = int(strings)
        self.rows = int(rows)
        self.matrix = matrix
        self.maxlength = 0
    def deflength(self):
        for i in range(int(self.strings)):
            for j in range(self.rows):
                self.maxlength = max(self.maxlength, len(str(self.matrix[i][j])))
    def add(self, a, b, c):
        for i in range(self.rows):
           self.matrix[b][i] = float(self.matrix[b][i]) + float(self.matrix[a][i]) * c
    def prt(self):
        self.deflength()
        print('This is your matrix')
        for i in range(self.strings):
            for j in range(self.rows):
                print(str(self.matrix[i][j]).rjust(self.maxlength), end = ' ')
            print()
        print()
def clear(name):
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def clear_console():
    clear(name)
    print('You are in the command mode now, please type here your commands (If you don\'t know what to do just type \'help\')')
    print()
    if 'X' in globals():
        X.prt()
    else:
        print('TIP: Type \'input\' to feed in your matrix')
        print()

def console():
    global X
    clear_console()
    command = input()
    if command == 'input':
        print()
        print('Now you should define size of the matrix - type two numbers, first for number of columns and second for number of rows')
        print()
        n, m = [int(x) for x in input().split()]
        print()
        print('Now just type your matrix line by line')
        print()
        A = []
        for i in range(n):
            A.append(list(input().split()))
        X = Matrix(n, m, A)
        X.prt()
    elif command = "finput":
        
    elif command == 'add':
        print()
        print('Now type 3 numbers (What string, to what string, with what multiplier)')
        print()
        a, b, c = [float(x) for x in input().split()]
        X.add(int(a) - 1, int(b) - 1, c)
        X.prt()
    elif command == 'clear':
        X.prt()
    elif command == 'exit':
        return
    console()

console()
