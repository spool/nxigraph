"""
Provides a toolkit for interoperability between igraph and networkx
"""

import networkx
import igraph

class SGraph(networkx.Graph):
    """
    Extends the networkx Graph class with an igraph property.

    g = SGraph()
    g.igraph.average_path_length()
    """

    @property
    def igraph(self):
        d = {}
        adj = self.adj
        for i, k in enumerate(adj.keys()):
            d[k] = i
        l = [(d[t[0]], d[t[1]]) for t in self.edges()]
        g = igraph.Graph(l)
        return g
