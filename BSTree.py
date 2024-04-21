#A.Tree Data Structure can be traversed in following ways:

#1.Depth First Search or DFS
# Inorder Traversal
# Preorder Traversal
# Postorder Traversal
#2.Level Order Traversal or Breadth First Search or BFS
#3.Boundary Traversal
#4.Diagonal Traversal

# Inorder

# class Node: 
#     def __init__(self, key): 
#         self.left = None 
#         self.right = None 
#         self.val = key 

# def printInorder(root): 
#     if root: 
#         printInorder(root.left)
    
#         print(root.val, end = " ")

#         printInorder(root.right)

# if __name__ == "__main__": 
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.left = Node(6)
#     root.right.right = Node(7)

#     print("Inorder traversal of binary tree is")
#     printInorder(root)

# Preorder

# def printPreorder(root): 
#     if root: 
#         print(root.val, end = " ")

#         printPreorder(root.left)

#         printPreorder(root.right)

# if __name__ == "__main__": 
#     root = Node(1)
#     root.left = Node(2)
#     root.right = Node(3)
#     root.left.left = Node(4)
#     root.left.right = Node(5)
#     root.right.left = Node(6)
#     root.right.right = Node(7)

#     print("Preorder traversal of binary tree is")
#     printPreorder(root)

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Convert the list of digits to an integer
        num = 0
        x = len(digits)
        for i in range(x):
            num += digits[i] * (10 ** (x - i -1))
        
        # Add 1 to the integer
        print(num)
        last_num = int(num) + int(1)
        print(last_num)
        # Convert the result back to a list of digits
        return [int(digit) for digit in str(last_num)]

# Test with input [1, 2, 3]
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
