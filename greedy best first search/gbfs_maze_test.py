from maze import Maze
from gbfs import GBFS



m=Maze(10,1029,700)
#m=Maze(0,200,200)
m.random_positions()

row_1=m.maze[0]
j=int(len(row_1)/2)

start_point=(0,j)
row_2=m.maze[-1]
j=int(len(row_2)/2)
goal_point=(len(m.maze)-1,j)

m.start(start_point,goal_point)


g= GBFS()
g.tree=m.positions
g.cost=m.m_distances

g.gbfs(start_point,goal_point)
m.path_setup(list(g.path),"red")
m.path_setup(g.shortest_path,"green")
x=input("Press any key to continue....!")
