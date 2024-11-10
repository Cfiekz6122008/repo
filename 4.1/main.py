# Позиционирование камеры на танке игрока

from tank import Tank
from tkinter import*
# 1 подключение библиотеки world
import world
import tank_collection


KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN = 37, 39, 38, 40

KEY_W = 87
KEY_S = 83
KEY_A = 65
KEY_D = 68


FPS = 60
def update():
    # 1 будем переставлять камеру в новые координаты совпадфющие с координатами танка игрока
    # world.set_camera_xy(player.get_x(), player.get_y())
    player = tank_collection.get_player()
    # 2 отцентруем камеру
    world.set_camera_xy(player.get_x()-world.SCREEN_WIDTH//2 + player.get_size()//2,
                        player.get_y()-world.SCREEN_HEIGHT//2 + player.get_size()//2)
    tank_collection.update()
    w.after(1000//FPS, update)


def key_press(event):
    player = tank_collection.get_player()
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
    elif event.keycode == 32:
        tank_collection.spawn_enemy()



w = Tk()
w.title('Танки на минималках 2.0')
canv = Canvas(w, width = world.WIDTH, height = world.HEIGHT, bg = 'alice blue')
canv.pack()



tank_collection.initialize(canv)

w.bind('<KeyPress>', key_press)



update()
w.mainloop()