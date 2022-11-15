from Solution import Solution, TreeNode
from collections import deque


def rightSideView(root: TreeNode):
    q = deque()
    res = []
    if root is not None:
        q.append(root)
    else:
        return res


if __name__ == '__main__':
    root = TreeNode(27)
    Solution.doInsert(root)
    print(Solution.bfs(root))
