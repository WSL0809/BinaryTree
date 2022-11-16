from Solution import Solution, TreeNode
from collections import deque


def rightSideView(root: TreeNode):
    q = deque()
    res = []
    if root is not None:
        q.append(root)
    else:
        return res
    while q:
        size = len(q)
        for i in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == size - 1:
                res.append(node.value)
    return res
if __name__ == '__main__':
    root = TreeNode(27)
    Solution.doInsert(root)
    print(Solution.bfs(root))
    print(rightSideView(root))