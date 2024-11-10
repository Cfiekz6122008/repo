# Позиционирование камеры на танке игрока

from tank import Tank
from tkinter import*
# 1 подключение библиотеки world
import world


KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68


FPS = 60
def update():
    # 1 будем переставлять камеру в новые координаты совпадфющие с координатами танка игрока
    # world.set_camera_xy(player.get_x(), player.get_y())

    # 2 отцентруем камеру
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2 + player.get_size()//2,
                        player.get_y()-world.SCREEN_HEIGHT//2 + player.get_size()//2)
    player.update()
    enemy.update()
    neutral.update()
    check_collision()
    w.after(1000//FPS, update)

def check_collision():
    player.inersects(enemy)
    enemy.inersects(player)


def key_press(event):
    if event.keycode == KEY_W:
        player.forvard()
    elif event.keycode == KEY_S:
        player.backward()
    elif event.keycode == KEY_A:
        player.left()
    elif event.keycode == KEY_D:
        player.right()
    elif event.keycode == KEY_UP:
        world.move_camera(0, -5)
    elif event.keycode == KEY_DOWN:
        world.move_camera(0, 5)
    elif event.keycode == KEY_LEFT:
        world.move_camera(-5, 0)
    elif event.keycode == KEY_RIGHT:
        world.move_camera(5, 0)



w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width = world.WIDTH, height = world.HEIGHT, bg = 'alice blue')
canv.pack()

player = Tank(canvas = canv, x = 100, y = 50, ammo = 100, speed=1, bot = False)
enemy = Tank(canvas = canv, x = 300, y = 300, ammo = 100, speed=1, bot = True)
neutral = Tank(canvas = canv, x = 300, y = 300, ammo = 100, speed=1, bot = False)
neutral.stop()

enemy.set_target(player)


w.bind('<KeyPress>', key_press)



update()
w.mainloop()