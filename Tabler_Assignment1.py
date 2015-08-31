# Ryan Tabler
# CSCI 3202
# Assignment 1

import queue

# Please use Python 3 to run this python script
# (in Python 3, Queue was renamed to queue)


# 1. Queue
class Queue:
    def __init__(self):
        self.queue = queue.Queue()

    def enqueue(self, value):
        if type(value) is int:
            self.queue.put(value)
            return True
        else:
            print("This queue supports only integers")
            return False

    def dequeue(self):
        return self.queue.get()

    def empty(self):
        return self.queue.empty()

# 2. Stack
class Stack:
    def __init__(self):
        self.L = list()

    def push(self, num):
        self.L.append(num)
        return True

    def pop(self):
        return self.L.pop()

    def checkSize(self):
        return len(self.L)

# 3. Binary Tree
class TreeNode:
    def __init__(self, key, parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
    
    def __str__(self):
        # Recursively collect all values in a string
        base = str(self.key)
        if self.left != None:
            base += ", "
            base += str(self.left)
        if self.right != None:
            base += ", "
            base += str(self.right)
        return base

class Tree:
    def __init__(self, key):
        self.root = TreeNode(key, None)

    def add(self, value, parentValue):
        # Breadth-first search of Trees using a Queue
        # Beginning with the root node
        nodes = [self.root]
        while len(nodes):
            thisNode = nodes[0]

            # Check every Tree node for the parent value
            if thisNode.key == parentValue:
                if thisNode.left == None:
                    thisNode.left = TreeNode(value, thisNode)
                    return True
                elif thisNode.right == None:
                    thisNode.right = TreeNode(value, thisNode)
                    return True
                else:
                    print("Parent has two children, node not added")
                    return False

            # Push this node's children, pop this node
            # And don't increment index (0)
            if thisNode.left != None:
                nodes.append(thisNode.left)
            if thisNode.right != None:
                nodes.append(thisNode.right)
            nodes.pop(0)

        print("Parent not found")
        return False

    def delete(self, value):
        # Breadth-first search of Trees using a Queue
        # Beginning with the root node
        nodes = [self.root]
        while len(nodes):
            thisNode = nodes[0]

            if thisNode.key == value:
                if thisNode.left == None and thisNode.right == None:
                    if thisNode.parent.left == thisNode:
                        thisNode.parent.left = None
                        del thisNode
                        return True
                    elif thisNode.parent.right == thisNode:
                        thisNode.parent.right = None
                        del thisNode
                        return True
                    else:
                        print("Error: Tree is malformed")
                        del thisNode
                        return False   
                else:
                    print("Node not deleted, has children")
                    return False

            # Push this node's children, pop this node
            # And don't increment index (0)
            if thisNode.left != None:
                nodes.append(thisNode.left)
            if thisNode.right != None:
                nodes.append(thisNode.right)
            nodes.pop(0)

        print("Node not found")
        return False

    def printTree(self):
        print("[" + str(self.root) + "]")

# 4. Graph
class Graph:
    def __init__(self):
        self.dict = {}

    def addVertex(self, value):
        if value in self.dict:
            print("Vertex already exists.")
            return False
        else:
            # Create a new key from value, and have it map to
            # a blank list, to store adjacent edges
            self.dict[value] = []
            return True

    def addEdge(self, value1, value2):
        if (value1 not in self.dict) or (value2 not in self.dict):
            print("One or more vertices not found.")
            return False
        else:
            if value2 in self.dict[value1] or value1 in self.dict[value2]:
                print("Edge already in Graph")
                return False
            else:
                # Add each node to the other's list of adjacent edges
                self.dict[value1].append(value2)
                self.dict[value2].append(value1)
                return True

    def findVertex(self, value):
        if value in self.dict:
            print(self.dict[value])
            return True
        else:
            print("Vertex not found")
            return False

def main():

    print("Ryan Tabler")
    print("CSCI 3202")
    print("Assignment 1")
    print("")

    # Testing MyQueue
    print("Testing: Queue")
    myQueue = Queue()
    print("Adding these 10 values to MyQueue:")
    valuesToEnqueue = [i for i in range(10)]
    print(valuesToEnqueue)
    for i in valuesToEnqueue:
        myQueue.enqueue(i)
    print("Dequeueing values now:")
    while not myQueue.empty():
        print(myQueue.dequeue())
    print("")

    # Testing Stack
    print("Testing: Stack")
    myStack = Stack()
    print("Pushing these 10 values to the stack:")
    valuesToPush = [i for i in range(10)]
    print(valuesToPush)
    for i in valuesToPush:
        myStack.push(i)
    print("Popping values now:")
    while myStack.checkSize() != 0:
        print(myStack.pop())
    print("")

    # Testing Tree
    print("Testing: Tree")
    myTree = Tree(10000)
    print("Tree after adding 10 values:")
    myTree.add(11000, 10000)
    myTree.add(12000, 10000)
    myTree.add(11100, 11000)
    myTree.add(11200, 11000)
    myTree.add(11110, 11100)
    myTree.add(11210, 11200)
    myTree.add(11220, 11200)
    myTree.add(12100, 12000)
    myTree.add(12110, 12100)
    myTree.add(12111, 12110)
    myTree.printTree()
    print("Tree after deleting 2 values:")
    myTree.delete(11110)
    myTree.delete(11210)
    myTree.printTree()
    print("Attempting to delete 2 un-deletable values:")
    myTree.delete(10000)
    myTree.delete(12100)
    print("Attempting to delete 1 value that dosen't exist:")
    myTree.delete(11111)
    print("Tree now:")
    myTree.printTree()
    print("")

    # Testing the Graph
    print("Testing: Graph")
    myGraph = Graph()
    print("Adding 10 values as vertices to the graph:")
    valuesToAdd = [i for i in range(10)]
    for i in valuesToAdd:
        myGraph.addVertex(i)
    print("Adding these 20 edges to the graph:")
    edgesToAdd = [(0,1), (2,3), (4,5), (6,7), (8,9),
                  (0,2), (0,3), (0,4), (0,5), (0,6),
                  (0,7), (0,8), (0,9), (2,4), (2,6),
                  (2,8), (4,6), (4,8), (6,8), (3,7)]
    for i in edgesToAdd:
        myGraph.addEdge(i[0],i[1])
    print("Find 5 vertices in the graph:")
    print("Vertex 0 should have edges [1,2,3,4,5,6,7,8,9]:")
    myGraph.findVertex(0)
    print("Vertex 1 should have edges [0]:")
    myGraph.findVertex(1)
    print("Vertex 3 should have edges [0,2,7]:")
    myGraph.findVertex(3)
    print("Vertex 6 should have edges [0,2,4,7,8]:")
    myGraph.findVertex(6)
    print("Vertex 9 should have edges [0,8]:")
    myGraph.findVertex(9)
    print("")

    print("Testing complete")

if __name__ == "__main__":
    main()


