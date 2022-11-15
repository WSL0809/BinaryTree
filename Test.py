from Solution import *


# from InvertTree import *
class Test:
    if __name__ == '__main__':
        root = TreeNode(27)
        Solution.doInsert(root)

        # print(Solution.preOrderTraversal(root))
        # print(Solution.inOrderTraversal(root))
        # print(Solution.postOrderTraversal(root))
        print(Solution.bfs(root))
        # print(Solution.levelOrderBottom(root))

    # print(Solution.bfs(Solution.invertTree(root)))
