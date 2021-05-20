class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def get_height(self, root):
        # Write your code here
        if root is None:
            return 0
        else:
            if (root.left is not None) or (root.right is not None):
                return 1 + max(self.get_height(root.left), self.get_height(root.right))
            else:
                return 0

    def level_order(self, root):
        order = list()
        order.append(root)

        for items in order:
            if items.left is not None:
                order.append(items.left)
            if items.right is not None:
                order.append(items.right)

            print(items.data, end=" ")


if __name__ == '__main__':

    print("Input all data to create BST (ex: 3 5 2 1 4 6 7):")
    # allData = list(map(int, input().strip().split(' ')))
    allData = [3, 5, 2, 1, 4, 6, 7]
    myTree = Solution()
    nodeRoot = None
    for item in allData:
        nodeRoot = myTree.insert(nodeRoot, item)
    height = myTree.get_height(nodeRoot)
    print("Height of BST:", height)
    print("Level order of BST:", height)
    myTree.level_order(nodeRoot)
