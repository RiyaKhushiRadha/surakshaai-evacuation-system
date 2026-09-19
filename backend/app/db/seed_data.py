from app.db.database import SessionLocal, init_db
from app.db.models import Node, Edge

def seed_ground_floor():
    db = SessionLocal()

    # ---- NODES ----
    nodes_data = [
        # Top row
        {"name": "Stair A", "node_type": "staircase", "floor": 0, "is_exit": True},
        {"name": "Toilets Boys", "node_type": "room", "floor": 0},
        {"name": "Class 1", "node_type": "room", "floor": 0},
        {"name": "Class 2", "node_type": "room", "floor": 0},
        {"name": "Class 3", "node_type": "room", "floor": 0},
        {"name": "Class 4", "node_type": "room", "floor": 0},
        {"name": "Toilets Girls", "node_type": "room", "floor": 0},
        {"name": "Stair B", "node_type": "staircase", "floor": 0, "is_exit": True},
        # Corridor segments
        {"name": "Cor 1", "node_type": "corridor", "floor": 0},
        {"name": "Cor 2", "node_type": "corridor", "floor": 0},
        {"name": "Cor 3", "node_type": "corridor", "floor": 0},
        {"name": "Cor 4", "node_type": "corridor", "floor": 0},
        {"name": "Cor 5", "node_type": "corridor", "floor": 0},
        {"name": "Cor 6", "node_type": "corridor", "floor": 0},
        # Bottom row (left to right)
        {"name": "Library", "node_type": "room", "floor": 0},
        {"name": "Activity Room", "node_type": "room", "floor": 0},
        {"name": "Principal Office", "node_type": "room", "floor": 0},
        {"name": "Admin Office", "node_type": "room", "floor": 0},
        {"name": "Reception", "node_type": "room", "floor": 0},
        {"name": "Waiting Area", "node_type": "room", "floor": 0},
        {"name": "Staff Room", "node_type": "room", "floor": 0},
        {"name": "Teacher Cabin", "node_type": "room", "floor": 0},
        {"name": "Class 5", "node_type": "room", "floor": 0},
        {"name": "Class 6", "node_type": "room", "floor": 0},
        {"name": "Store", "node_type": "room", "floor": 0},
        # Entrances (ye bhi exits hai)
        {"name": "Main Entrance", "node_type": "entrance", "floor": 0, "is_exit": True},
        {"name": "Second Entrance", "node_type": "entrance", "floor": 0, "is_exit": True},
    ]

    node_objs = {}
    for n in nodes_data:
        obj = Node(**n)
        db.add(obj)
        db.flush()
        node_objs[n["name"]] = obj

    # ---- EDGES ----
    edges_data = [
        # Top row to corridor
        ("Stair A", "Cor 1"), ("Toilets Boys", "Cor 1"),
        ("Cor 1", "Cor 2"), ("Class 1", "Cor 2"),
        ("Cor 2", "Cor 3"), ("Class 2", "Cor 3"),
        ("Cor 3", "Cor 4"), ("Class 3", "Cor 4"),
        ("Cor 4", "Cor 5"), ("Class 4", "Cor 5"),
        ("Cor 5", "Cor 6"), ("Toilets Girls", "Cor 6"), ("Stair B", "Cor 6"),
        # Bottom row to corridor (nearest segment ke hisab se)
        ("Library", "Cor 1"), ("Activity Room", "Cor 1"),
        ("Principal Office", "Cor 2"), ("Admin Office", "Cor 2"),
        ("Reception", "Cor 3"), ("Waiting Area", "Reception"), ("Main Entrance", "Waiting Area"),
        ("Staff Room", "Cor 4"), ("Teacher Cabin", "Cor 4"),
        ("Class 5", "Cor 5"), ("Class 6", "Cor 5"),
        ("Store", "Cor 6"), ("Second Entrance", "Cor 6"),
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