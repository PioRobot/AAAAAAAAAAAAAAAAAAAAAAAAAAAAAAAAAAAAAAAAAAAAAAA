import turtle
import math
import tkinter as TK
#dont type in 10
a=input("1 for addition 2 for subtraction 3 for multiplication 4 for division 5 for elevation 6 for percentages 7 for perfect squares 8 for deltaV 9 for square roots 10 for trygonometry:")

def sum():
    s1 = float(input("insert first number:"))
    s2 = float(input("insert second number:"))
    s3 = s1 + s2
    print("the answer is: " + str(s3))

def mus():
    m1 = float(input("insert first number:"))
    m2 = float(input("insert second number:"))
    m3 = m1 - m2
    print("the answer is: " + str(m3)) 

def mult():
    t1 = float(input("insert first number:"))
    t2 = float(input("insert second number:"))
    t3 = t1 * t2
    print("the answer is: " + str(t3))

def div():
    d1 = float(input("insert first number:"))
    d2 = float(input("insert second number:"))
    d3 = d1 / d2
    print("your answer is: " + str(d3))

def tpo():
    tp1 = int(input("select number:"))
    tp2 = int(input("raised to the power of:"))
    tp3 = tp1 ** tp2
    print("the answer is: " + str(tp3))

def per():
    pe1 = float(input("percentage:"))
    pe2 = float(input("of:"))
    pe3 = pe1 / 100 * pe2
    print("answer: " + str(pe3))

def ps():
    ps1 = int(input("select numb:"))
    ps2 = math.sqrt(ps1)
    if ps2 == int(ps2):
        print("number is a perfect square")
    else:
        print("number isn't a perfect square")

def dv():
    dv1 = float(input("weight of rocket with fuel (tons):"))
    dv2 = float(input("weight of rocket without fuel (tons):"))
    dv3 = float(input("thrust of rocket (tons):"))
    dv4 = dv1 / dv2
    dv5 = dv4 * 3
    print("your delta v is: " + str(dv5))

def sr():
    sr1 = int(input("select number:"))
    print("the square root is: " + str(math.sqrt(sr1)))

def trygonometry():
    import math
    angle1 = math.radians(int(input("Enter angle 1 in degrees: ")))
    side1 = int(input("Enter side 1 length: "))
    angle2 = math.radians(int(input("Enter angle 2 in degrees: ")))
    side2 = int(input("Enter side 2 length: "))
    x1 = 0
    y1 = 0
    x2 = side1 * math.cos(angle1)
    y2 = side1 * math.sin(angle1)
    x3 = x2 + side2 * math.cos(angle2)
    y3 = y2 + side2 * math.sin(angle2)
    print("Vertex 1: (", x1, ",", y1, ")")

def draw_triangle(x1, y1, x2, y2, x3, y3):

    trygonometry()

    turtle.penup()

    turtle.goto(x1, y1)

    turtle.pendown()

    turtle.goto(x2, y2)

    turtle.goto(x3, y3)

    turtle.goto(x1, y1)

    

    draw_triangle(-100, 0, 100, 0, 0, 100)



    turtle.done()

if a=="1":

    sum()

elif a=="2":

    mus()

elif a=="3":

    mult()

elif a=="4":

    div()

elif a=="5":

    tpo()

elif a=="6":

    per()

elif a=="7":

    ps()

elif a=="8":

    dv()

elif a=="9":

    sr()

elif a=="10":
    trygonometry()
    draw_triangle()
else:
    print("invalid input")