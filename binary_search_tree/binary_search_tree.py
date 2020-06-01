"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTNode(value)

        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return self.value
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        # elif target < self.data and self.left


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        
        if self.left:
            self.left.for_each(fn)
        
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if self.left is not None:
            self.left.in_order_print(self.left)
        print(node.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        #make a queue
        queue = []

        #enqueue the node
        queue.append(node)

        #as long as the queue is not empty
        while len(queue) > 0:
            ##dequeue from the front of the queue, this is our current node
            node = queue.pop(0)
            print(node.value)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        

        
        
        
        
        ##enqueue the kids of the current node on the stack


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        #make a stacc
        stack = []

        #push the node on the stacc
        stack.append(node)
        #as long as the stacc is thicc
        while len(stack) > 0:
        ##pop off the stacc, this is our current node
            node = stack.pop()
            print(node.value)
            
        ##the kids, check that they are not None, and put them on the stacc
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        stack = []

        #push the node on the stacc
        stack.append(node)
        #as long as the stacc is thicc
        while len(stack) != 0:
        ##pop off the stacc, this is our current node
            node = stack.pop()
            print(node.value)
            
        ##the kids, check that they are not None, and put them on the stacc
            print(node.value)
            if node.left is not None:
                stack.append(node.left)
            
            if node.right is not None:
                stack.append(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        stack = []

        #push the node on the stacc
        stack.append(node)
        #as long as the stacc is thicc
        while len(stack) != 0:
        ##pop off the stacc, this is our current node
            node = stack.pop()

            
        ##the kids, check that they are not None, and put them on the stacc
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            return(node.value)