import turtle
import math
turtle.bye()                #обновляем поле
turtle.ht()                 #скрываем черпаху

def Pixel(a):               #процедура рисования пикселя
    turtle.forward(a)
    turtle.begin_fill()
    for i in range (1,5):
        turtle.left(90)
        turtle.forward(a)
    turtle.end_fill()


turtle.speed(0.1)           #рисуем сетку. увеличиваем скорость, для
for i in range (4):         #большей продуктивности
    turtle.left(90*i)
    turtle.forward(turtle.getscreen().window_width()/2)
    turtle.home()
turtle.forward(300)
turtle.left(90)
turtle.forward(300)
#turtle.left(90)
for i in range (1,5):
    turtle.left(90)
    turtle.forward(600)
turtle.up()
turtle.home()
turtle.down()


turtle.speed(0)               #для наглядности уменьшим скорость
x1=int(input('введите х: '))    #принимаем данные и вычисляем коэф
y1=int(input('введите у: '))
a=int(input('Задайте размер пикселя: '))

if x1>=y1:                      #рассматриваем два варианта:
    axis=1                      #потому что алгоритмы отличаются
    kf=y1/x1
else:
    kf=kf=x1/y1
    axis=0
    
print("Угловой коэффициент: ",kf)
check=0
grad=90
if axis==0:
    turtle.forward(a)
    turtle.left(90)
    grad=-90
                                #дальше начинается сам процесс рисования
while turtle.xcor()<x1*5 and turtle.ycor()<y1*5:
    if(check<=0.5):
        Pixel(a)
        check+=kf
    else:
        turtle.backward(a)
        check-=1
        turtle.up()
        turtle.left(grad)
        turtle.forward(a)
        turtle.right(grad)
        turtle.forward(a)
        turtle.down()
input('намите Enter, чтобы закончить')
exit()


        
