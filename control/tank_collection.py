from tank import Tank
from random import randint
import world

_tank = []
_canvas = None


def initialize(canv):
    global _canvas
    _canvas = canv

    player = Tank(canvas=canv, x=100, y=50, ammo=100, speed=1, bot=False)
    enemy = Tank(canvas=canv, x=300, y=300, ammo=100, speed=1, bot=True)
    neutral = Tank(canvas=canv, x=500, y=300, ammo=100, speed=1, bot=False)
    neutral.stop()
    enemy.set_target(player)

    _tank.append(player)
    _tank.append(enemy)
    _tank.append(neutral)
    print(_tank)

def get_player():
    return _tank[0]

def update():
    for tank in _tank:
        tank.update()
        check_collision(tank)

def check_collision(tank):
    for other_tank in _tank:
        if tank == other_tank:
            continue
        if tank.intersects(other_tank):
            return True
    return False
def spawn_enemy():
    while True:
        pos_x = randint(200, 800)
        pos_y = randint(200, 800)
        t = Tank(_canvas, x=pos_x, y=pos_y, speed=1)
        if not check_collision(t):
            t.set_target(get_player())
            _tank.append(t)
            return True


