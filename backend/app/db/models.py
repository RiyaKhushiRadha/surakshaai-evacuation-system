from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)          # e.g. "Class 1", "Cor 1", "Stair A"
    node_type = Column(String, nullable=False)      # "room", "corridor", "staircase", "entrance"
    floor = Column(Integer, nullable=False)          # 0 = ground, 1 = first, 2 = second
    is_exit = Column(Boolean, default=False)         # True for staircases/entrances
    x_coord = Column(Float, nullable=True)            # for drawing on frontend map
    y_coord = Column(Float, nullable=True)

class Edge(Base):
    __tablename__ = "edges"

    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, ForeignKey("nodes.id"), nullable=False)
    target_id = Column(Integer, ForeignKey("nodes.id"), nullable=False)
    weight = Column(Float, default=1.0)               # distance/time cost
    is_blocked = Column(Boolean, default=False)        # True agar fire/smoke detect ho us path pe