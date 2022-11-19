from collections import deque

from Solution import TreeNode, Solution


def averageOfLevels(root: TreeNode):
    res = []
    q = deque()
    if root is None:
        return res
    q.append(root)
    while q:
        size = len(q)
        t = []
        for _ in range(size):
            node = q.popleft()
            t.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        a = doAvg(t)
        res.append(a)
    return res


def doAvg(arr: list):
    sum = 0
    for i in arr:
        sum += i
    avg = sum / len(arr)
    print(avg)
    return avg


if __name__ == '__main__':
    root = TreeNode(27)
    Solution.doInsert(root)
    end = averageOfLevels(root)
    print(end)
    # arr = [1, 2, 3, 4, 5]
    # doAvg(arr)
