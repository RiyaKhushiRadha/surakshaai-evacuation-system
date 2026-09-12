from app.routing.graph_builder import build_graph, find_nearest_exit
from app.db.database import SessionLocal
from app.db.models import Node, Edge

# --- RESET: pichle test se koi bhi blocked edge wapas unblock karo ---
db = SessionLocal()
db.query(Edge).update({Edge.is_blocked: False})
db.commit()
db.close()

# --- TEST 1: Normal condition, Class 3 se nearest exit ---
db = SessionLocal()
class3 = db.query(Node).filter(Node.name == "Class 3").first()
db.close()

G = build_graph()
path, length = find_nearest_exit(G, class3.id)

db = SessionLocal()
path_names = [db.get(Node, nid).name for nid in path]
db.close()

print("Normal Path:", path_names)
print("Distance:", length)

# --- TEST 2: Cor 4 -> Cor 5 block karo (fire simulate) ---
db = SessionLocal()
cor4 = db.query(Node).filter(Node.name == "Cor 4").first()
cor5 = db.query(Node).filter(Node.name == "Cor 5").first()

blocked_edge = db.query(Edge).filter(
    Edge.source_id == cor4.id,
    Edge.target_id == cor5.id
).first()
blocked_edge.is_blocked = True
db.commit()
db.close()

G2 = build_graph()
path2, length2 = find_nearest_exit(G2, class3.id)

db = SessionLocal()
path_names2 = [db.get(Node, nid).name for nid in path2]
db.close()

print("\nAfter fire blocks Cor4-Cor5 section:")
print("New Path:", path_names2)
print("New Distance:", length2)

# --- RESET again, taaki agli baar test clean state se shuru ho ---
db = SessionLocal()
db.query(Edge).update({Edge.is_blocked: False})
db.commit()
db.close()