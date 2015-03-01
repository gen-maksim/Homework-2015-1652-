from turtle import *
bye()
ht()
def Pixel(a):
    forward(a)
    begin_fill()
    for i in range (1,5):
        left(90)
        forward(a)
    end_fill()

speed(0.1)
for i in range (4):
    left(90*i)
    forward(getscreen().window_width()/2)
    home()
speed(3)
x1=10#int(input('введите х'))
y1=3#int(input('введите у'))

kf=y1/x1
print(kf)
check=0
while xcor()<x1*5:
    print(check)
    if(check<=0.5):
        Pixel(5)
        check+=kf
    else:
        backward(5)
        check-=1
        up()
        left(90)
        forward(5)
        right(90)
        forward(5)
        down()


        
