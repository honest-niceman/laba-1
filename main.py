import pathpy as pp


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
