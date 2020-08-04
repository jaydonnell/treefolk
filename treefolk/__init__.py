def hello_world():
    print("hello from treefolk")

class Node:
    def __init__(self, id, label, types = []):
        self.id = id
        self.label = label
        self.types = types
        
    def to_cyto_node(self):
        return {  'data': {
                  'id': self.id,
                  'label': self.label,
                  'classes': self.types
               }}

    def __str__(self):
        return str({
                  'id': self.id,
                  'label': self.label,
                  'types': self.types
               })
    
class Edge:
    def __init__(self, id, source, target):
        self.id = id
        self.source = source
        self.target = target

    def to_cyto_edge(self):
        return {
            'data': {
                'id': self.id,
                'source': self.source,
                'target': self.target,
            }
        }

    def __str__(self):
        return str({
                'id': self.id,
                'source': self.source,
                'target': self.target,
            })