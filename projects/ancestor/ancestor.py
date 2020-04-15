# Let's import our util function and graph class
import sys
sys.path.append('../graph')
from util import Queue
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    
    # Create our graph
    graph = Graph()
    
    # Add vertices to graph
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
        # Add directions
        # Since we want to traverse *up* the list we will point the child -> parent -> grandparent
        graph.add_edge(child, parent)

    qq = Queue()
    qq.enqueue([starting_node])

    # longest_len = 1
    # # Return negative 1 if no parent nodes exist
    # earliest_ancestor = -1

    print(graph.get_neighbors(3))
    if len(graph.get_neighbors(starting_node)) == 0:
        return -1
         
    else:
        while qq.size() > 0:
            print('hi')
            path = qq.dequeue()
            vertex = path[-1]

            # if len(path) >= longest_len :
            #     longest_len = len(path)
            #     earliest_ancestor = vertex

            parents = graph.get_neighbors(vertex)
            for parent in sorted(parents):
                copy_path = list(path)
                copy_path.append(parent)
                qq.enqueue(copy_path)
        return vertex

if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 3))