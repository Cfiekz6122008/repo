from hitbox import Hitbox
# 2 задача размесить танки на канвасе,
# добавить переменные класса (количество созданных танков, размер танка)
class Tank:
    count = 0 # общее количество изготовленных танков
    SIZE = 100  # размер танка
    def __init__(self, canvas, x, y,model = 'Т-14 Армата', ammo = 100, speed = 10):
        self.__hitbox = Hitbox(x, y, Tank.SIZE, Tank.SIZE)
        self.canvas = canvas
        Tank.count += 1
        self.model = model
        self.hp = 100
        self.xp = 0
        self.ammo = ammo
        self.fuel = 100
        self.speed = speed
        self.x = x
        self.y = y
        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

        self.create()  # вызов функции отрисовки танка внутри конструктора

    # Методы класса

    def fire(self): # метод для стрельбы и подсчета боеприпасов
        if self.ammo > 0:
            self.ammo -= 1
            print('стреляю')

    def forvard(self):  # по оси y вверх
        if self.fuel > 0:
            self.y += -self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.repaint()  # перерисовка танка
            print(self)

    def backward(self): # по оси y вниз
        if self.fuel > 0:
            self.y += self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.repaint()  # перерисовка танка
            print(self)

    def left(self):  # по оси x влево
        if self.fuel > 0:
            self.x += -self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.repaint()  # перерисовка танка
            print(self)

    def right(self): # по оси x вправо
        if self.fuel > 0:
            self.x += self.speed
            self.__update_hitbox()
            self.fuel -= 1
            self.repaint()  # перерисовка танка
            print(self)

    def create(self): # создание танка на холсте в виде квадратной поверхности через идентификатор
        self.id = self.canvas.create_rectangle(self.x, self.y, self.x + Tank.SIZE,
                                               self.y + Tank.SIZE, fill='red')

    def repaint(self):
        self.canvas.moveto(self.id, x = self.x, y = self.y)

    def __update_hitbox(self):
        self.__hitbox.moveto(self.x, self.y)

    def intersects(self, other_tank):
        return self.__hitbox.intersects(other_tank.__hitbox)

    def __str__(self):
        return f'координаты: x = {self.x}, y = {self.y}, модель: {self.model}, здоровье: {self.hp}, опыт: {self.xp}, боеприпасы: {self.ammo}'

