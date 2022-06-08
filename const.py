from orientation import Orientation


windows_size = (800,800) # width X height
framerate = 120
GAP = 50
WIDTH = 5
LINES = (0,0,0)
rows = windows_size[0]/GAP+WIDTH
columns = windows_size[1]/GAP+WIDTH
SQUARE_SIZE = windows_size[0]/16
GRID_SIZE = 48
scale = 0.12
START_POS = (0, 0)
START_ORIENTATION = Orientation.UP
MONSTER_NAMES = ['Wolf', 'Bandit', 'Griffin', 'Leshy']
MONSTER_COUNT = 10

MAPS = [
    (0,0),(0,1),(0,2),
    (1,0),(1,1),(1,2),
    (2,0),(2,1),(2,2)
]

WATER = [
    # Map 2,1
    (0,19),
    (1,19),(1,20),
    (2,17),(2,21),
    (3,21),(3,22),(3,28),(3,29),
    (4,22),(4,28),(4,29),(4,30),
    (5,16),(5,23),(5,25),(5,26),
    (6,19),(6,20),(6,26),(6,27),
    (7,27),
    (8,20),(8,21),(8,22),(8,23),(8,27),(8,28),(8,30),(8,31),
    (9,21),(9,22),(9,23),(9,28),(9,30),(9,31),
    (10,22),(10,23),(10,27),(10,28),
    (11,16),(11,17),(11,18),(11,25),(11,27),
    (13,19),(13,20),(13,21),(13,26),(13,27),
    (14,17),(14,23),(14,24),(14,26),(14,27),
    (15,23),(15,24),

    # Map 2,2
    (16,22),(16,23),
    (17,29),(17,30),
    (18,19),(18,20),(18,22),(18,23),(18,25),(18,26),(18,27),(18,29),(18,30),(18,31),
    (19,18),(19,19),(19,27),
    (20,17),(20,18),(20,27),(20,28),
    (21,17),
    (22,17),(22,20),(22,28),(22,29),
    (23,17),(23,29),
    (24,29),
    (25,22),(25,23),(25,24),(25,25),(25,28),(25,29),
    (26,17),(26,18),(26,23),(26,24),(26,25),(26,28),
    (27,17),(27,18),(27,21),(27,24),(27,25),
    (28,18),(28,19),(28,27),(28,28),
    (29,18),(29,19),(29,20),(29,27),(29,28),
    (30,19),(30,20),(30,22),(30,23),(30,24),(30,25),(30,26),

    # Map 2,3
    (35,22),(35,24),
    (36,18),(36,19),(36,20),(36,21),(36,22),(36,24),(36,25),(36,26),
    (37,18),(37,19),(37,26),(37,27),
    (38,21),(38,27),
    (39,18),(39,27),
    (40,18),(40,22),(40,23),(40,24),(40,27),
    (41,19),(41,22),(41,23),(41,24),(41,28),(41,29),
    (42,19),(42,23),(42,24),(42,29),
    (43,19),(43,24),(43,31),
    (44,19),(44,27),(44,31),
    (45,21),(45,27),(45,28),
    (46,18),(46,21),(46,27),(46,28),(46,30),
    (47,21)
]

ROCKS = [
    # Map 1,1
    (0,3),(5,5),(6,13),

    # Map 1,2
    (22,14),(23,7),(23,11),

    # Map 1,3
    (33,11),(37,10),(38,2),(38,7),

    # Map 3,1
    (1,46),(3,46),(13,33),

    # Map 3,2
    (16,36),(17,42),(18,32),(19,46),(26,38),(30,33),

    # Map 3,3
    (32,35),(32,41),(35,46),(42,37),

]

COLLISIONS = [
    # Map 1,1
    (0,6),(0,7),(0,8),(0,9),(0,10),(0,11),
    (1,6),(1,7),(1,8),(1,9),(1,11),
    (2,1),(2,3),(2,4),(2,6),(2,7),(2,8),(2,11),(2,13),(2,14),
    (3,3),(3,4),(3,7),(3,10),(3,11),(3,13),(3,14),
    (4,10),(4,11),
    (5,0),(5,1),(5,2),(5,7),(5,15),
    (6,1),(6,2),(6,3),(6,8),
    (7,2),(7,3),(7,10),(7,11),(7,14),
    (8,6),(8,7),(8,11),(8,12),
    (9,6),(9,7),(9,8),(9,12),
    (10,2),(10,3),(10,6),(10,7),(10,8),(10,10),(10,12),
    (11,2),(11,3),(11,12),(11,15),
    (12,2),(12,3),(12,4),(12,5),(12,7),(12,11),(12,12),
    (13,10),(13,11),(13,14),
    (14,0),(14,3),(14,5),(14,6),(14,8),(14,15),
    (15,5),(15,11),(15,15),
    
    # Map 1,2
    (16,5),(16,11),(16,15),
    (17,0),(17,1),(17,2),(17,5),(17,6),
    (18,0),(18,1),(18,2),(18,3),(18,5),(18,6),(18,7),(18,10),(18,11),(18,12),(18,14),
    (19,0),(19,1),(19,2),(19,6),(19,7),(19,10),(19,11),(19,12),
    (20,0),(20,1),(20,4),(20,12),
    (21,12),(21,14),(21,15),
    (22,2),(22,3),(22,9),
    (23,2),(23,3),(23,14),
    (24,5),(24,13),
    (25,7),(25,8),
    (26,2),(26,3),(26,5),(26,7),(26,8),(26,10),(26,14),
    (27,2),(27,3),(27,4),
    (28,2),(28,3),(28,4),(28,7),(28,11),(28,12),
    (29,11),(29,12),
    (30,0),(30,1),(30,8),(30,9),(30,15),
    (31,0),(31,1),(31,4),(31,5),(31,15),

    # Map 1,3
    (32,0),(32,1),(32,4),(32,5),
    (33,4),(33,7),(33,8),(33,9),(33,14),(33,15),
    (34,4),(34,7),(34,8),(34,9),(34,13),(34,14),(34,15),
    (35,1),(35,2),(35,4),(35,5),(35,7),(35,8),(35,12),(35,13),(35,14),(35,15),
    (36,1),(36,2),(36,4),(36,5),(36,13),(36,14),(36,15),
    (37,8),(37,13),(37,14),(37,15),
    (38,12),(38,13),(38,14),
    (39,4),(39,5),(39,10),(39,12),(39,13),
    (40,3),(40,4),
    (41,0),(41,1),(41,3),(41,6),(41,7),(41,10),
    (42,0),(42,1),(42,3),(42,6),(42,7),(42,8),(42,12),(42,13),
    (43,3),(43,6),(43,7),(43,8),(43,12),(43,13),
    (44,3),(44,4),(44,10),(44,11),(44,12),(44,13),
    (45,1),(45,4),(45,5),
    (46,7),(46,9),(46,10),(46,14),
    (47,2),(47,4),(47,10),

    # Map 2,1
    
    (1,22),(1,24),(1,25),(1,27),(1,29),
    (2,24),(2,25),
    (4,17),(4,19),
    (6,30),
    (7,17),(7,28),
    (8,25),
    (9,18),
    (10,25),
    (11,20),(11,28),
    (12,23),(12,30),
    (13,22),
    (14,16),(14,29),(14,30),
    (15,16),(15,22),

    # Map 2,2
    (16,16),(16,24),
    (18,24),
    (20,20),(20,23),(20,25),
    (21,16),(21,18),(21,28),(21,29),
    (22,18),(22,22),(22,23),
    (23,22),(23,23),(23,26),
    (24,17),
    (25,20),
    (26,29),
    (28,17),
    (29,25),(29,26),(29,30),
    (30,16),
    (31,16),

    # Map 2,3
    # --- kolumna pusta ---
    (33,16),(33,18),(33,20),(33,21),(33,24),(33,27),
    (34,16),(34,29),(34,30),
    (35,16),(35,21),(35,25),(35,29),(35,30),
    (36,16),
    (37,16),(37,30),
    (38,24),
    (39,30),
    (42,17),(42,26),
    (43,17),(43,21),
    (45,23),(45,24),
    (46,23),(46,24),
    

    # Map 3,1
    (0,36),(0,37),(0,39),
    (1,33),(1,39),(1,42),(1,43),
    (2,33),(2,35),(2,36),(2,38),(2,39),(2,42),(2,43),(2,44),(2,47),
    (3,35),(3,36),(3,38),(3,42),(3,43),(3,44),
    (4,33),(4,38),
    (5,36),(5,41),(5,44),(5,47),
    (6,34),(6,42),(6,46),
    (7,35),(7,36),(7,37),(7,38),(7,40),(7,45),(7,46),
    (8,32),(8,34),(8,38),(8,44),
    (9,32),(9,39),(9,42),(9,44),(9,46),
    (10,34),(10,35),(10,37),(10,39),(10,44),(10,46),
    (11,34),(11,35),(11,39),(11,41),
    (12,37),(12,38),(12,45),
    (13,37),(13,40),(13,42),(13,46),
    (14,35),(14,40),(14,43),(14,46),
    (15,37),(15,46),

    # Map 3,2
    (16,37),(16,46),
    (17,33),(17,36),(17,39),(17,40),(17,45),(17,46),
    (18,39),(18,40),(18,43),(18,44),
    (19,35),(19,36),(19,43),
    (20,36),(20,37),
    (21,33),(21,38),(21,40),(21,42),(21,46),(21,47),
    (22,34),(22,35),(22,38),(22,42),(22,44),(22,46),(22,47),
    (23,34),(23,35),(23,38),(23,40),(23,42),(23,46),(23,47),
    (24,33),(24,37),(24,42),(24,43),
    (25,36),(25,40),(25,45),(25,47),
    (26,34),(26,36),(26,40),(26,47),
    (27,34),(27,36),(27,43),
    (28,39),(28,40),(28,43),(28,46),
    (29,39),(29,40),(29,43),(29,44),(29,46),
    (30,36),(30,44),
    (31,36),(31,41),(31,44),
    
    # Map 3,3
    (32,36),(32,44),
    (33,33),(33,35),(33,38),(33,39),(33,43),(33,44),(33,46),
    (34,38),(34,39),(34,42),
    (35,35),(35,41),(35,44),
    (36,33),(36,35),(36,36),(36,44),
    (37,37),(37,40),(37,42),(37,47),
    (38,34),(38,35),(38,37),(38,40),(38,44),(38,47),
    (39,34),(39,35),(39,37),(39,40),(39,43),(39,44),(39,45),(39,46),
    (40,36),(40,39),(40,40),(40,41),(40,42),
    (41,33),(41,35),(41,39),
    (42,35),(42,44),(42,46),
    (43,32),(43,35),(43,41),(43,46),
    (44,32),(44,39),(44,41),(44,46),(44,47),
    (45,41),(45,42),(45,44),(45,47),
    (46,35),(46,37),(46,38),(46,39),(46,42),(46,44),(46,46),(46,47),
    (47,33),(47,35),(47,37),(47,38),(47,39),(47,41),(47,42),(47,46),(47,47)
]