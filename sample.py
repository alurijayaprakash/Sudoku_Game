from random import *
def generateNewBoard():
    base  = 3
    side  = base*base
    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)

    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    sudokuBoard = []
    for line in board:
        # print(line)
        sudokuBoard.append(line)  
    return sudokuBoard

# for _ in range(10):
# 	value = randint(0, 10)
#     print(value)

# import random
# n = randint(1,9)
# m = randint(1,9)
# print(n,m)

# for i in range(len(list1)):
# for i in range(10):
#     n = randint(0,8)
#     m = randint(0,8)
#     print(n,m)
#     list1[n][m] = 0
# list2 = list1
# print("New List with random 0's ", list2)