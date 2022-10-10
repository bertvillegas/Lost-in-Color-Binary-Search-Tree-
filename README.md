# Lost-in-Color-Binary-Search-Tree-
Returns the path to a node in a Binary Search Tree based on its respected color

Write a function which traverses a tree and returns the path to the desired node.

The maze is represented by a tree, where each node has a val, which tells you which color it is, and a left node and a right node (although nodes might be None!). Once you find the color you're looking for, return the path you took to get there. The output should be a list of 'left' and 'right' strings.
![download](https://user-images.githubusercontent.com/110595566/194790448-d975f7a4-799f-4e2a-8be9-b23b89469f62.png)

![download (1)](https://user-images.githubusercontent.com/110595566/194790453-a0e4a222-6077-4906-8ff2-8c40e630cb63.png)

For example, if you were asked to return the path to 'yellow' in this maze, you should return ['right', 'left']. You begin at 'red'. After going right, you'd be at 'blue'. After going left, you'd be at 'yellow', which is the goal node. Since the path you took was right then left, you should return ['right', 'left'].  
