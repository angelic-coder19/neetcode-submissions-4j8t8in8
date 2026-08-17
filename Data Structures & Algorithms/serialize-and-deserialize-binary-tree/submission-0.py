# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#"

        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"
        
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "#":
            return None
        
        nodes = data.split(",")
        next_right = 0
        
        def buildTree(idx):
            nonlocal nodes, next_right

            if nodes[idx] == "#":
                next_right = idx
                return None
            
            node = TreeNode(int(nodes[idx]))
            node.left = buildTree(idx + 1)
            node.right = buildTree(next_right + 1)

            return node
        
        return buildTree(0)

