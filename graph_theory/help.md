# [graph theory](http://www.python-course.eu/graphs_python.php)



arc: directed edge

node/vertices

edge

```
graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }



#get all edge

def generate_edges(graph):
    edges = []
    for node in graph:
        for neighbour in graph[node]:
            edges.append((node, neighbour))

    return edges

print(generate_edges(graph))

#get all isolated node

def find_isolated_nodes(graph):
    """ returns a list of isolated nodes. """
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated += node
    return isolated

#find path
def find_path(graph,start_vertex, end_vertex, path=None):
    """ find a path from start_vertex to end_vertex
        in graph """
    if path == None:
        path = []
    path = path + [start_vertex]
    if start_vertex == end_vertex:
        return path
    if start_vertex not in graph:
        return None
    for vertex in graph[start_vertex]:
        if vertex not in path:
            extended_path = find_path(graph, vertex,end_vertex, path)
            if extended_path:
                return extended_path
    return None
```
