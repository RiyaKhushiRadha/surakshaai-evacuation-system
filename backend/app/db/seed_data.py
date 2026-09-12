from app.db.database import SessionLocal, init_db
from app.db.models import Node, Edge

def seed_ground_floor():
    db = SessionLocal()

    # ---- NODES ----
    nodes_data = [
        {"name": "Stair A", "node_type": "staircase", "floor": 0, "is_exit": True},
        {"name": "Toilets Boys", "node_type": "room", "floor": 0},
        {"name": "Class 1", "node_type": "room", "floor": 0},
        {"name": "Class 2", "node_type": "room", "floor": 0},
        {"name": "Class 3", "node_type": "room", "floor": 0},
        {"name": "Class 4", "node_type": "room", "floor": 0},
        {"name": "Toilets Girls", "node_type": "room", "floor": 0},
        {"name": "Stair B", "node_type": "staircase", "floor": 0, "is_exit": True},
        {"name": "Cor 1", "node_type": "corridor", "floor": 0},
        {"name": "Cor 2", "node_type": "corridor", "floor": 0},
        {"name": "Cor 3", "node_type": "corridor", "floor": 0},
        {"name": "Cor 4", "node_type": "corridor", "floor": 0},
        {"name": "Cor 5", "node_type": "corridor", "floor": 0},
        {"name": "Cor 6", "node_type": "corridor", "floor": 0},
    ]

    node_objs = {}
    for n in nodes_data:
        obj = Node(**n)
        db.add(obj)
        db.flush()  # id turant assign karne ke liye, commit se pehle
        node_objs[n["name"]] = obj

    # ---- EDGES ----
    # Har room apne corridor segment se, aur corridor segments ek doosre se
    edges_data = [
        ("Stair A", "Cor 1"), ("Toilets Boys", "Cor 1"),
        ("Cor 1", "Cor 2"), ("Class 1", "Cor 2"),
        ("Cor 2", "Cor 3"), ("Class 2", "Cor 3"),
        ("Cor 3", "Cor 4"), ("Class 3", "Cor 4"),
        ("Cor 4", "Cor 5"), ("Class 4", "Cor 5"),
        ("Cor 5", "Cor 6"), ("Toilets Girls", "Cor 6"), ("Stair B", "Cor 6"),
    ]

    for source_name, target_name in edges_data:
        edge = Edge(
            source_id=node_objs[source_name].id,
            target_id=node_objs[target_name].id,
            weight=1.0
        )
        db.add(edge)

    db.commit()
    db.close()
    print("Ground floor seeded successfully!")

if __name__ == "__main__":
    init_db()
    seed_ground_floor()