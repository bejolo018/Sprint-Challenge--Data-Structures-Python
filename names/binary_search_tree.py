class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    current_tree = self

    checking = True

    while checking is True: 
     
      if value >= current_tree.value and current_tree.right:
        current_tree = current_tree.right
    
      elif value < current_tree.value and current_tree.left:
        current_tree = current_tree.left
     
      elif value >= current_tree.value and not current_tree.right:
        current_tree.right = BinarySearchTree(value)
        checking = False
      
      elif value < current_tree.value and not current_tree.left:
        current_tree.left = BinarySearchTree(value)
        checking = False

  def contains(self, target):
    current_tree = self

    checking = True

    while checking is True:
      if current_tree.value == target:
        checking = False
        return True
      elif target >= current_tree.value and current_tree.right:
        current_tree = current_tree.right
      elif target < current_tree.value and current_tree.left:
        current_tree = current_tree.left
      elif target >= current_tree.value and not current_tree.right:
        return False
      elif target < current_tree.value and not current_tree.left:
        return False
        
  def get_max(self):
      if self.right:
        return self.right.get_max()
      else:
        return self.value

  def for_each(self, cb):
    cb(self.value)
    
    if self.left:
        self.left.for_each(cb)
    if self.right:
        self.right.for_each(cb)