# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        results = []

        que = deque()
        que.append(root)
        
        # BFS on tree using deque`
        while que:
            levelNodes = []
            for i in range(len(que)):
                currentNode = que.popleft()
                levelNodes.append(currentNode.val)
                if currentNode.left:
                    que.append(currentNode.left)
                if currentNode.right:
                    que.append(currentNode.right)
            results.append(levelNodes)
        return results
