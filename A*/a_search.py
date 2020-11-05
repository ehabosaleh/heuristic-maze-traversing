from collections import deque
import numpy as np
class ASearch:   
   optimal_path=[]
   shortest_path=[]
   tree={}
   cost={}
   new_cost=[]
   pos=0
   path={}      
   def a_search(self,src_node,dest_node):
        queue=[]
        self.path=[]
        steps=[]
        total_cost=[self.cost[src_node]]
        found=False
        queue.append(src_node)
        self.optimal_path.append([src_node])
        steps.append([0])
        keys=list(self.tree)
        

        while(len(queue)!=0):

                  nominated_node=queue[total_cost.index(min(total_cost))]
                  lower_cost=min(total_cost)
                  
                  if nominated_node==dest_node:
                    found=True
                    pos=total_cost.index(min(total_cost))
                    self.path.append(queue.pop(queue.index(nominated_node)))  
                    break
                     
                  elif  nominated_node in keys:
                     V=nominated_node
                     self.path.append(queue.pop(queue.index(nominated_node)))
                     p=self.optimal_path[total_cost.index(min(total_cost))]
                     step=steps[total_cost.index(min(total_cost))]
                     steps.pop(total_cost.index(min(total_cost)))
                     self.optimal_path.pop(total_cost.index(min(total_cost)))

                     total_cost.pop(total_cost.index(min(total_cost)))
                     
                     for l  in range(len(self.tree[V])):
                        if  self.tree[V][l] not in self.path and self.tree[V][l] not in queue:
                         queue.append(self.tree[V][l])
                         steps.append(np.array(step)+1)
                         total_cost.append(self.cost[self.tree[V][l]]+np.array(step)) 
                         self.optimal_path.append(p+[self.tree[V][l]])
        if found==True:
           self.shortest_path=self.optimal_path[pos]
           print("UCS:Optimal path from {} to {} is {}, with totall cost: {}\n Path was found after traversing all of these nodes:\n {}".format(src_node,dest_node,self.optimal_path[pos],total_cost[pos],(self.path)))
           print('-'*50)
        elif found==False:
           print("Target {} is NOT reachable from source {}  using UCS".format(dest_node,src_node)) 
           print('-'*50) 
        del queue
