# class Node:
# 	def __init__(self, value):
# 		self.value = value
# 		self.next = None

# # class SList:
# # 	def __init__(self, value):
# # 		node = Node(value)
# # 		self.head = node

# node1 = Node(5)
# node2 = Node(9)
# node3 = Node(11)

# node1.next = node2
# node2.next = node3

# # runner = node1

# # while (runner):
# # 	print(runner.value)
# # 	runner = runner.next

# slist = SList(7)
# sList1 = SList(9)

# class SList:	
# 	def __init__(self, value):
# 		node = Node(value)
# 		self.head = node

# 	def printAllValues(self):
# 		runner = self.head #runner point to where self.head is pointing to
# 		while(runner.next != None):
# 			print(runner.value)
# 			runner = runner.next
# 		print(runner.value)

# 	def addNode(self, value):
# 		runner = self.head
# 		while(runner.next != None):
# 			runner = runner.next
# 		node = Node(10)
# 		runner.next = node

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node
     
    def printAllValues(self, msg=""):
        runner = self.head          # create a runner     
        print("head points to ", id(self.head))
        print("Printing the values in the list ---", msg,"---")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next        
        print(id(runner), runner.value, id(runner.next))
      
print("\n\n\n\n================== START OF THE PROGRAM ================")       
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
     
list.printAllValues("Attempt 1")
