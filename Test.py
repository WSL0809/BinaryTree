from traversal import *
# from InvertTree import *
class Test:
    if __name__ == '__main__':
        root = TreeNode(27)

        root.insert(14)
        root.insert(35)
        root.insert(10)
        root.insert(19)
        root.insert(31)
        root.insert(42)
        '''

        '''
        print(Solution.preOrderTraversal(root))
        print(Solution.inOrderTraversal(root))
        print(Solution.postOrderTraversal(root))
        print(Solution.bfs(root))
        print(Solution.bfs(Solution.invertTree(root)))
