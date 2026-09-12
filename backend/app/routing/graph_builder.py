import networkx as nx
from app.db.database import SessionLocal
from app.db.models import Node, Edge

def build_graph():
    db = SessionLocal()
    G = nx.Graph()  # undirected graph — corridor dono taraf se chala jaa sakta hai

    nodes = db.query(Node).all()
    for node in nodes:
        G.add_node(node.id, name=node.name, node_type=node.node_type, is_exit=node.is_exit)

    edges = db.query(Edge).all()
    for edge in edges:
        if not edge.is_blocked:  # blocked edges graph me hi nahi daalenge
            G.add_edge(edge.source_id, edge.target_id, weight=edge.weight)

    db.close()
    return G

def find_nearest_exit(G, start_node_id):
    exit_nodes = [n for n, data in G.nodes(data=True) if data.get("is_exit")]

    best_path = None
    best_length = float("inf")

    for exit_id in exit_nodes:
        try:
            path = nx.shortest_path(G, source=start_node_id, target=exit_id, weight="weight")
            length = nx.shortest_path_length(G, source=start_node_id, target=exit_id, weight="weight")
            if length < best_length:
                best_length = length
                best_path = path
        except nx.NetworkXNoPath:
            continue  # is exit tak koi raasta nahi mila (blocked hoga shayad)

    return best_path, best_length