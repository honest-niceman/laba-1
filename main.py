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

n = pp.Network()
n.add_edge(('a', 'b'), ('a', 'c'))
print(n)

pp.visualisation.export_html(n, filename='3.html', **params)

# %% My task

n = pp.Network(directed=False)
n.add_edge('a', 'b')
n.add_edge('b', 'd')
n.add_edge('a', 'e')
n.add_edge('a', 'd')
n.add_edge('d', 'e')
n.add_edge('d', 'f')
n.add_edge('e', 'f')

n.add_edge('б', 'д')
n.add_edge('д', 'ж')
n.add_edge('ж', 'ц')

pp.visualisation.export_html(n, filename='myNetwork.html', **params)


def dfs(A, temp, v, visited):
    print("Recursion started with params:\n" + str(A) + "\n" + str(temp) + "\n" + str(v) + "\n" + str(visited))
    visited[int(v)] = True
    temp.append(int(v))
    print("Now temp is " + str(temp))

    for i in A[int(v)]:
        print(str(i) + " element of row " + str(v))
        if not visited[int(i)]:
            print(str(i) + " element of row " + str(v) + "is not visited")
            print("Deep into recursion from recursion")
            temp = dfs(A, temp, i, visited)
    return temp


def connected_components(network):
    visited = []
    conn_component = []
    A = network.adjacency_matrix().toarray()

    print("Matrix:\n" + str(A))

    for i in range(network.nodes.__len__()):
        visited.append(False)

    print("Visited list of nodes:\n" + str(visited))

    for v in range(network.nodes.__len__()):
        print("Node №" + str(v))
        if not visited[int(v)]:
            print("Node №" + str(v) + " is not visited")
            temp = []
            print("Deep into recursion")
            conn_component.append(dfs(A, temp, v, visited))
    return conn_component


print(connected_components(n))
