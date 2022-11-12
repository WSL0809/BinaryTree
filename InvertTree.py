from .Solution import TreeNode


class InvertTree:
    @staticmethod
    def invertTree(root: TreeNode):
        if root is None:
            return root

        root.left, root.right = root.right, root.left
        InvertTree.invertTree(root.left)
        InvertTree.invertTree(root.right)
        return root

