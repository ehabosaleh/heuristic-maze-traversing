import random as rn
import turtle
import numpy as np
import sys
import random
class Maze(turtle.Turtle):
      width=0
      height=0
      maze=""
      positions={}
      m_distances={}
      move_speed=0
      goal_point=(0,0)
      start_point=(0,0)
      def __init__(self,speed,width,height):
             turtle.Turtle.__init__(self)
             window=turtle.Screen()
             self.move_speed=speed
             window.title("A Maze")             
             window.setup(width,height)
             window=turtle.Screen()
             window.bgcolor("black")
             self.fillcolor('brown')
             self.penup()
             self.speed(speed)
             self.width=width
             self.height=height
             self.pencolor("green")
             self.pensize(3)
      def start(self,start_point,goal_point):
             self.start_point=start_point
             self.goal_point=goal_point
             if(self.maze[start_point[0]][start_point[1]] =='#'):
                    raise Exception("maze must have exactly one start point")
                    #sys.exit(1)
             if(self.maze[goal_point[0]][goal_point[1]] =='#'):
                    raise Exception("maze must have exactly one goal")
                    #sys.exit(1)
             self.setup_maze(self.goal_point) 
                        
      def setup_maze(self,goal_point):
             self.pencolor("white")
             for i in range(len(self.maze)):
                 for j in range(len(self.maze[i])):
                     x=-int(self.width/2-10)+15*j
                     y=int(self.height/2-15)-15*i
                     self.goto(x,y)
                     if self.maze[i][j]=='#':                      
                       self.stamp()
                     elif self.maze[i][j]=='O':
                       cost=self.manhattan_distance((i,j),goal_point)
                       self.m_distances[(i,j)]=cost
                       self.write(cost,align="center",font=("Times",7, "normal"))
   
      def manhattan_distance(self,point_A,point_B):
           return (abs(point_A[0]-point_B[0])+abs(point_A[1]-point_B[1]))      
                      
      def random_positions(self):
           
             self.maze=[['#' for i in range(int(self.width/15))] for j in range(int(self.height/15))]
             h=len(self.maze)
             w=len(self.maze[0])
             stack=[]
             tentative_stack=[]
             pos=(0,0)
             stack.append(pos)
             visited=[]

             while len(stack)!=0 :            
                       (i,j) = pos
                       self.maze[i][j]='O' 
                       if (j+1)in range(len(self.maze[0])) and (i,j+1) not in visited:
                          tentative_stack.append((i,j+1))

                       if (j-1) in range(len(self.maze[0])) and (i,j-1) not in visited:
                          tentative_stack.append((i,j-1))

                       if (i-1) in range(len(self.maze)) and (i-1,j) not in visited:
                          tentative_stack.append((i-1,j))

                       if (i+1) in range(len(self.maze)) and (i+1,j) not in visited:
                          tentative_stack.append((i+1,j))
                       if(len(tentative_stack)==0):
                          pos=stack.pop()
                       else:   
                          new_pos=random.choice(tentative_stack)
                        
                          if pos not in self.positions:
                               self.positions[pos]=[]
                               self.positions[pos].append(new_pos)
                          elif new_pos not in self.positions[pos]:
                               self.positions[pos].append(new_pos)
                          if new_pos not in self.positions:
                               self.positions[new_pos]=[]
                               self.positions[new_pos].append(pos)
                          elif pos not in self.positions[new_pos]:
                               self.positions[new_pos].append(pos)  
                  
                          pos=new_pos
                          visited.append(pos)
                          stack.append(pos)
             
                          tentative_stack=[]
             del stack
             del tentative_stack
             del visited
             visited_wall=[]    
                  
             for (i,j) in self.positions.keys(): 
                           if  ((i,j),(i,j+1)) not in visited_wall and (i,j+1) not in self.positions[(i,j)]:
                              self.draw_wall((i,j),(i,j+1),1)
                              visited_wall.append(((i,j),(i,j+1)))
                           if ((i,j-1),(i,j)) not in visited_wall and (i,j-1) not in self.positions[(i,j)]:
                              self.draw_wall((i,j-1),(i,j),1)
                              visited_wall.append(((i,j-1),(i,j)))
                           if  ((i-1,j),(i,j)) not in visited_wall and (i-1,j) not in self.positions[(i,j)]:
                              self.draw_wall((i-1,j),(i,j),0)
                              visited_wall.append(((i-1,j),(i,j)))
                           if ((i,j),(i+1,j)) not in visited_wall and (i+1,j) not in self.positions[(i,j)]:
                              self.draw_wall((i,j),(i+1,j),0)
                              visited_wall.append(((i,j),(i+1,j)))                      
      def draw_wall(self,point_1,point_2,flg):
                  if flg==1:
                     x=-int(self.width/2)+15*point_2[1]
                     y=int(self.height/2)-15*point_1[0]
                     point1=(x,y)
                     x=-int(self.width/2)+15*point_2[1]
                     y=int(self.height/2)-15*point_2[0]-15
                     point2=(x,y)
                     self.penup()
                     self.goto(point1)
                     self.pendown()
                     self.goto(point2)
                     self.penup()  
                  else:
                     x=-int(self.width/2)+15*point_1[1]
                     y=int(self.height/2)-15*point_2[0]
                     point1=(x,y)
                     x=-int(self.width/2)+15*point_2[1]+15
                     y=int(self.height/2)-15*point_2[0]
                     point2=(x,y)
                     self.penup()
                     self.goto(point1)
                     self.pendown()
                     self.goto(point2)
                     self.penup()  
             
             
                    
      def path_setup(self,path,color="Red"):
             self.speed(0)
             #self.shape("classic")
             self.pencolor(color)
             for block in path:
                     x=-int(self.width/2-10)+15*block[1]
                     y=int(self.height/2-15)-15*block[0]
                     self.goto(x,y)
                     self.write(self.m_distances[block],align="center",font=("Times",6, "normal"))
             self.speed(self.move_speed)
             
