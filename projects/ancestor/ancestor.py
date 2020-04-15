# Let's import our util function and graph class
import sys
sys.path.append('../graph')
from util import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # Create our graph
    graph = Graph()
    
    # Add vertices to graph
    for node_pairs in ancestors:
        # Get parent and child from ancestors pairs
        parent = node_pairs[0]
        child = node_pairs[1]
        # Add vertices to graph
        graph.add_vertex(parent)
        graph.add_vertex(child)
        # Add directions
        # Since we want to traverse *up* the list we will point the child -> parent -> grandparent
        graph.add_edge(child, parent)

    
    qq = Queue()
    qq.enqueue([starting_node])

    # Used to control when the longest len has been reached
    longest_len = 1
    # Return negative 1 if no parent nodes exist
    earliest_ancestor = -1

    while qq.size() > 0:
        path = qq.dequeue()
        vertex = path[-1]
        
        if len(path) > longest_len:
            longest_len = len(path)
            earliest_ancestor = vertex

        parents = graph.vertices[vertex]
        for parent in parents:
            copy_path = list(path)
            copy_path.append(parent)
            qq.enqueue(copy_path)
    
    return earliest_ancestor