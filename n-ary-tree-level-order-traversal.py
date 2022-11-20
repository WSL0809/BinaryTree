from collections import deque
from Solution import TreeNode, Solution

"""
#本题没有测试，懒得定义 n 叉树了
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


def levelOrder(root: TreeNode):
    res = []
    q = deque()
    if root is None:
        return res
    q.append(root)

    while q:
        tmp = []
        size = len(q)
        for _ in range(size):
            t = q.popleft()
            tmp.append(t.value)
            if t.children:
                for child in t.children:
                    q.append(child)

        res.append(tmp)
    return res
