import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Carregar o dataset (exemplo usando um arquivo CSV)
df = pd.read_csv('credit_card_fraud_detection.csv')  # Substitua pelo caminho do seu arquivo

paises = nx.DiGraph()
paises.add_nodes_from(df['Country'].unique())

# Definir manualmente as posições dos nós
num_nodes = len(paises.nodes())
pos = {node: (0, i) for i, node in enumerate(paises.nodes())}  # Posiciona os nós em uma coluna vertical

# Ajustar as posições para centralizar na tela
# O eixo Y é invertido no matplotlib, então começamos de cima para baixo
pos = {node: (0, num_nodes - i - 1) for i, node in enumerate(paises.nodes())}

# Desenhar o grafo
nx.draw(paises, pos, with_labels=True, node_size=1000, node_color='blue', font_size=12, font_weight='bold')

# Mostrar o gráfico
plt.show()