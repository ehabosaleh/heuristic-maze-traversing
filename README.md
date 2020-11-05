# heuristic-maze-traversing
This repository contains two implementations of algorithms of finding the optimal path to traverse a customized size maze from the starting point to the target. The used algorithms are: Greedy Best First Search and A* Search.
## Greedy Best First Search
Greedy Best First Search algorithm takes advantage from both two algorithms: Depth First Search and Breadth First Search.  At each step we choose the most optimal node which is closet node to the goal node.
An estimated cost is being calculated by a heuristic function such as Manhattan Distance, Euclidean Distance and Hamming Distance.
More information in [Best First Search](https://en.wikipedia.org/wiki/Best-first_search)
## A* Search
A* is the best known algorithm to traverse a tree or a graph and it known as an improvement version of the algorithm Best First Search. Instead of using only the heuristic cost function which estimate the cost from the current node to the goal node, we use in addition the estimated cost from the starting node to the current node.  
More information in [A* Search](https://en.wikipedia.org/wiki/A*_search_algorithm)


## License
[MIT](https://choosealicense.com/licenses/mit/)
