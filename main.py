import pathpy as pp
import numpy as np
import matplotlib.pyplot as plt

# %% Networks objects

n1 = pp.Network()
print(n1)

n2 = pp.Network(directed=True)
print(n2)

n = pp.Network(directed=True)
n.add_node('a')
n.add_node('b')
n.add_node('b')
n.add_edge('a', 'b')
n.add_edge('b', 'c')
print(n)

print(n.nodes)

print('d' in n.nodes)

n.add_edge('c', 'd')
n.add_edge('d', 'a')
print(n)

print('d' in n.nodes)

print('Number of nodes: {0}'.format(len(n.nodes)))
print('Number of edges: {0}'.format(len(n.edges)))

print(n.summary())

# %% Node and Edge objects

for v in n.nodes:
    print(v)

print(n.nodes['a'])

params = {'label_color': '#ff0000',
          'node_color': {'a': '#ff0000', 'b': '#00ff00', 'c': '#0000ff'}
          }

pp.visualisation.export_html(n, filename='1.html', **params)

n2.add_node('a')

for e in n.edges:
    print('---')
    print(e)

# %% Networks, Nodes and Edges with attributes

trolls = pp.Network(directed=False)
trolls.add_node('t')
trolls.add_node('b')
trolls.add_node('w')
trolls.add_edge('t', 'b', uid='t-b')
trolls.add_edge('t', 'w', uid='t-w')
print(trolls)

trolls.nodes['t']['name'] = 'Tom'
trolls.nodes['t']['age'] = 156
trolls.nodes['b']['name'] = 'Bert'
trolls.nodes['b']['age'] = 96
trolls.nodes['w']['name'] = 'William'
trolls.nodes['w']['age'] = 323

trolls.edges['t-b']['strength'] = 2.0
trolls.edges['t-b']['type'] = 'like'
trolls.edges['t-w']['strength'] = 5.0
trolls.edges['t-w']['type'] = 'dislike'

print(trolls.edges['t-b'])
print(trolls.edges['t-w'])

nx = pp.Network()
nx.add_edge('a', 'b')
nx.add_edge('b', 'a')
nx.add_edge('b', 'c')
nx.add_edge('d', 'c')
nx.add_edge('c', 'd')
nx.add_edge('c', 'b')
print(nx)

print(nx.edges[('a', 'b')]['weight'])

nx.add_edge('a', 'b', weight=2.0)
print(nx.edges[('a', 'b')]['weight'])

print(nx.adjacency_matrix().todense())

print(nx.degrees())
print(nx.ecount())
print(nx.ncount())

# %% Clustering coefficient

n = pp.Network(directed=True)
n.add_edge('a', 'b')
n.add_edge('b', 'd')
n.add_edge('a', 'e')
n.add_edge('a', 'd')
n.add_edge('d', 'e')
n.add_edge('d', 'f')
n.add_edge('e', 'f')


def local_cluster_coef(network, v):
    if network.directed and network.nodes[v]['outweight'] < 2:
        return 0.0
    if not network.directed and network.nodes[v]['degree'] < 2:
        return 0.0
    k_i = 0.0
    for i in network.successors[v]:
        for j in network.successors[v]:
            if (i, j) in network.edges:
                k_i += 1.0
    if not network.directed:
        return k_i / (network.nodes[v]['degree'] * (network.nodes[v]['degree'] - 1.0))
    return k_i / (network.nodes[v]['outweight'] * (network.nodes[v]['outweight'] - 1.0))


print(n.successors)

v = 'a'
local_cluster_coef(n, v)

# %% Interactive network visualisation in jupyter

params = {'label_color': '#ff0400',
          'label_size': '20',
          'node_color': {'a': '#ff0000', 'b': '#00ff00', 'c': '#0d00ff'},
          'node_size': {'a': '5', 'b': '10', 'c': '20'}
          }

pp.visualisation.export_html(nx, filename='2.html', **params)

class Graph:
    # init function to declare class variables
    def __init__(self, V, A):
        self.V = V
        self.adj = A

    def dfs(self, temp, v, visited):
        # Mark the current vertex as visited
        visited[v] = True
        # Store the vertex to list
        temp.append(v)
        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if not visited[i]:
                # Update the list
                temp = self.dfs(temp, i, visited)
        return temp

    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        connected_components = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if not visited[v]:
                temp = []
                connected_components.append(self.dfs(temp, v, visited))
        return connected_components


# Driver Code
if __name__ == "__main__":
    # получаю список списков.
    # где первый список это список элементов на которые ссылается первый элемент
    # второй где список это список элементов на которые ссылается первый элемент
    # и т.д.
    def connected_for_each_node(network):
        A = []
        for row in range(network.adjacency_matrix().toarray().shape[0]):
            temp = []
            for col in range(network.adjacency_matrix().toarray().shape[0]):
                if network.adjacency_matrix().toarray()[row][col] != 0:
                    temp.append(col)
            A.append(temp)
        return A


    n = pp.Network(directed=False)
    n.add_edge('a', 'd')
    n.add_edge('b', 'c')
    n.add_edge('c', 'd')

    n.add_edge('а', 'б')
    n.add_edge('в', 'г')

    params = {'label_color': '#ff0400',
              'label_size': '20',
              'node_color': {
                  'a': '#ff0000',
                  'b': '#00ff00',
                  'd': '#362f8a',
                  'c': '#f68e1e',
                  'а': '#0d00ff',
                  'б': '#f68e1e',
                  'в': '#00ff00',
                  'г': '#362f8a',
              },
              'node_size': {
                  'a': '5',
                  'b': '10',
                  'c': '20',
                  'd': '12',
                  'а': '14',
                  'б': '7',
                  'в': '3',
                  'г': '2'
              }
              }

    pp.visualisation.export_html(n, filename='myNetwork.html', **params)

    # Создаю свою
    g = Graph(n.adjacency_matrix().shape[0], connected_for_each_node(n))

    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)
