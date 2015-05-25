import turtle
import math


def pixel(a):  # процедура рисования пикселя
   # turtle.forward(a)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.end_fill()

turtle.listen()
turtle.bye()  # обновляем поле
turtle.ht()  # скрываем черпаху
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

"""if x1 >= y1:  # рассматриваем два варианта:
    axis = 1  # потому что алгоритмы отличаются
    kf = y1 / x1
else:
    kf = kf = x1 / y1
    axis = 0"""

#print("Угловой коэффициент: ", kf)
check = 0
grad = 90
radius = 80
step = 4
"""if axis == 0:
    turtle.forward(a)
    turtle.left(90)
    grad = -90"""
turtle.sety(radius)
turtle.setx(0)
# дальше начинается сам процесс рисования
turtle.down()
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

while turtle.xcor() > 0 and turtle.ycor() > -radius:
    mh1 = int(abs((turtle.xcor() - step)**2 + turtle.ycor() ** 2 - radius**2))
    md2 = int(abs((turtle.xcor()-step)**2+(turtle.ycor()-step)**2 - radius**2))
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
""" turtle.backward(a)
        check -= 1
        turtle.up()
        turtle.left(grad)
        turtle.forward(a)
        turtle.right(grad)
        turtle.forward(a)
        turtle.down()"""





