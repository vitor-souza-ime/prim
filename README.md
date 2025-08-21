# Algoritmo de Prim aplicado a Sistemas Elétricos de Potência ⚡

Este repositório demonstra, de maneira didática, a aplicação do **Algoritmo de Prim** para otimização de redes de transmissão em **sistemas elétricos de potência**.  
O objetivo é reduzir o custo total de interligação das subestações escolhendo um subconjunto de linhas de transmissão que mantenha a rede **conectada com menor custo possível**.

## 📂 Estrutura do Projeto

- `main.py` → Código principal que implementa:
  - Construção do grafo representando as subestações e linhas de transmissão (com custos/pesos).
  - Aplicação do algoritmo de **Prim** via NetworkX.
  - Comparação entre:
    - **Rede original (sem otimização)** → todos os enlaces possíveis.
    - **Árvore Geradora Mínima (MST)** → rede otimizada.
  - Geração de gráficos ilustrando a diferença.

## 🚀 Execução

Clone este repositório e execute o código em Python (recomenda-se ambiente com `venv` ou Google Colab):

```bash
git clone https://github.com/vitor-souza-ime/prim.git
cd prim
python main.py
````

### 📦 Dependências

Instale as bibliotecas necessárias:

```bash
pip install networkx matplotlib
```

## 📊 Resultados esperados

O script gera dois gráficos:

1. **Rede Original** → mostra todas as conexões possíveis entre as 10 subestações, com seus respectivos custos (pesos nas arestas).
2. **Rede Otimizada (MST - Prim)** → mostra apenas as conexões essenciais para manter a rede conectada com **custo mínimo**.

Além disso, o console exibirá:

```
Custo total da rede original (sem otimização): XXXX
Custo total da MST (Prim): YYYY
Economia absoluta: ZZZZ
Economia percentual: W.WW%
```

## 📖 Contexto

Em sistemas elétricos de potência, uma rede de subestações pode ser representada como um **grafo ponderado**:

* **Nós (vértices)** → Subestações.
* **Arestas (com pesos)** → Linhas de transmissão, com custo associado (financeiro, impedância ou perda).

O **Algoritmo de Prim** encontra a **Árvore Geradora Mínima (MST)**, garantindo conectividade com menor custo possível — uma técnica útil para **planejamento de redes elétricas**.

## ✨ Autor

* [Vitor Amadeu Souza](https://github.com/vitor-souza-ime)

---

📢 *Este repositório é um exemplo educacional para aplicação de algoritmos clássicos em problemas de Engenharia Elétrica.*

