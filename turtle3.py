import turtle


turtle.shape('turtle')
turtle.title("Смотри, как могу!!!")

# установка параметров
radius = 70  # радиус узора
curse = 0   # начальное направление черепахи
n = 3  # кол-во веток


# цикл рисования
for i in range(n):
    turtle.seth(curse)
    turtle.circle(radius)
    turtle.circle(-radius)
    curse += 360/n
