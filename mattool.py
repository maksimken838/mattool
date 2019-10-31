from math import *
from os import system, name

"The beginning of Matrix class"

class Matrix:

    def __init__(self, strings, rows, matrix):
        self.strings = int(strings)
        self.rows = int(rows)
        self.matrix = matrix
        self.maxlength = 0
        self.IsAugmented = False
        self.IsDet = False
    
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

    def multiply(self, a, b):
        for i in range(self.rows):
            self.matrix[a][i] *= b

    def IsSquare(self):
        if self.strings == self.rows:
            return True
        else:
            return False

    def addunit(self):
        if self.IsSquare():
            for i in range(self.strings):
                for j in range(self.rows):
                    if i == j:
                        self.matrix[i].append(1)
                    else:
                        self.matrix[i].append(0)
            self.rows = self.rows * 2
            self.IsAugmented = True
        else:
            print('Error: trying to add identity matrix to matrix which is not square\n')

    def delunit(self):
        if self.IsAugmented:
            for i in range(self.strings):
                del self.matrix[i][self.strings : self.rows - 1]
            self.rows = self.strings
    
    def det(self):
        if self.IsSquare():
            "self.IsDet = True"
            if self.strings == 2:
                a = self.matrix
                res = []
                res[0] = a[0][0] * a[1][1]
                res[1] = a[0][1] * a[1][0]
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            elif self.strings == 3:
                a = self.matrix
                res = []
                res[0] = a[0][0] * a[1][1] * a[2][2]
                res[1] = a[0][1] * a[1][2] * a[2][0]
                res[2] = a[0][2] * a[1][0] * a[2][1]
                res[3] = a[0][2] * a[1][1] * a[2][0]
                res[4] = a[0][0] * a[1][2] * a[2][1]
                res[5] = a[0][1] * a[1][0] * a[2][2]

                return '(' + str(self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]) + ') + (' + str(self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0]) + ') + (' + str(self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1]) + ') - (' + str(self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]) + ') - (' + str(self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]) + ') - (' + str(self.matrix[1][0] * self.matrix[0][1] * self.matrix[2][2]) + ') = ', (self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] + self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0] + self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1] - self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0] - self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1] - self.matrix[1][0] * self.matrix[0][1] * self.matrix[2][2])
            else:
                d = 0
                s = ''
                fix = 0
                for i in range(self.strings):
                    for j in range(self.rows):
                        reduced_matrix = []
                        fix = 0
                        for k in range(self.strings):
                            if k != i:
                                reduced_matrix.append([])
                                for l in range(self.rows):
                                    if l != j:
                                        reduced_matrix[k - fix].append(self.matrix[k][l])
                                        print('>', reduced_matrix)
                            else:
                                fix = 1
                    a = Matrix(self.strings - 1, self.rows - 1, reduced_matrix)
                    print(a.strings, a.rows, a.matrix)
                    s1 = (Matrix(self.strings - 1, self.rows - 1, reduced_matrix).det()) + ' + '
                    s += s1[0]
                    d += s1[1]
                return s, d

    def prt(self):
        for i in range(self.strings):
            for j in range(self.rows):
                if float(self.matrix[i][j]) == int(self.matrix[i][j]):
                    self.matrix[i][j] = int(self.matrix[i][j])
                else:
                    self.matrix[i][j] = float(self.matrix[i][j])

        self.deflength()
        print('This is your matrix')
        for i in range(self.strings):
            for j in range(self.rows):
                if j == 0:
                    print('(', end = ' ')
                elif self.IsAugmented and j == self.strings:
                    print('|', end = ' ')
                print(str(self.matrix[i][j]).rjust(self.maxlength), end = ' ')
                if j == self.rows - 1:
                    print(')', end = '\n')
        print('\n|A| = ' + str(self.det()))
        print('\nYou still can use commands\n')

"The end of Matrix class"

def clear(name):
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def clear_console():
    clear(name)
    print('MATTOOL - Easy to use (I hope it is) console matrix manipulation tool\n')
    if 'X' in globals():
        X.prt()
    else:
        print('TIP: Type \'input\' to feed in your matrix\n')

def console():
    global X
    clear_console()
    command = input('--> ')
    if command == 'input':
        print('\nNow you should define size of the matrix - type two numbers, first for number of columns and second for number of rows\n')
        n, m = [int(x) for x in input('--> ').split()]
        print('\nNow just type your matrix line by line\n')
        A = []
        for i in range(n):
            A.append(list(input('--> ').split()))
        X = Matrix(n, m, A)
    elif command == 'add':
        print('\nNow type 3 numbers (What string, to what string, with what multiplier)\n')
        a, b, c = [float(x) for x in input('--> ').split()]
        X.add(int(a) - 1, int(b) - 1, c)
    elif command == 'swap':
        print('\nNow type 2 numbers (Numbers of string that the program should swap)\n')
        a, b = [int(x) for x in input('--> ').split()]
        X.swap(a - 1, b - 1)
    elif command == 'mult' or command == 'multiply':
        print('\nNow type 2 numbers, what string to multiply and the actual multiplier\n')
        a, b = [float(x) for x in input('--> ').split()]
        X.multiply(int(a) - 1, b)
    elif command == 'addunit' or command == '+unit':
        X.addunit()
    elif command == 'delunit' or command == '-unit':
        X.delunit()
    elif command == 'exit':
        return
    console()

console()
