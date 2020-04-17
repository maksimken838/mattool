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
    
    def det(self, isStr = True, number = 0):
        if self.IsSquare():
            "self.IsDet = True"
            if self.strings == 2:
                a = self.matrix[:]
                res = []
                res[0] = a[0][0] * a[1][1]
                res[1] = a[0][1] * a[1][0]
                return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
            elif self.strings == 3:
                a = self.matrix[:]
                res = [0, 0, 0, 0, 0, 0]
                res[0] = a[0][0] * a[1][1] * a[2][2]
                res[1] = a[0][1] * a[1][2] * a[2][0]
                res[2] = a[0][2] * a[1][0] * a[2][1]
                res[3] = a[0][2] * a[1][1] * a[2][0]
                res[4] = a[0][0] * a[1][2] * a[2][1]
                res[5] = a[0][1] * a[1][0] * a[2][2]
                s = '(' + str(res[0]) + ') + (' + str(res[1]) + ') + (' + str(res[2]) + ') - (' + str(res[3]) + ') - (' + str(res[4]) + ') - (' + str(res[5]) + ')' 
                return s, res[0] + res[1] + res[2] - res[3] - res[4] - res[5]
            else:
                '''
                value = 0
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
                            else:
                                fix = 1
                    s1, value1 = (Matrix(self.strings - 1, self.rows - 1, reduced_matrix)).det()
                    s += '|A|(' + str(i) + ')(' + str(j) + ') + (' + s1 + ' = ' + str(value1) + '\n'
                    value += value1
                print(reduced_matrix)
                return s, value
                '''
                return self.Laplace(isStr, number)

    def Laplace(self, isStr = True, number = 0):
        value = 0
        result = ''
        sign = '-'
        if isStr:
            for i in range(self.rows):
                sign = '-' if (i * number) % 2 == 1 else '+'
                preresult, prevalue = self.submatrix(number, i).det()
                result += '|A|(' + str(number) + ')(' + str(i) + ') = ' + sign + '( ' + preresult + ' ) = ' + str(prevalue) + '\n'
                value += prevalue if sign == '+' else -prevalue
        else:
            for i in range(self.strings):
                sign = '-' if (i * number) % 2 == 1 else '+'
                preresult, prevalue = self.submatrix(i, number).det()
                result += '|A|(' + str(i) + ')(' + str(number) + ') = ' + sign + '( ' + preresult + ' ) = ' + str(prevalue) + '\n'
                value += prevalue if sign == '+' else -prevalue
        return result, value

    def submatrix(self, string, row):
        submat = list(self.matrix)
        print(string, row)
        print(submat, id(submat))
        print(self.matrix, id(self.matrix))
        #del submat[0:self.strings][row]
        for i in range(self.strings):
            del submat[i][row]
            print(submat, id(submat))
            print(self.matrix, id(self.matrix))
        del submat[string]
        print(submat)
        print(self.matrix)
        return Matrix(self.strings - 1, self.strings - 1, submat)

    def prt(self):

        print(str(self))
        #for i in range(self.strings):
        #    for j in range(self.rows):
        #        if float(self.matrix[i][j]) == int(self.matrix[i][j]):
        #            self.matrix[i][j] = int(self.matrix[i][j])
        #        else:
        #            self.matrix[i][j] = float(self.matrix[i][j])

        #self.deflength()
        ##print('This is your matrix')
        #for i in range(self.strings):
        #    for j in range(self.rows):
        #        if j == 0:
        #            print('(', end = ' ')
        #        elif self.IsAugmented and j == self.strings:
        #            print('|', end = ' ')
        #        print(str(self.matrix[i][j]).rjust(self.maxlength), end = ' ')
        #        if j == self.rows - 1:
        #            print(')', end = '\n')
        #s = []
        #s = self.det()
        #print(s[0] + '\t|A| = ' + str(s[1]) + '\n')
        #print('\nYou still can use commands\n')

    def __str__(self):
        self.deflength()
        #s = ' '.join([s, '(', str(x).rjust(self.maxlength), ')\n'])[[f.maxlength), ')\n']) for x in y] for y in self.matrix]
        s = ''
        for column in self.matrix:
            s += '( '
            for i, x in enumerate(column):
                if self.IsAugmented and i == self.strings:
                    s += '| '
                s += str(x).rjust(self.maxlength) + ' '
            s += ')'
            if self.matrix.index(column) != self.strings - 1:
                s += '\n' 
        return s


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
        history.append(['init', [n, m, A]])
        Mhistory.append(X)
    elif command == 'add':
        print('\nNow type 3 numbers (What string, to what string, with what multiplier)\n')
        a, b, c = [float(x) for x in input('--> ').split()]
        history.append(['add', [a, b, c]])
        Mhistory.append(X)
        X.add(int(a) - 1, int(b) - 1, c)
    elif command == 'swap':
        print('\nNow type 2 numbers (Numbers of string that the program should swap)\n')
        a, b = [int(x) for x in input('--> ').split()]
        history.append(['swap', [a, b]])
        Mhistory.append(X)
        X.swap(a - 1, b - 1)
    elif command == 'mult' or command == 'multiply':
        print('\nNow type 2 numbers, what string to multiply and the actual multiplier\n')
        a, b = [float(x) for x in input('--> ').split()]
        history.append(['multiply', [a, b]])
        Mhistory.append(X)
        X.multiply(int(a) - 1, b)
    elif command == 'addunit' or command == '+unit':
        X.addunit()
    elif command == 'delunit' or command == '-unit':
        X.delunit()
    elif command == 'history' or command == 'his':
        for x in range(len(Mhistory)):
            print(history[x])
            Mhistory[x].prt()
        qqq = input()
    elif command == 'exit':
        return
    console()

if __name__ == '__main__':
    Mhistory = []
    history = []
    console()
