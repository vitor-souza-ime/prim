import networkx as nx
import matplotlib.pyplot as plt

# ------------------------
# Grafo do sistema elétrico (10 subestações)
# Pesos = custo (ou impedância equivalente) das linhas
# ------------------------
edges = [
    (0, 1, 4), (0, 7, 8),
    (1, 2, 8), (1, 7, 11),
    (2, 3, 7), (2, 8, 2), (2, 5, 4),
    (3, 4, 9), (3, 5, 14),
    (4, 5, 10),
    (5, 6, 2),
    (6, 7, 1), (6, 8, 6),
    (7, 8, 7), (7, 9, 2),
    (8, 9, 5)
]

G = nx.Graph()
G.add_weighted_edges_from(edges)

# ------------------------
# Algoritmo de Prim -> Árvore Geradora Mínima (MST)
# ------------------------
mst = nx.minimum_spanning_tree(G, algorithm="prim")

# ------------------------
# Custos
# ------------------------
# Custo "sem otimização": soma de TODAS as linhas existentes (toda a malha original)
total_sem_otimizacao = sum(w for *_, w in G.edges.data("weight"))

# Custo "com otimização": soma das linhas selecionadas pela MST (Prim)
total_mst = sum(w for *_, w in mst.edges.data("weight"))

economia_abs = total_sem_otimizacao - total_mst
economia_pct = 100.0 * economia_abs / total_sem_otimizacao

print(f"Custo total da rede original (sem otimização): {total_sem_otimizacao}")
print(f"Custo total da MST (Prim): {total_mst}")
print(f"Economia absoluta: {economia_abs}")
print(f"Economia percentual: {economia_pct:.2f}%")

# ------------------------
# Gráficos
# ------------------------
pos = nx.spring_layout(G, seed=42)

plt.figure(figsize=(14, 7))

# Rede original
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=10)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
plt.title("Rede Elétrica Original (10 Subestações)")

# MST
plt.subplot(1, 2, 2)
nx.draw(mst, pos, with_labels=True, node_size=800, node_color="lightgreen", font_size=10)
labels_mst = nx.get_edge_attributes(mst, "weight")
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels_mst, font_size=8)
