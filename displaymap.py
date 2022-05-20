from time import time
from planner.cbs import CBS
from cbsclass import CBSClass

positions, goalPositions, obstacles, freeCells, n, m, radius = CBSClass.collectData('data/input10_32x32_0.15_0.yaml')
map = {
    'agents':[{'start': list(positions[i]),'goal': list(goalPositions[i]), 'name': f'agent{i}'} for i in range(len(positions))],
    'map': {'dimensions':[n, m], 'obstacles':obstacles}
}
print(f'Obstacle density {str(len(obstacles)/(n*m)*100)[:4]}')
CBSClass.display(map)
