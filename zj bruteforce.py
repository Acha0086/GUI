test = ('Isuru', [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

classes = ['FIT2004', ['WS1', '1', 'Mon', '15-16'], ['WS2 1', 'Thu', '15-16']]

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          33, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311]


def getprime(input):
    available = input[1]
    nrow, ncolumn = len(available), len(available[0])
    product = 1
    for i in range(nrow):
        for j in range(ncolumn):
            if available[i][j] == 0:
                product *= primes[j*nrow+i]
    return product


def getdayrough(input):
    goodtimes = []
    for i in range(len(primes)):
        if input // primes[i] == 0:
            goodtimes.append(primes[i])
    return goodtimes, input


print(getprime(test))
print(getdayrough(getprime(test)))