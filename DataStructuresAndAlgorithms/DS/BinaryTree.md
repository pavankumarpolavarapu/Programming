# Binary Tree
A tree which has atmost two elements as its children is called a binary tree.

A Binary tree contains
	1) Data
	2) Pointer to Right child
	3) Pointer to Left child

```python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
```

1) Full Binary Tree
    If every node contains 0 or 2 child nodes
2) Perfect Binary Tree
    If every node contains 2 children and all leaves are at the same level
3) Balanced Binary Tree
    If the height of the tree is O(logn)
