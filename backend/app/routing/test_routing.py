from app.routing.graph_builder import build_graph, find_nearest_exit
from app.db.database import SessionLocal
from app.db.models import Node, Edge

def get_path_from(room_name):
    db = SessionLocal()
    room = db.query(Node).filter(Node.name == room_name).first()
    db.close()

    G = build_graph()
    path, length = find_nearest_exit(G, room.id)

    db = SessionLocal()
    path_names = [db.get(Node, nid).name for nid in path]
    db.close()

    return path_names, length

# Reset
db = SessionLocal()
db.query(Edge).update({Edge.is_blocked: False})
db.commit()
db.close()

# Test rooms from all 3 floors
test_rooms = ["Class 15", "Computer Lab", "Class 12", "Terrace Access Door", "Class 2"]
for room in test_rooms:
    path, dist = get_path_from(room)
    print(f"{room}: {path} (distance: {dist})")