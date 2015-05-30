import turtle
import math


def pixel(a):  # процедура рисования пикселя
    turtle.forward(-a/2)
    turtle.left(90)
    turtle.forward(-a/2)
    turtle.right(90)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.back(-a/2)
    turtle.right(90)
    turtle.back(-a/2)


def Radius():
    #radius = math.sqrt(x**2 + y**2)
    turtle.sety(radius)
    turtle.setx(0)
    turtle.up()
    # дальше начинается сам процесс рисования
    #выбираем путь, который меньше всего отличается от радиуса
    while turtle.xcor() < radius and turtle.ycor() > 0:
        mh1 = int(abs((turtle.xcor() + step)**2 + turtle.ycor() ** 2 - radius**2))
        md2 = int(abs((turtle.xcor()+step)**2+(turtle.ycor()-step)**2 - radius**2))
        mv3 = int(abs(turtle.xcor()**2+(turtle.ycor()-step)**2 - radius**2))
        smallest = 0
       # print(mh1,md2,mv3)
        pixel(step)
        turtle.listen()
        if mh1 < md2 and mh1 < mv3:
            turtle.goto((turtle.xcor() + step), turtle.ycor())
          #  print(1)
        elif md2 < mh1 and md2 < mv3:
            turtle.goto((turtle.xcor()+step),turtle.ycor()-step)
           # print(2)
        else:
            turtle.goto((turtle.xcor(),turtle.ycor()-step))
    pixel(step)

    #4 цикла отвечают за разные дуги окружности
    
    while turtle.xcor() > 0 and turtle.ycor() > -radius:
        mh1 = int(abs((turtle.xcor() - step)**2 + turtle.ycor() ** 2 - radius**2))
        md2 = int(abs((turtle.xcor()- step)**2+(turtle.ycor()-step)**2 - radius**2))
        mv3 = int(abs(turtle.xcor()**2+(turtle.ycor()-step)**2 - radius**2))
        smallest = 0
       # print(mh1,md2,mv3)
        pixel(step)
        turtle.listen()
        if mh1 < md2 and mh1 < mv3:
            turtle.goto((turtle.xcor() - step), turtle.ycor())
          #  print(1)
        elif md2 < mh1 and md2 < mv3:
            turtle.goto((turtle.xcor()-step),turtle.ycor()-step)
           # print(2)
        else:
            turtle.goto((turtle.xcor(),turtle.ycor()-step))
    pixel(step)
            
    while turtle.xcor() >= -radius and turtle.ycor() <0:
        mh1 = int(abs((turtle.xcor() - step)**2 + turtle.ycor() ** 2 - radius**2))
        md2 = int(abs((turtle.xcor()-step)**2+(turtle.ycor()+step)**2 - radius**2))
        mv3 = int(abs(turtle.xcor()**2+(turtle.ycor()+step)**2 - radius**2))
        smallest = 0
       # print(mh1,md2,mv3)
        pixel(step)
        turtle.listen()
        if mh1 < md2 and mh1 < mv3:
            turtle.goto((turtle.xcor() - step), turtle.ycor())
          #  print(1)
        elif md2 < mh1 and md2 < mv3:
            turtle.goto((turtle.xcor()-step),turtle.ycor()+step)
           # print(2)
        else:
            turtle.goto((turtle.xcor(),turtle.ycor()+step))
    pixel(step)      
    while turtle.xcor() < 0:
        mh1 = int(abs((turtle.xcor() + step)**2 + turtle.ycor() ** 2 - radius**2))
        md2 = int(abs((turtle.xcor()+step)**2+(turtle.ycor()+step)**2 - radius**2))
        mv3 = int(abs(turtle.xcor()**2+(turtle.ycor()+step)**2 - radius**2))
        smallest = 0
       # print(mh1,md2,mv3)
        pixel(step)
        turtle.listen()
        if mh1 < md2 and mh1 < mv3:
            turtle.goto((turtle.xcor() + step), turtle.ycor())
          #  print(1)
        elif md2 < mh1 and md2 < mv3:
            turtle.goto((turtle.xcor()+step),turtle.ycor()+step)
           # print(2)
        else:
            turtle.goto((turtle.xcor(),turtle.ycor()+step))
    pixel(step)
    



turtle.listen()
turtle.bye()  # обновляем поле
#turtle.ht()  # скрываем черпаху
turtle.speed(0.5)  # рисуем сетку. увеличиваем скорость, для
for i in range(4):  # большей продуктивности
    turtle.left(90 * i)
    turtle.forward(turtle.getscreen().window_width() / 2)
    turtle.home()
turtle.forward(80)
turtle.left(90)
turtle.forward(80)
# turtle.left(90)
for i in range(1, 5):
    turtle.left(90)
    turtle.forward(160)
turtle.up()
turtle.home()
turtle.down()

turtle.speed(0.1)  # для наглядности уменьшим скорость



check = 0
grad = 90
step = 4

radius = turtle.numinput("Радиус", "Введите радиус круга:", 300, minval=10, maxval=300)
Radius()





