from os import stat
from time import time
from planner.cbs import CBS
from cbsclass import CBSClass

import random

positions, goalPositions, obstacles, freeCells, n, m, radius = CBSClass.collectData('data/input10_32x32_0.15_0.yaml')

f = open('output_data/explorations2agents.csv', 'a+')
i = 1
NUM_AGENTS = 2
try:
    while True:
        startPos = []
        goalPos = []
        for numagents in range(NUM_AGENTS):
            s = (random.randint(0, 31), random.randint(0, 31))
            g = (random.randint(0, 31), random.randint(0, 31))
            while s == g or s in obstacles or g in obstacles or s in startPos or s in goalPos or g in goalPos or g in startPos:
                s = (random.randint(0, 31), random.randint(0, 31))
                g = (random.randint(0, 31), random.randint(0, 31))
            startPos.append(s)
            goalPos.append(g)
        # startPos, goalPos = [(4, 0), (1, 25)], [(24, 7), (3, 9)]
        totalTime, dist, replanningCnt = CBSClass.solve(startPos, goalPos, obstacles, freeCells, 32, 32, 10)
        print(dist, replanningCnt, totalTime)
        # print(f'{startPos[0]}, {startPos[1]}, {goalPos[0]}, {goalPos[1]}, {dist}, {replanningCnt}, {totalTime}\n')
        output, outputReversed = '', ''
        for s, g in zip(startPos, goalPos):
            output += f'{s[0]},{s[1]},{g[0]},{g[1]},'
        for s, g in zip(goalPos, startPos):
            outputReversed += f'{s[0]},{s[1]},{g[0]},{g[1]},'
        output += f'{dist},{replanningCnt},{totalTime}\n'
        outputReversed += f'{dist},{replanningCnt},{totalTime}\n'
        f.write(output)
        f.write(outputReversed)
        if i % 10 == 0:
            f.close()
            print(f"{i} Explorations Run")
            f = open('output_data/explorations2agents.csv', 'a+')
        i += 1
except KeyboardInterrupt:
    pass

# replanningCnt = 11
# while replanningCnt > 1:
#     startPos = (11, 16)
#     goalPos = (18, 26)
#     totalTime, dist, replanningCnt = CBSClass.solve([startPos], [goalPos], obstacles, freeCells, 32, 32, 10)
#     # print(totalTime, dist, replanningCnt)
#     print(len(CBSClass.positionCache))

# f = open('explorations.csv', 'a+')
# startPos = (11, 23)
# goalPos = (23, 28)
# totalTime, dist, replanningCnt = CBSClass.solve([startPos], [goalPos], obstacles, freeCells, 32, 32, 10)
# print(dist, totalTime, replanningCnt)
# print(f'{startPos[0]}, {startPos[1]}, {goalPos[0]}, {goalPos[1]}, {dist}, {totalTime}, {replanningCnt}\n')
# f.write(f'{startPos[0]}, {startPos[1]}, {goalPos[0]}, {goalPos[1]}, {dist}, {totalTime}, {replanningCnt}\n')
# f.close()