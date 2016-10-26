import networkx as nx

G = nx.Graph()

G.add_node(1)

G.add_nodes_from([2, 3])

G.add_edge(1, 2)

print G.nodes()


nx.draw(G)

print nx.info(G)
