from math import *
from os import system, name

"The beginning of Matrix class"

class Matrix:

    def __init__(self, strings, rows, matrix):
        self.strings = int(strings)
        self.rows = int(rows)
        self.matrix = matrix
        self.maxlength = 0
        self.isAugmented = False

    def deflength(self):
        for i in range(int(self.strings)):
            for j in range(self.rows):
                self.maxlength = max(self.maxlength, len(str(self.matrix[i][j])))

    def add(self, a, b, c):
        for i in range(self.rows):
           self.matrix[b][i] = float(self.matrix[b][i]) + float(self.matrix[a][i]) * c

    def isSquare(self):
        if self.strings == self.rows:
            return True
        else:
            return False

    def augment(self):
        print('debug message')
        if self.isSquare():
            for i in range(self.strings):
                for j in range(self.rows):
                    if self.strings == self.rows:
                        self.matrix[i].append(1)
                    else:
                        self.matrix[i].append(0)
            self.rows == self.rows * 2
            self.isAugmented = True
        else:
            print('Error: trying to add identity matrix to matrix which is not square\n')

    def prt(self):
        self.deflength()
        print('This is your matrix')
        for i in range(self.strings):
            for j in range(self.rows):
                if j == 0:
                    print('(', end = ' ')
                elif self.isAugmented and j == self.rows:
                    print('|', end = '  ')
                if j == self.rows - 1:
                    print(str(self.matrix[i][j]).rjust(self.maxlength) + ' )', end = '\n')
                else:
                    print(str(self.matrix[i][j]).rjust(self.maxlength), end = '  ')

        print('\nYou still can use commands\n')

"The end of Matrix class"

def clear(name):
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def clear_console():
    clear(name)
    print('You are in the command mode now, please type here your commands (If you don\'t know what to do just type \'help\')\n')
    if 'X' in globals():
        X.prt()
    else:
        print('TIP: Type \'input\' to feed in your matrix\n')

def console():
    global X
    clear_console()
    command = input()
    if command == 'input':
        print('\nNow you should define size of the matrix - type two numbers, first for number of columns and second for number of rows\n')
        n, m = [int(x) for x in input().split()]
        print()
        print('\nNow just type your matrix line by line\n')
        print()
        A = []
        for i in range(n):
            A.append(list(input().split()))
        X = Matrix(n, m, A)
        X.prt()
    elif command == 'add':
        print('\nNow type 3 numbers (What string, to what string, with what multiplier)\n')
        a, b, c = [float(x) for x in input().split()]
        X.add(int(a) - 1, int(b) - 1, c)
        X.prt()
    elif command == 'fuck':
        print("debug message_0")
        X.augment()
        X.prt()
        X.augment()
        print(X)
    elif command == 'clear':
        X.prt()
    elif command == 'exit':
        return
    else:
        print('Command does not exist')
        system(read)
    console()

console()
