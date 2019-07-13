
class Node(object):

	def __init__(self, data):
		self.data = data;
		self.leftChild = None;
		self.rightChild = None;
		
class BinarySearchTree(object):

	def __init__(self):
		self.root = None;
		
	def insert(self, data):
		if not self.root:
			self.root = Node(data);
		else:
			self.insertNode(data, self.root);
			
	# O(logN)   if the tree is balanced !!!!!!!!!!!!!  --> it can reduced to O(N) --> AVL RBT are needed !!!!!
	def insertNode(self, data, node):
	
		if data < node.data:
			if node.leftChild:
				self.insertNode(data, node.leftChild);
			else:
				node.leftChild = Node(data);
		else:
			if node.rightChild:
				self.insertNode(data, node.rightChild);
			else:
				node.rightChild = Node(data);
	
	# O(logN)	
	def removeNode(self, data, node):
	
		if not node:
			return node;
			
		if data < node.data:
			node.leftChild = self.removeNode(data, node.leftChild);
		elif data > node.data:
			node.rightChild = self.removeNode(data, node.rightChild);
		else:
			
			if not node.leftChild and not node.rightChild:
				print("Removing a leaf node...");
				del node;
				return None;
				
			if not node.leftChild:  # node !!!
				print("Removing a node with single right child...");
				tempNode = node.rightChild;
				del node;
				return tempNode;
			elif not node.rightChild:   # node instead of self
				print("Removing a node with single left child...");
				tempNode = node.leftChild;
				del node;
				return tempNode;
    
			
			print("Removing node with two children....");
			tempNode = self.getPredecessor(node.leftChild);   # self instead of elf  + get predecessor 
			node.data = tempNode.data;
			node.leftChild = self.removeNode(tempNode.data, node.leftChild);
		
		return node;   # !!!!!!!!!!!!

	def getPredecessor(self, node):
	
		if node.rightChild:
			return self.getPredeccor(node.rightChild);
			
		return node;
		
	def remove(self, data):
		if self.root:
			self.root = self.removeNode(data, self.root);
			
		# O(logN)
	def getMinValue(self):
		if self.root:
			return self.getMin(self.root);
			
	def getMin(self, node):
	
		if node.leftChild:
			return self.getMin(node.leftChild);
			
		return node.data;
		
		# O(logN)
	def getMaxValue(self):
		if self.root:
			return self.getMax(self.root);
			
	def getMax(self, node):
	
		if node.rightChild:
			return self.getMax(node.rightChild);
			
		return node.data;
		
	def traverse(self):
		if self.root:
			self.traverseInOrder(self.root);
			
			# O(N)
	def traverseInOrder(self, node):
	
		if node.leftChild:
			self.traverseInOrder(node.leftChild);
			
		print("%s " % node.data);
		
		if node.rightChild:
			self.traverseInOrder(node.rightChild);
        
        
    
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)

print(bst.getMinValue())
print(bst.getMaxValue())
bst.traverse()
  

bst2 = BinarySearchTree()
bst2.insert("C")
bst2.insert("A")
bst2.insert("Z")
bst2.insert("G")
bst2.traverse()

bst3 = BinarySearchTree()
bst3.insert(10)
bst3.insert(13)
bst3.insert(5)
bst3.insert(1)
bst3.remove(5)
bst3.traverse()

bst4 = BinarySearchTree()
bst4.insert(10)
bst4.insert(13)
bst4.insert(5)
bst4.insert(14)
bst4.remove(13)
bst4.traverse()

bst5 = BinarySearchTree()
bst5.insert(10)
bst5.insert(13)
bst5.insert(5)
bst5.insert(14)
bst5.remove(10)
bst5.traverse()