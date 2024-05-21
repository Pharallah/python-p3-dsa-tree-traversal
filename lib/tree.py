import ipdb

class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      # Pop the root, save in node variable
      node = nodes_to_visit.pop(0)
      # If id of current node == id -> append & return
      if node['id'] == id:
        result.append(node)
        return result[0]
      # Else, append the node's children to NTV
      nodes_to_visit = node['children'] + nodes_to_visit

    # No matches? Return None
    return None

























  # def get_element_by_id(self, input_str):
  #   result = []
  #   nodes_to_visit = [self.root]

  #   while len(nodes_to_visit) > 0:
  #     node = nodes_to_visit.pop(0)
  #     if node['id'] == input_str:
  #       result.append(node)
  #       return result[0]
  #     nodes_to_visit = node['children'] + nodes_to_visit

  #   return None


# Like the browser's getElementById method, your method should take a string as an argument and return the node with that value. If a matching node is not found, your method should return None.
