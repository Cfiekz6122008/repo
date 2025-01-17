from tkinter import *
import random
import json
import os

game_width = 3440
game_height = 1440

window = Tk()
window.title('Мухобойка')
window.resizable(width=False, height=False)

canvas = Canvas(window, width=game_width, height=game_height)
canvas.pack()

background_image = PhotoImage(file='img/forest.png')
canvas.create_image(0, 0, image=background_image, anchor=NW)

npc_image = PhotoImage(file='img/fly.png')
npc_id = canvas.create_image(0, 0, image=npc_image, anchor=NW)

swatter_image = PhotoImage(file='img/pngwing.com.png')
swatter_cursor = canvas.create_image(0, 0, image=swatter_image, anchor=NW)
window.config(cursor="none")

npc_width = 120
npc_height = 95
score = 10
text_id = canvas.create_text(game_width - 10, 10, fill="white", font="Times 20 bold", text=f'Очки: {score}', anchor=NE)
gameover = False
paused = False

def mouse_move(e):
    canvas.coords(swatter_cursor, e.x, e.y)

def mouse_click(e):
    global gameover, paused
    if gameover or paused:
        return
    if collision_detection(e.x, e.y):
        hit()
    else:
        missclick()

def collision_detection(x, y):
    position = canvas.coords(npc_id)
    left = position[0]
    top = position[1]
    right = left + npc_width
    bottom = top + npc_height
    return left <= x <= right and top <= y <= bottom

def hit():
    global score
    score += 1
    update_points()
    move_npc()

def missclick():
    global score
    score -= 1
    if score < 0:
        game_over()
    else:
        update_points()

def update_points():
    canvas.itemconfigure(text_id, text=f'Очки: {score}')

def game_over():
    global gameover
    canvas.itemconfigure(text_id, text='Игра окончена!')
    gameover = True

def spawn():
    x = random.randint(0, game_width - npc_width)
    y = random.randint(0, game_height - npc_height)
    canvas.coords(npc_id, x, y)

def move_npc():
    spawn()

def game_update():
    if not gameover and not paused:
        spawn()
    canvas.after(1000, game_update)

def show_menu():
    global paused
    paused = True
    menu_window = Toplevel(window)
    menu_window.title("Меню")
    menu_window.geometry("600x400")
    menu_window.configure(bg="white")

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (window_width // 2) - (600 // 2)
    y = (window_height // 2) - (400 // 2)
    menu_window.geometry(f"600x400+{x}+{y}")

    title_label = Label(menu_window, text="Меню", font=("Arial", 24), bg="white")
    title_label.pack(pady=20)

    button_style = {
        'width': 25,
        'font': ("Arial", 16),
        'bg': 'lightblue',
        'activebackground': 'lightgray',
        'bd': 2,
        'relief': 'solid'
    }

    def start_new_game():
        reset_game()
        menu_window.destroy()

    def save_game():
        game_data = {
            "score": score
        }
        with open('saved_game.json', 'w') as f:
            json.dump(game_data, f)
        menu_window.destroy()

    def load_game():
        global score, gameover, paused
        if os.path.exists('saved_game.json'):
            with open('saved_game.json', 'r') as f:
                game_data = json.load(f)
                score = game_data["score"]
                gameover = False
                paused = False
                update_points()
                menu_window.destroy()
        else:
            print("Файл сохранения не найден.")

    def exit_game():
        window.destroy()

    Button(menu_window, text="Новая игра", command=start_new_game, **button_style).pack(pady=10)
    Button(menu_window, text="Сохранить игру", command=save_game, **button_style).pack(pady=10)
    Button(menu_window, text="Загрузить игру", command=load_game, **button_style).pack(pady=10)
    Button(menu_window, text="Выход", command=exit_game, **button_style).pack(pady=10)

def reset_game():
    global score, gameover, paused
    score = 10
    gameover = False
    paused = False
    update_points()
    spawn()

def on_escape(event):
    show_menu()

window.bind("<Motion>", mouse_move)
window.bind("<Button-1>", mouse_click)
window.bind("<Escape>", on_escape)

game_update()
window.mainloop()







