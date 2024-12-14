import tkinter as tk
import turtle
import string
import random

root = tk.Tk()
root.geometry('600x600')
root.config(bg="silver")
root.minsize(600,600)
root.maxsize(600,600)

canvas = tk.Canvas(root, width=400,height=270, bg="silver")
canvas.pack()
screen = turtle.TurtleScreen(canvas)
screen.bgcolor('silver')
cat = turtle.RawTurtle(screen)
cat.speed(15)

def draw_circle(color, radius, x, y):
    cat.penup()
    cat.fillcolor(color)
    cat.goto(x, y)
    cat.pendown()
    cat.begin_fill()
    cat.circle(radius)
    cat.end_fill()

def draw_triangle(color, x, y):
    cat.fillcolor(color)
    cat.begin_fill()
    cat.goto(x, y)
    cat.pendown()
    for _ in range(3):
        cat.forward(50)
        cat.left(120)
    cat.end_fill()


def draw_cat():

    # Уши
    cat.penup()
    cat.goto(-72, 90)
    cat.pendown()
    draw_triangle("gray", -72, 90)

    cat.penup()
    cat.goto(22, 90)
    cat.pendown()
    draw_triangle("gray", 22, 90)

    # Голова
    draw_circle("gray", 100, 0, -80)

    # Глаза
    draw_circle("white", 30, -35, -10)  # Левый глаз
    draw_circle("white", 30, 35, -10)  # Правый глаз
    draw_circle("black", 10, -35, -2)  # Левый зрачок
    draw_circle("black", 10, 35, -2)  # Правый зрачок

    # Нос
    draw_circle("pink", 10, 0, -30)

    # Рот
    cat.penup()
    cat.goto(0, -40)
    cat.pendown()
    cat.right(90)
    cat.circle(20, 180)

    cat.penup()
    cat.goto(-40, -40)
    cat.pendown()
    cat.right(-180)
    cat.circle(20, 180)

def final_gen_pass():
    try:
        length = int(entry.get())
        if 1 <= length <= 99:
            text1.delete("1.0",tk.END)
            password = gen_pass(length)
            text1.insert("1.0", password)
        else:
            text1.delete("1.0", tk.END)
            text1.insert("1.0","Длина пароля должна быть от 1 до 99 символов. Попробуйте еще раз.")
    except ValueError:
        text1.insert("1.0","Пожалуйста, введите корректное число.")

text = tk.Text(root,height=3,width=50)
text.insert("1.0","генератор поролей от Matvic.corp")
text.config(state="disabled")
text.pack()

entry = tk.Entry(root,width=2)
entry.place(x=100,y=350)

mas = tk.Message(root,text="укажите длину пароля (от 1 до 99)=>")
mas.place(x=10,y=315)

butt = tk.Button(root,text="сгенерировать",command=final_gen_pass)
butt.place(x=10,y=380)

text1 = tk.Text(root,height=3,width=33)
text1.place(x=100,y=420)

def gen_pass(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

draw_cat()
cat.hideturtle()
root.mainloop()