from input import class_input
from input import student_input


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          33, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313]


def getprime(input):
    available_lst = []
    for k in range(len(input)):
        available = input[k]
        nrow, ncolumn = len(available), len(available[0])
        product = 1
        for i in range(nrow):
            for j in range(ncolumn):
                if int(available[i][j]) == 0:
                    product *= primes[j*nrow+i]
        available_lst.append(product)
    return available_lst


def gettimerough(input):
    goodtimes = []
    for i in range(len(primes)):
        if input % primes[i] == 0:
            goodtimes.append(primes[i])
    return goodtimes


print(getprime(student_input('test student.csv')))
