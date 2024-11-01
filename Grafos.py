import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = {}

    def agregar_arista(self, vertice1, vertice2, peso=None, direccionado=False):
        self.agregar_vertice(vertice1)
        self.agregar_vertice(vertice2)
        self.grafo[vertice1][vertice2] = peso
        if not direccionado:
            self.grafo[vertice2][vertice1] = peso


estados = ['CDMX', 'EdoMex', 'Puebla', 'Veracruz', 'Oaxaca', 'Guerrero', 'Morelos']
conexiones = [
    ('CDMX', 'EdoMex', 50),
    ('CDMX', 'Puebla', 120),
    ('EdoMex', 'Morelos', 70),
    ('Puebla', 'Veracruz', 200),
    ('Veracruz', 'Oaxaca', 250),
    ('Oaxaca', 'Guerrero', 180),
    ('Guerrero', 'Morelos', 140)
]


grafo = Grafo()
for estado in estados:
    grafo.agregar_vertice(estado)
for u, v, peso in conexiones:
    grafo.agregar_arista(u, v, peso)

from itertools import permutations

def recorrer_sin_repetir(grafo):
    estados = list(grafo.grafo.keys())
    min_cost = float('inf')
    min_path = []

    for perm in permutations(estados):
        cost = 0
        valid = True
        for i in range(len(perm) - 1):
            if perm[i + 1] in grafo.grafo[perm[i]]:
                cost += grafo.grafo[perm[i]][perm[i + 1]]
            else:
                valid = False
                break
        if valid and cost < min_cost:
            min_cost = cost
            min_path = perm

    return min_path, min_cost

def recorrer_con_repetir(grafo):
    estados = list(grafo.grafo.keys())
    max_cost = 0
    max_path = []

    for perm in permutations(estados):
        cost = 0
        for i in range(len(perm) - 1):
            if perm[i + 1] in grafo.grafo[perm[i]]:
                cost += grafo.grafo[perm[i]][perm[i + 1]]
        if cost > max_cost:
            max_cost = cost
            max_path = perm

    return max_path, max_cost

def mostrar_relaciones(grafo):
    for vertice, adyacentes in grafo.grafo.items():
        for adyacente, peso in adyacentes.items():
            print(f"{vertice} -> {adyacente}: {peso}")



path, cost = recorrer_sin_repetir(grafo)
print(f"Recorrido sin repetir: {path}, Costo total: {cost}")

path, cost = recorrer_con_repetir(grafo)
print(f"Recorrido con repetir: {path}, Costo total: {cost}")

mostrar_relaciones(grafo)



def dibujar_grafo(grafo):
    G = nx.Graph()
    for vertice, adyacentes in grafo.grafo.items():
        for adyacente, peso in adyacentes.items():
            G.add_edge(vertice, adyacente, weight=peso)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Grafo de Estados de la República Mexicana")
    plt.show()


dibujar_grafo(grafo)
