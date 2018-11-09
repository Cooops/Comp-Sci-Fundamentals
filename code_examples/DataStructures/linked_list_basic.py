###########################################
# Outline Node class and define functions #
###########################################

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

def insertNode(head, valuetoInsert):
    currentNode = head
    while currentNode:  # same as `is not None`
        while not currentNode.nextNode:  # same as `is None`
            currentNode.nextNode = Node(valuetoInsert)
            return head
        currentNode = currentNode.nextNode

def deleteNode(head, valueToDelete):
    currentNode = head
    previousNode = None
    while currentNode:
        if currentNode.value == valueToDelete:
            if not previousNode:
                newHead = currentNode.nextNode
                currentNode.nextNode = None
                return newHead
            previousNode.nextNode = currentNode.nextNode
            return head
        previousNode = currentNode
        currentNode = currentNode.nextNode
    return head

def traverseNode(currentNode):
    while currentNode:
        print(currentNode.value)
        currentNode = currentNode.nextNode

def buildAndTraverse():
    currentNode = head
    traverseNode(currentNode)

#####################
# Create base nodes #
#####################

firstNode = Node("5")
secondNode = Node("13")
thirdNode = Node("2")

firstNode.nextNode = secondNode # firstNode -> secondNode , "5" -> "13"
secondNode.nextNode = thirdNode # secondNode -> thirdNode , "13" -> "2"

# set head (root) Node equal to the first node, which is "5" in this case
head = firstNode

######################
# Traverse the nodes #
######################

buildAndTraverse()
print()

#################
# Delete a Node #
#################

nodeToDelete = '13'
print(f"Deleting new Node: {nodeToDelete} and traversing updated Linked List.")
newHead = deleteNode(head, nodeToDelete)
buildAndTraverse()
print()

#################
# Insert a Node #
#################

nodeToInsert = '99'
print(f"Inserting new Node: {nodeToInsert} and traversing updated Linked List.")
newHead = insertNode(newHead, nodeToInsert)
buildAndTraverse()