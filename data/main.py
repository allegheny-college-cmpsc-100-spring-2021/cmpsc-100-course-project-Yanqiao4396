from Battle import Battle
from monsters import monsters
monster_a = monsters()
monster_b = monsters()

PVP = Battle(monster_a, monster_b)
PVP.fight()