from .traversal import TreeNode


@staticmethod
def invertTree(root: TreeNode):
    if root is None:
        return root

