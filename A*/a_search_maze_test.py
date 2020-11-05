from maze_2 import Maze
#from maze_1 import Maze
from a_search import ASearch



m=Maze(10,1029,700)
#m=Maze(10,200,200)
m.random_positions()
row_1=m.maze[0]
j=row_1[int(len(row_1)/2):-1].index('O')
j=j+int(len(row_1)/2)
start_point=(0,j)
row_2=m.maze[-1]
j=int(len(row_2)/2)
goal_point=(len(m.maze)-1,j)


m.start(start_point,goal_point)


g= ASearch()
g.tree=m.positions
g.cost=m.m_distances

g.a_search(start_point,goal_point)
m.path_setup(list(g.path),"Red")
m.path_setup(g.shortest_path,"yellow")
x=input("Press any key to continue....!")
