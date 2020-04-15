"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {} # This is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2
        """
        # Check if they exist
        if v1 in self.vertices and v2 in self.vertices:
            # Add the edge
            self.vertices[v1].add(v2)
        else:
            raise ValueError('Vertex does not exist')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None
            # Might want to raise an exception here instead

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # # Create a queue and enqueue starting vertex
        # qq = Queue()
        # qq.enqueue([starting_vertex])
        # # Create a set of traversed vertices
        # visited = set()
        # # While queue is not empty:
        # while qq.size() > 0:
        #     # dequeue/pop the first vertex
        #     path = qq.dequeue()
        #     # if not visited
        #     if path[-1] not in visited:
        #         # DO THE THING!
        #         print(path[-1])
        #         # mark as visited
        #         visited.add(path[-1])
        #         # enqueue all neighbors
        #         for next_vert in self.get_neighbors(path[-1]):
        #             new_path = list(path)
        #             new_path.append(next_vert)
        #             qq.enqueue(new_path)

        # Why not do this instead?
        # After doing the later functions I see....
        qq = Queue()
        qq.enqueue(starting_vertex)
        visited = set()
        while qq.size() > 0:
            vertex = qq.dequeue()
            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for next_vert in self.get_neighbors(vertex):
                    qq.enqueue(next_vert)
        
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create stack
        ss = Stack()
        # Add starting vertex to stack
        ss.push(starting_vertex)
        # Create empty set to hold items already visited
        visited = set()
        # While stack is not empty
        while ss.size() > 0:
            # Get next item from stack
            node = ss.pop()
            # Check if item has been visited already
            if node not in visited:
                # If not, print it
                print(node)
                # and add it to visited set
                visited.add(node)
                for next_node in self.get_neighbors(node):
                    # Get neighbors of node and add them to the stack to iterate through next
                    ss.push(next_node)

    def dft_recursive(self, vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initial run
        if visited is None:
            visited = set()
        # Can't think of how to do this without setting visited as a parameter
        # If vertex not visited yet, add to set and print
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)
            # Recursivly do the same for neighbors of vertex (DEPTH first, so it moves down the tree)
            for i in self.get_neighbors(vertex):
                self.dft_recursive(i, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create queue
        qq = Queue()
        # Enqueue starting vertex PATH (will use path to build list for return)
        qq.enqueue([starting_vertex])
        # Create set for visited items
        visited = set()
        while qq.size() > 0:
            path = qq.dequeue()
            # Item from end of path
            vertex = path[-1]
            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    return path
                else:
                    for neighbor in self.get_neighbors(vertex):
                        new_path = list(path)
                        new_path.append(neighbor)
                        qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create stack
        ss = Stack()
        # Push starting vertex PATH (will use path to build list for return)
        ss.push([starting_vertex])
        # Create set for visited items
        visited = set()
        while ss.size() > 0:
            path = ss.pop()
            # Item from end of path
            vertex = path[-1]
            if vertex not in visited:
                visited.add(vertex)
                if vertex == destination_vertex:
                    return path
                else:
                    for neighbor in self.get_neighbors(vertex):
                        new_path = list(path)
                        new_path.append(neighbor)
                        ss.push(new_path)

    def dfs_recursive(self, vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initial run
        if visited is None:
            visited = set()
        if path is None:
            path = []
        # Rename starting_vertex because of recursion later
        # Again I can't see how to do this without declaring visited and path as parameters
        # Check if vertex in visited
        if vertex not in visited:
            # Append vertex to path
            # But need to create a copy of path otherwise you end up with all elements
            copy_path = list(path)
            copy_path.append(vertex)
            # Add vertex to visited set
            visited.add(vertex)
            # Check if at destination
            if vertex == destination_vertex:
                # If so, return the path
                return copy_path
            # else recursively iterate through neighbors
            for neighbor in self.get_neighbors(vertex):
                # Create new path that will eventually hold list of path from vertex to destination
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, copy_path)
                # If new_path exists (i.e. there are neighbors and you haven't reached destination)
                if new_path:
                    return new_path
                

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
