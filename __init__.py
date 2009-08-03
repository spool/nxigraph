"""
Provides a toolkit for interoperability between igraph and networkx

>>> h = networkx.erdos_renyi_graph(30, .6)
>>> g = NXiGraph(h)
>>> networkx.clustering(g) == networkx.clustering(h)
True
>>> networkx.diameter(g) == g.igraph.diameter() == networkx.diameter(h)
True
"""

import networkx
import igraph

class NXiGraph(networkx.Graph):
    """
    Extends the networkx Graph class with an igraph property.

    >>> g = NXiGraph()
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
    def node_dict(self):
        d = {}
        for i, k in enumerate(self.adj.keys()):
            d[k] = i
        return d

    @property
    def igraph(self):
        l = [(self.node_dict[t[0]], self.node_dict[t[1]]) for t in self.edges()]
        g = igraph.Graph(l)
        g.vs["name"] = [str(i) for i in self.nodes()]
        return g
        #return igraph.Graph(l)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

