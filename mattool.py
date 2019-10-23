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

    def swap(self, a, b):
        x = []
        x = self.matrix[a]
        self.matrix[a] = self.matrix[b]
        self.matrix[b] = x

    def isSquare(self):
        if self.strings == self.rows:
            return True
        else:
            return False

    def addunit(self):
        if self.isSquare():
            for i in range(self.strings):
                for j in range(self.rows):
                    if i == j:
                        self.matrix[i].append(1)
                    else:
                        self.matrix[i].append(0)
            self.rows = self.rows * 2
            self.isAugmented = True
        else:
            print('Error: trying to add identity matrix to matrix which is not square\n')

    def delunit(self):
        if self.isAugmented:
            for i in range(self.strings):
                del self.matrix[i][self.strings : self.rows - 1]
            self.rows = self.strings
    
    def det(self):
        "some code"

    def prt(self):
        self.deflength()
        print('This is your matrix')
        for i in range(self.strings):
            for j in range(self.rows):
                if j == 0:
                    print('(', end = ' ')
                elif self.isAugmented and j == self.strings:
                    print('|', end = ' ')
                print(str(self.matrix[i][j]).rjust(self.maxlength), end = ' ')
                if j == self.rows - 1:
                    print(')', end = '\n')
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
        print('\nNow just type your matrix line by line\n')
        A = []
        for i in range(n):
            A.append(list(input().split()))
        X = Matrix(n, m, A)
    elif command == 'add':
        print('\nNow type 3 numbers (What string, to what string, with what multiplier)\n')
        a, b, c = [float(x) for x in input().split()]
        X.add(int(a) - 1, int(b) - 1, c)
    elif command == 'swap':
        print('\nNow type 2 numbers (Numbers of string that the program should swap)\n')
        a, b = [int(x) for x in input().split()]
        X.swap(a - 1, b - 1)
    elif command == 'addunit' or command == '+unit':
        X.addunit()
    elif command == 'delunit' or command == '-unit':
        X.delunit()
    elif command == 'exit':
        return
    console()

console()
