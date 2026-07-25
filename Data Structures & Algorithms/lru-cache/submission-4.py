class Node:
    
    def __init__(self, val, key=None, prev=None, next=None): 
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.keys = dict()
        self.capacity = capacity
        self.Left = Node(0)
        self.Right = Node(0)
        self.Left.next = self.Right
        self.Right.prev = self.Left

    def get(self, key: int) -> int:
        # If the key exists and is valid
        try: 
            node = self.keys[key]

            # Set this to the MRU side of the cache
            self.remove(node) 
            self.insert(node) 

            return node.val
        
        # When the index is invalid 
        except KeyError:
            
            return -1

    def put(self, key: int, value: int) -> None:

        # When the key already exists in the dict, update
        try: 
            node = self.keys[key]
            node.val = value

            # Move this node the MRU
            self.remove(node)
            self.insert(node)

        # When the key is new, create and add to dict
        except KeyError:
            
            node = Node(value, key)
            ptr = node

            self.keys[key] = ptr

            # Add to MRU side
            self.insert(node)

            # Check for exceeded capacity
            if len(self.keys) > self.capacity:
                
                # Get node on the LRU side
                node = self.Left.next
                self.remove(node) 

                # Orphan node
                node.next = None
                node.prev = None

                # Delete the node from dict
                del self.keys[node.key]

    def remove(self, node):
        # Bridge this node's previous and next neighbours
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node): 
        # Add this node to the Most Recently Used (MRU) side of the cache
        node.next = self.Right
        node.prev = self.Right.prev
        self.Right.prev.next = node
        self.Right.prev = node


