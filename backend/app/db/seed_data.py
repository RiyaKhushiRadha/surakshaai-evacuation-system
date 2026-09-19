from app.db.database import SessionLocal, init_db
from app.db.models import Node, Edge

def seed_all_floors():
    db = SessionLocal()

    # ---- NODES ----
    nodes_data = [
        # ===== GROUND FLOOR (floor 0) =====
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
        {"name": "Main Entrance", "node_type": "entrance", "floor": 0, "is_exit": True},
        {"name": "Second Entrance", "node_type": "entrance", "floor": 0, "is_exit": True},

        # ===== FIRST FLOOR (floor 1) =====
        {"name": "Stair A F1", "node_type": "staircase", "floor": 1},
        {"name": "Toilets Boys F1", "node_type": "room", "floor": 1},
        {"name": "Class 7", "node_type": "room", "floor": 1},
        {"name": "Class 8", "node_type": "room", "floor": 1},
        {"name": "Class 9", "node_type": "room", "floor": 1},
        {"name": "Class 10", "node_type": "room", "floor": 1},
        {"name": "Toilets Girls F1", "node_type": "room", "floor": 1},
        {"name": "Stair B F1", "node_type": "staircase", "floor": 1},
        {"name": "F1 Cor 1", "node_type": "corridor", "floor": 1},
        {"name": "F1 Cor 2", "node_type": "corridor", "floor": 1},
        {"name": "F1 Cor 3", "node_type": "corridor", "floor": 1},
        {"name": "F1 Cor 4", "node_type": "corridor", "floor": 1},
        {"name": "F1 Cor 5", "node_type": "corridor", "floor": 1},
        {"name": "F1 Cor 6", "node_type": "corridor", "floor": 1},
        {"name": "Computer Lab", "node_type": "room", "floor": 1},
        {"name": "Science Lab", "node_type": "room", "floor": 1},
        {"name": "Teacher Cabin F1", "node_type": "room", "floor": 1},
        {"name": "Meeting Room", "node_type": "room", "floor": 1},
        {"name": "Class 11", "node_type": "room", "floor": 1},
        {"name": "Class 12", "node_type": "room", "floor": 1},

        # ===== SECOND FLOOR (floor 2) =====
        {"name": "Stair A F2", "node_type": "staircase", "floor": 2},
        {"name": "Toilets Boys F2", "node_type": "room", "floor": 2},
        {"name": "Class 13", "node_type": "room", "floor": 2},
        {"name": "Class 14", "node_type": "room", "floor": 2},
        {"name": "Class 15", "node_type": "room", "floor": 2},
        {"name": "Class 16", "node_type": "room", "floor": 2},
        {"name": "Toilets Girls F2", "node_type": "room", "floor": 2},
        {"name": "Stair B F2", "node_type": "staircase", "floor": 2},
        {"name": "F2 Cor 1", "node_type": "corridor", "floor": 2},
        {"name": "F2 Cor 2", "node_type": "corridor", "floor": 2},
        {"name": "F2 Cor 3", "node_type": "corridor", "floor": 2},
        {"name": "F2 Cor 4", "node_type": "corridor", "floor": 2},
        {"name": "F2 Cor 5", "node_type": "corridor", "floor": 2},
        {"name": "F2 Cor 6", "node_type": "corridor", "floor": 2},
        {"name": "Seminar Room", "node_type": "room", "floor": 2},
        {"name": "Library Upper Level", "node_type": "room", "floor": 2},
        {"name": "Activity Room F2", "node_type": "room", "floor": 2},
        {"name": "Class 17", "node_type": "room", "floor": 2},
        {"name": "Class 18", "node_type": "room", "floor": 2},
        {"name": "Terrace Access Door", "node_type": "room", "floor": 2},
    ]

    node_objs = {}
    for n in nodes_data:
        obj = Node(**n)
        db.add(obj)
        db.flush()
        node_objs[n["name"]] = obj

    # ---- EDGES ----
    edges_data = [
        # ===== GROUND FLOOR =====
        ("Stair A", "Cor 1"), ("Toilets Boys", "Cor 1"),
        ("Cor 1", "Cor 2"), ("Class 1", "Cor 2"),
        ("Cor 2", "Cor 3"), ("Class 2", "Cor 3"),
        ("Cor 3", "Cor 4"), ("Class 3", "Cor 4"),
        ("Cor 4", "Cor 5"), ("Class 4", "Cor 5"),
        ("Cor 5", "Cor 6"), ("Toilets Girls", "Cor 6"), ("Stair B", "Cor 6"),
        ("Library", "Cor 1"), ("Activity Room", "Cor 1"),
        ("Principal Office", "Cor 2"), ("Admin Office", "Cor 2"),
        ("Reception", "Cor 3"), ("Waiting Area", "Reception"), ("Main Entrance", "Waiting Area"),
        ("Staff Room", "Cor 4"), ("Teacher Cabin", "Cor 4"),
        ("Class 5", "Cor 5"), ("Class 6", "Cor 5"),
        ("Store", "Cor 6"), ("Second Entrance", "Cor 6"),

        # ===== FIRST FLOOR =====
        ("Stair A F1", "F1 Cor 1"), ("Toilets Boys F1", "F1 Cor 1"),
        ("F1 Cor 1", "F1 Cor 2"), ("Class 7", "F1 Cor 2"),
        ("F1 Cor 2", "F1 Cor 3"), ("Class 8", "F1 Cor 3"),
        ("F1 Cor 3", "F1 Cor 4"), ("Class 9", "F1 Cor 4"),
        ("F1 Cor 4", "F1 Cor 5"), ("Class 10", "F1 Cor 5"),
        ("F1 Cor 5", "F1 Cor 6"), ("Toilets Girls F1", "F1 Cor 6"), ("Stair B F1", "F1 Cor 6"),
        ("Computer Lab", "F1 Cor 1"),
        ("Science Lab", "F1 Cor 2"),
        ("Teacher Cabin F1", "F1 Cor 3"),
        ("Meeting Room", "F1 Cor 4"),
        ("Class 11", "F1 Cor 5"),
        ("Class 12", "F1 Cor 6"),

        # ===== SECOND FLOOR =====
        ("Stair A F2", "F2 Cor 1"), ("Toilets Boys F2", "F2 Cor 1"),
        ("F2 Cor 1", "F2 Cor 2"), ("Class 13", "F2 Cor 2"),
        ("F2 Cor 2", "F2 Cor 3"), ("Class 14", "F2 Cor 3"),
        ("F2 Cor 3", "F2 Cor 4"), ("Class 15", "F2 Cor 4"),
        ("F2 Cor 4", "F2 Cor 5"), ("Class 16", "F2 Cor 5"),
        ("F2 Cor 5", "F2 Cor 6"), ("Toilets Girls F2", "F2 Cor 6"), ("Stair B F2", "F2 Cor 6"),
        ("Seminar Room", "F2 Cor 1"),
        ("Library Upper Level", "F2 Cor 2"),
        ("Activity Room F2", "F2 Cor 3"),
        ("Class 17", "F2 Cor 4"),
        ("Class 18", "F2 Cor 5"),
        ("Terrace Access Door", "F2 Cor 6"),
    ]

    for source_name, target_name in edges_data:
        edge = Edge(
            source_id=node_objs[source_name].id,
            target_id=node_objs[target_name].id,
            weight=1.0
        )
        db.add(edge)

    # ---- VERTICAL (STAIRCASE) CONNECTIONS BETWEEN FLOORS ----
    # Weight 2.0 rakha hai kyunki stairs use karna corridor walk karne se "costlier" hai
    vertical_edges = [
        ("Stair A", "Stair A F1"),
        ("Stair A F1", "Stair A F2"),
        ("Stair B", "Stair B F1"),
        ("Stair B F1", "Stair B F2"),
    ]
    for source_name, target_name in vertical_edges:
        edge = Edge(
            source_id=node_objs[source_name].id,
            target_id=node_objs[target_name].id,
            weight=2.0
        )
        db.add(edge)

    db.commit()
    db.close()
    print("All 3 floors seeded successfully!")

if __name__ == "__main__":
    init_db()
    seed_all_floors()