"""
Provides a toolkit for interoperability between igraph and networkx
"""
import networkx
import igraph

def nx2igraph(nxgraph):
    """
    Converts a networkx graph to an igraph graph.
    """
    d = {}
    adj = nxgraph.adj
    for i, k in enumerate(adj.keys()):
        d[k] = i
    l = [(d[t[0]], d[t[1]]) for t in nxgraph.edges()]
    return(igraph.Graph(l))

class SGraph(networkx.Graph):
    """
    Extends the networkx Graph class with an igraph property.

    >>> g = SGraph()
    >>> edgelist = [('blue', 'purple'),
    ...                 ('blue', 'green'),
    ...                 ('blue', 'red'),
    ...                 ('yellow', 'green'),
    ...                 ('green', 'orange')]
    >>> g.add_edges_from(edgelist)
    >>> networkx.diameter(g)
    3
    >>> g.igraph.diameter()
    3
    >>> g.add_edge('orange', 'mauve')
    >>> networkx.diameter(g)
    4
    >>> g.igraph.diameter()
    4
    """
    @property
    def igraph(self):
        return nx2igraph(self)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

