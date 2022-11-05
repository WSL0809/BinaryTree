# 二叉树节点定义
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # 将新值与父节点进行比较
        if self.value:  # 非空
            if value < self.value:  # 新值较小，放左边
                if self.left is None:  # 若空，则新建插入节点
                    self.left = TreeNode(value)
                else:  # 否则，递归往下查找
                    self.left.insert(value)
            elif value > self.value:  # 新值较大，放右边
                if self.right is None:  # 若空，则新建插入节点
                    self.right = TreeNode(value)
                else:  # 否则，递归往下查找
                    self.right.insert(value)
        else:
            self.value = value


class Solution:
    def preOrderTraversal(root: TreeNode) -> list[int]:
        res = []

        def traversal(root: TreeNode):
            if root is None:
                return
            res.append(root.value)
            traversal(root.left)
            traversal(root.right)

        traversal(root)
        return res

    def inOrderTraversal(root: TreeNode) -> list[int]:
        res = []

        def traversal(root: TreeNode):
            if root is None:
                return

            traversal(root.left)
            res.append(root.value)
            traversal(root.right)

        traversal(root)
        return res
    def postOrderTraversal(root: TreeNode) -> list[int]:
        res = []

        def traversal(root: TreeNode):
            if root is None:
                return

            traversal(root.left)
            traversal(root.right)
            res.append(root.value)


        traversal(root)
        return res
if __name__ == '__main__':
    root = TreeNode(27)

    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(Solution.preOrderTraversal(root))
    print(Solution.inOrderTraversal(root))
    print(Solution.postOrderTraversal(root))

