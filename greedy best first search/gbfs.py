from collections import deque
class GBFS:   
   optimal_path=[]
   shortest_path=[]
   tree={}
   cost={}
   pos=0
   path={}      
   def gbfs(self,src_node,dest_node):
        queue=[]
        self.path=[]
        total_cost=[self.cost[src_node]]
        found=False
        queue.append(src_node)
        self.optimal_path.append([src_node])
        keys=list(self.tree)
        while(len(queue)!=0):                              
                  nominated_node=queue[total_cost.index(min(total_cost))]
                  lower_cost=min(total_cost)
                  
                  if nominated_node==dest_node:
                    found=True
                    pos=total_cost.index(min(total_cost))
                    self.path.append(queue.pop(queue.index(nominated_node)))  
                    break
                    
                  elif nominated_node not in keys  :
                     self.path.append(queue.pop(queue.index(nominated_node))) 
                     
                     self.optimal_path.pop(total_cost.index(min(total_cost)))
                     total_cost.pop(total_cost.index(min(total_cost)))
                  elif  nominated_node in keys:
                     V=nominated_node
                     self.path.append(queue.pop(queue.index(nominated_node)))
                     p=self.optimal_path[total_cost.index(min(total_cost))]
                     self.optimal_path.pop(total_cost.index(min(total_cost)))                
                     total_cost.pop(total_cost.index(min(total_cost)))
                     
                     for l  in range(len(self.tree[V])):
                        if  self.tree[V][l] not in self.path and self.tree[V][l] not in queue:
                         queue.append(self.tree[V][l])
                         total_cost.append(self.cost[ self.tree[V][l]]) 

                         self.optimal_path.append(p+[self.tree[V][l]])
        if found==True:
           self.shortest_path=self.optimal_path[pos]
           print("GBFS:Optimal path from {} to {} is {}\n Path was found after traversing all of these nodes:\n {}".format(src_node,dest_node,self.optimal_path[pos],set(self.path)))
           print('-'*50)
        elif found==False:
           print("Target {} is NOT reachable from source {}  using UCS".format(dest_node,src_node)) 
           print('-'*50) 
           self.optimal_path=[[self.shortest_path]]
        del queue
