class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_path(root, goal):
  def helper(root,goal,path):
    if not root: return False
    if root.val == goal: return True
    if helper(root.left,goal,path): 
      path.append('left')
      return True
    if helper(root.right,goal,path): 
      path.append('right')
      return True
    if path: path.pop()
    return False
  path = []
  helper(root,goal,path)
  path.reverse()
  return path