from mimetypes import init
from collections import deque
from turtle import left

class Node:
  def __init__(self, data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right


class TreeSet:
  def __init__(self, initial_array):
    self.head = None
    self._build_bst(initial_array)
  

  def _insert(self, current_node, node):
    if (node.data < current_node.data ):
      if current_node.left == None:
        current_node.left = node
      else:
        self._insert(current_node.left, node)
    elif ( node.data > current_node.data):
      if current_node.right == None:
        current_node.right = node
      else:
        self._insert(current_node.right, node)
    else:
      return

  
  def put(self, data):
    if (self.head == None):
      self.head = Node(data)
    else:
      self._insert(self.head, Node(data))

  def _build_bst(self, initial_array):
    for item in initial_array:
      self.put(item)

  def _search(self, current_node, data):
    if ( not current_node):
      return False
    if current_node.data == data:
      return True
    
    present_left, present_right = False, False

    if data < current_node.data:
      present_left = self._search(current_node.left, data)
      if (present_left):
        return True
    
    if data > current_node.data:
      present_right = self._search(current_node.right, data)
    
    return present_left or present_right
    

  def exists(self, data):
    return self._search(self.head, data)


  def lower(self, data):
    (_, predecessor) = self._search_node_with_predecessor(data)
    return predecessor and predecessor.data



      
  def higher(self, data):
      (_, successor) = self._search_node_with_successor(data=data)
      return successor and successor.data

  def _search_node_with_successor(self, data=None, node=None):
    if (data):
      node = self.head
    
    if not node:
      return (None, None)

    stack = deque([])
    stack.append((node, False))
    successor = None
    item_found = False
    successor = None
    item = None
    while(len(stack)):
      (top, left_processed) = stack.pop()
      if top.data == data:
        item_found = True
        item = top
      
      if not left_processed:
        stack.append((top, True))
        if (top.left and top.data != data):
          stack.append((top.left, False))
      elif left_processed:
        if item_found and top.data != data:
          successor = top
          break
        else:
          if (top.right):
            stack.append((top.right, False))

    return (item, successor)



  def _search_node_with_predecessor(self, data):
    if not self.head:
      return (None, None)

    stack = deque([])
    predecessor = None
    node = None
    stack.append((self.head, False))

    while(len(stack)):
      (top, left_processed) = stack.pop()
      if not left_processed:
        stack.append((top, True))
        if (top.left):
          stack.append((top.left, False))
      else:
        if top.data == data:
          node = top
          break
        else:
          predecessor = top
        
        if (top.right):
          stack.append((top.right, False))

    return (node, predecessor)

  def _search_node_with_parent(self, current, parent, data):

    if current.data == data:
      return (current, parent)

    if (data < current.data):
      if (current.left):
        return self._search_node_with_parent(current.left, current)
      else:
        return (None, None)
    else:
      if (current.right):
        return self._search_node_with_parent(current.right, current)
      else:
        return (None, None)

    
    

    

        
        

tree_set = TreeSet([100, 50, 120, 30, 75, 60, 90, 80, 110, 130])
tree_set.put(20)
print(tree_set.exists(20))
print(tree_set.higher(75))
print(tree_set.lower(100))

        





  

