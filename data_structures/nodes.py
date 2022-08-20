class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  def set_link_node(self, link_node):
    self.link_node = link_node
    
  def get_link_node(self):
    return self.link_node
  
  def get_value(self):
    return self.value

# Add your code below:
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")
# link yacko with dot 
yacko.set_link_node(dot)
# link dot with wacko
dot.set_link_node(wacko)
# wacko link_node = None

# create two new variables dots_data and wackos_data
dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()
# use both getter methods to get dot's and wacko's value using their link_node
# get dot's value from yacko 
# get wacko's value from dot
# print dots_data and wackos_data
print(dots_data)
print(wackos_data)