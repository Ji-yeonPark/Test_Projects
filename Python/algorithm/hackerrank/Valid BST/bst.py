class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        node = TreeNode(value)

        if not self.root:
          self.root = node
        else:
          self.insertRec(self.root, node)
    
    def insertRec(self, latestRoot, node):

        if latestRoot.val > node.val:
            if not latestRoot.left:
              latestRoot.left = node
            else:
              self.insertRec(latestRoot.left, node)
        
        else:
          if not latestRoot.right:
            latestRoot.right = node
          else:
            self.insertRec(latestRoot.right, node)
    
    def printPreorder(self):
      self.array = []

      self.printPreOrderRec(self.root)
      return self.array
    

    def printPreOrderRec(self, currentRoot):
        if currentRoot:
          self.array.append(currentRoot.val)
          self.printPreOrderRec(currentRoot.left)
          self.printPreOrderRec(currentRoot.right)


a = [3,2,1,5,4]

bst = BinarySearchTree()

for i in a:
  bst.insert(i)

if bst.printPreorder() == a:
  print("YES")
else:
  print("NO")