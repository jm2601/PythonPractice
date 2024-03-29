# Define your Node class below:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

# my_node = Node(44)
# print(my_node.get_value())

# Create your LinkedList class below:
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)

  def get_head_node(self):
    return self.head_node

# Add your insert_beginning and stringify_list methods below:
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    # setting new_node as head_node using .set_next_node() from Node class
    new_node.set_next_node(self.head_node)
    # replacing current head_node with new_node
    self.head_node = new_node

  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  

# Test your code by uncommenting the statements below - did your list print to the terminal?
# ll = LinkedList(5)
# ll.insert_beginning(70)
# ll.insert_beginning(5675)
# ll.insert_beginning(90)
# print(ll.stringify_list())

# Define your remove_node method below:
  def remove_node(self, value_to_remove):
   current_node = self.get_head_node()
   if (current_node.get_value() == value_to_remove):
     self.head_node = current_node.get_next_node()
   else:
     while current_node:
       next_node = current_node.get_next_node()
       if next_node.get_value() == value_to_remove:
         current_node.set_next_node(next_node.get_next_node())
         current_node = None
       else:
         current_node = next_node

# Create a few nodes and adding them to a new linked list
# Print your linked list out by using your stringify_list() method
# Remove your linked list’s head node
# Print your list again — was your original head node removed?
# So far you’ve built a method to remove the first occurrence of a given value. How do you think you would remove all nodes that have a specific value? 
# Try building a method to do that!

# def remove_node(self, node_to_remove):
#     current_node = self.head_node
#     if current_node == node_to_remove:
#       self.head_node = current_node.next_node
#     else:
#       while current_node:
#         next_node = current_node.next_node
#         if next_node == node_to_remove:
#           # --------> what line of code goes here?
#           current_node = None
#         else:
#           current_node = next_node