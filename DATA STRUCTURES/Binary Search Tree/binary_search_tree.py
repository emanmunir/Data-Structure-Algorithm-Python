
class Tree:
    def __init__(self, data, l_child = None, r_child = None) -> None:
        self.data = data
        self.left = l_child
        self.right = r_child
        
# class BinarySearchTree:
    
#     def __init__(self) -> None:
#         pass
    
    def insert(self, val):
        
        if self.data:            
            if val < self.data:                
                if self.left is None:                    
                    self.left = Tree(val)                    
                else:                    
                    self.left.insert(val)                    
            elif val > self.data:                
                if self.right is None:                    
                    self.right = Tree(val)                    
                else:                    
                    self.right.insert(val)            
            else:                
                self.data = val
          
    def search(self, val):
        
        if val < self.data:
            
            if self.left is None:
                
                return str(val) + ' Value not found'
            
            return self.left.search(val)
            
        elif val > self.data:
            
            if self.right is None:
                
                return str(val) + ' Value not found'
            
            return self.right.search(val)
            
        if val == self.data:
            
            return str(val) + ' is in the list \'hehe\' '
            
            
    def traverse_in_order(self):
        if self.left :
            self.left.traverse_in_order()
        print(self.data, end =' ')
        if self.right:
            self.right.traverse_in_order()
            
            
    def traverse_pre_order(self):
        print(self.data)
        if self.left :
            self.left.traverse()
        if self.right:
            self.right.traverse()
            
            
    # Find the inorder successor
    def minValueNode(self, node):
        current = node

        # Find the leftmost leaf
        while(current.left is not None):
            current = current.left

        return current 
           
        # Deleting a node
        
    def deleteNode(self, key):
        temp = self.root
        hehe = self.deleteNode_aux(self, temp, key)
        self.root = hehe
        
    def deleteNode_aux(self, root, key):

        # Return if the tree is empty
        if root is None:
            return root

        # Find the node to be deleted
        if key < root.data:
            root.left = self.deleteNode_aux(root.left, key)
        elif(key > root.data):
            root.right = self.deleteNode_aux(root.right, key)
        else:
            # If the node is with only one child or no child
            if root.left is None:
                temp = root.right
                root = None 
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # If the node has two children,
            # place the inorder successor in position of the node to be deleted
            temp = self.minValueNode(root.right)

            root.data = temp.data

            # Delete the inorder successor
            root.right = self.deleteNode_aux(root.right, temp.data)

        return root

                    
                
    
    def height(self):
        pass
            
            
            
            